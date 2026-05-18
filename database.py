"""
HEM Product Catalogue - Database Module
Persistent PostgreSQL (Supabase) database with session-state caching.
"""
import os
import json
import uuid
import logging
from datetime import datetime

import psycopg2
import streamlit as st

from config import SAVED_TEMPLATES_FILE
from imagekit_client import upload_custom_image

logger = logging.getLogger(__name__)

# =========================================================================
# Database Connection
# =========================================================================

def _get_conn():
    """Get a PostgreSQL connection from environment variable."""
    return psycopg2.connect(st.secrets["DATABASE_URL"])


# =========================================================================
# Database Schema
# =========================================================================

def get_empty_products_db():
    """Return the default empty database structure."""
    return {
        "version": 1,
        "last_updated": "",
        "product_overrides": {},
        "custom_products": [],
        "deleted_products": [],
        "saved_cart": [],
    }


# =========================================================================
# Core Load / Save with Session-State Caching
# =========================================================================

_DB_CACHE_KEY = "_products_db_cache"


def _load_from_cloud():
    """Load DB from Supabase PostgreSQL."""
    try:
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute("SELECT data FROM products_db ORDER BY last_updated DESC LIMIT 1")
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            logger.info("Database loaded from Supabase ✓")
            return row[0]  # JSONB auto-parsed to dict
    except Exception as e:
        logger.warning(f"Failed to load from Supabase: {e}")

    logger.info("Starting with empty database")
    return get_empty_products_db()


def _write_to_cloud(db):
    """Write DB to Supabase PostgreSQL."""
    try:
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM products_db")
        cur.execute(
            "INSERT INTO products_db (data) VALUES (%s)",
            (json.dumps(db),)
        )
        conn.commit()
        cur.close()
        conn.close()
        logger.info("Database saved to Supabase ✓")
    except Exception as e:
        logger.error(f"Failed to save to Supabase: {e}")
        raise


def load_products_db():
    """Load the products database using session-state cache."""
    if _DB_CACHE_KEY not in st.session_state:
        st.session_state[_DB_CACHE_KEY] = _load_from_cloud()
    return st.session_state[_DB_CACHE_KEY]


def save_products_db(db):
    """Save the products database to Supabase, update cache."""
    db["last_updated"] = datetime.now().isoformat()
    try:
        _write_to_cloud(db)
        st.session_state[_DB_CACHE_KEY] = db
    except Exception as e:
        logger.error(f"Failed to save products database: {e}")
        st.error(f"Failed to save products database: {e}")


def invalidate_db_cache():
    """Force reload from Supabase on next access."""
    if _DB_CACHE_KEY in st.session_state:
        del st.session_state[_DB_CACHE_KEY]


# =========================================================================
# Product Override Operations
# =========================================================================

def save_product_override(product_id, field_changes):
    db = load_products_db()
    if product_id not in db["product_overrides"]:
        db["product_overrides"][product_id] = {}
    db["product_overrides"][product_id].update(field_changes)
    save_products_db(db)


def remove_product_override(product_id, field_name=None):
    db = load_products_db()
    if product_id in db["product_overrides"]:
        if field_name:
            db["product_overrides"][product_id].pop(field_name, None)
            if not db["product_overrides"][product_id]:
                del db["product_overrides"][product_id]
        else:
            del db["product_overrides"][product_id]
    save_products_db(db)


# =========================================================================
# Product Delete / Hide Operations
# =========================================================================

def mark_product_deleted(product_id):
    db = load_products_db()
    if product_id not in db["deleted_products"]:
        db["deleted_products"].append(product_id)
    save_products_db(db)


def unmark_product_deleted(product_id):
    db = load_products_db()
    db["deleted_products"] = [pid for pid in db["deleted_products"] if pid != product_id]
    save_products_db(db)


# =========================================================================
# Custom Products
# =========================================================================

def add_custom_product_to_db(product_data):
    db = load_products_db()
    db["custom_products"].append(product_data)
    save_products_db(db)


def delete_custom_product_from_db(product_id):
    db = load_products_db()
    db["custom_products"] = [
        p for p in db["custom_products"] if p.get("ProductID") != product_id
    ]
    save_products_db(db)


def get_custom_products_from_db():
    db = load_products_db()
    return db.get("custom_products", [])


def add_custom_item(catalogue, category, subcategory, item_name,
                    fragrance, sku_code, is_new, image_file):
    img_url = ""
    if image_file:
        img_url = upload_custom_image(image_file)

    new_item = {
        "ProductID": f"CUST_{uuid.uuid4().hex[:8]}",
        "Catalogue": catalogue,
        "Category": category,
        "Subcategory": subcategory if subcategory else "N/A",
        "ItemName": item_name,
        "Fragrance": fragrance,
        "SKU Code": sku_code,
        "IsNew": 1 if is_new else 0,
        "ImageB64": img_url,
        "Packaging": "Default",
        "SerialNo": 0,
    }
    add_custom_product_to_db(new_item)
    return new_item


def delete_custom_item(pid):
    delete_custom_product_from_db(pid)


# =========================================================================
# Cart Persistence
# =========================================================================

def save_cart_to_db(cart_items):
    db = load_products_db()
    db["saved_cart"] = cart_items
    save_products_db(db)


def load_cart_from_db():
    db = load_products_db()
    return db.get("saved_cart", [])


# =========================================================================
# Template Management (still file-based as fallback)
# =========================================================================

def load_saved_templates():
    if os.path.exists(SAVED_TEMPLATES_FILE):
        try:
            with open(SAVED_TEMPLATES_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            logger.warning(f"Failed to load templates: {e}")
    return {}


def save_template_to_disk(name, cart_items):
    templates = load_saved_templates()
    templates[name] = cart_items
    try:
        with open(SAVED_TEMPLATES_FILE, 'w') as f:
            json.dump(templates, f, indent=4)
        st.toast(f"Template '{name}' saved!", icon="💾")
    except Exception as e:
        logger.error(f"Failed to save template: {e}")
        st.error(f"Failed to save template: {e}")


def delete_template(name):
    templates = load_saved_templates()
    if name in templates:
        del templates[name]
        try:
            with open(SAVED_TEMPLATES_FILE, 'w') as f:
                json.dump(templates, f, indent=4)
            st.toast(f"Template '{name}' deleted!", icon="🗑️")
        except Exception as e:
            logger.error(f"Failed to delete template: {e}")

# =========================================================================
# Migration (kept for backwards compatibility)
# =========================================================================

def migrate_old_custom_items():
    """Legacy migration function - kept for compatibility."""
    logger.info("Migration skipped - using Supabase now")
    return False
