"""
HEM Product Catalogue v3 - HEM Brand Ultra-Premium Edition
===========================================================
UI/UX Pro Max Enhanced — Luxury Light Theme with Premium Animations

HEM Corporation Brand System:
  Primary:    HEM Crimson Red    #c8102e
  Secondary:  Saffron Amber      #e8870a
  Accent:     Warm Gold          #fdbc00
  Deep Gold:  Burnished Gold     #b8860b
  Background: Warm Cream White   #fff9f5
  Cards:      Pure White         #ffffff
  Sidebar:    Deep Garnet        #1a0508
  Dark Text:  Charcoal           #1a0a0a

Design Principles (UI/UX Pro Max):
  • Motion conveys meaning — every animation has cause-effect
  • 150–300ms micro-interactions with ease-out enter / ease-in exit
  • Spring physics via cubic-bezier for natural feel
  • transform/opacity only — no width/height animation (GPU composited)
  • Stagger list/grid entrances at 30–50ms per item
  • Reduced-motion fallback respects prefers-reduced-motion
  • Accessibility: 4.5:1 contrast, focus rings, ARIA-compatible

Injected via st.markdown(APP_CSS, unsafe_allow_html=True) in app.py.
"""

APP_CSS = """
<style>
/* ═══════════════════════════════════════════════════════════════════════════
   GOOGLE FONTS — Cinzel (luxury serif) + Inter (clean body)
═══════════════════════════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;1,600&display=swap');

/* ═══════════════════════════════════════════════════════════════════════════
   CSS DESIGN TOKENS — HEM Brand Ultra-Premium
═══════════════════════════════════════════════════════════════════════════ */
:root {
    /* ── HEM Brand Reds ── */
    --hem-red:        #c8102e;
    --hem-red-deep:   #8b0a1e;
    --hem-red-light:  #e8304a;
    --hem-red-pale:   #fdedf0;
    --hem-red-ultra:  #ff2244;
    --hem-red-glow:   rgba(200,16,46,0.18);
    --hem-red-glow-sm:rgba(200,16,46,0.10);

    /* ── Saffron / Amber ── */
    --saffron:        #e8870a;
    --saffron-light:  #f5a832;
    --saffron-pale:   #fff5e6;
    --saffron-glow:   rgba(232,135,10,0.20);

    /* ── Gold Palette ── */
    --gold:           #fdbc00;
    --gold-dark:      #b8860b;
    --gold-burnished: #c9973d;
    --gold-pale:      #fffbe6;
    --gold-glow:      rgba(253,188,0,0.25);
    --gold-shine:     rgba(253,188,0,0.60);

    /* ── Light Backgrounds ── */
    --bg-page:        #fff9f5;
    --bg-card:        #ffffff;
    --bg-card-warm:   #fffaf7;
    --bg-cream:       #fdf5ee;
    --bg-cream-deep:  #f8ede0;
    --bg-sidebar:     #1a0508;
    --bg-glass:       rgba(255,255,255,0.75);
    --bg-glass-warm:  rgba(255,249,245,0.80);

    /* ── Borders ── */
    --border-red:     rgba(200,16,46,0.22);
    --border-saffron: rgba(232,135,10,0.25);
    --border-gold:    rgba(253,188,0,0.35);
    --border-light:   rgba(0,0,0,0.07);
    --border-medium:  rgba(0,0,0,0.11);
    --border-glass:   rgba(255,255,255,0.65);

    /* ── Text ── */
    --text-dark:   #1a0a0a;
    --text-body:   #3d2020;
    --text-mid:    #6b4040;
    --text-muted:  #a07070;
    --text-white:  #ffffff;
    --text-cream:  rgba(255,220,200,0.85);

    /* ── Premium Shadows ── */
    --shadow-xs:   0 1px 3px rgba(0,0,0,0.06);
    --shadow-sm:   0 2px 8px rgba(200,16,46,0.07), 0 1px 4px rgba(0,0,0,0.05);
    --shadow-md:   0 6px 20px rgba(200,16,46,0.09), 0 3px 10px rgba(0,0,0,0.07);
    --shadow-lg:   0 12px 40px rgba(200,16,46,0.11), 0 6px 20px rgba(0,0,0,0.08);
    --shadow-xl:   0 20px 60px rgba(200,16,46,0.14), 0 10px 30px rgba(0,0,0,0.10);
    --shadow-red:  0 6px 24px rgba(200,16,46,0.32), 0 2px 8px rgba(200,16,46,0.20);
    --shadow-gold: 0 4px 20px rgba(253,188,0,0.30), 0 2px 8px rgba(0,0,0,0.06);
    --shadow-glow: 0 0 0 3px rgba(200,16,46,0.15), 0 0 20px rgba(200,16,46,0.10);

    /* ── Radius ── */
    --r-xs:  4px;
    --r-sm:  8px;
    --r-md:  14px;
    --r-lg:  20px;
    --r-xl:  28px;
    --r-pill:50px;

    /* ── Animation Timing (UI/UX Pro Max §7) ── */
    --t-instant: 0.08s cubic-bezier(0.4,0,1,1);
    --t-fast:    0.15s cubic-bezier(0,0,0.2,1);
    --t-normal:  0.25s cubic-bezier(0,0,0.2,1);
    --t-spring:  0.35s cubic-bezier(0.34,1.56,0.64,1);
    --t-slow:    0.40s cubic-bezier(0,0,0.2,1);
    --t-exit:    0.10s cubic-bezier(0.4,0,1,1);

    /* ── Blur ── */
    --blur-sm:  blur(8px);
    --blur-md:  blur(16px);
    --blur-lg:  blur(24px);
}

/* ═══════════════════════════════════════════════════════════════════════════
   GLOBAL BASE
═══════════════════════════════════════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; }

.stApp {
    background: var(--bg-page) !important;
    color: var(--text-body) !important;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

.main .block-container {
    background: transparent !important;
    padding-top: 1.2rem;
    max-width: 1440px;
}

/* Luxury warm ambient background — animated orbs */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 70% 50% at 8%  5%,  rgba(200,16,46,0.055) 0%, transparent 55%),
        radial-gradient(ellipse 55% 45% at 92% 88%, rgba(232,135,10,0.045) 0%, transparent 55%),
        radial-gradient(ellipse 40% 30% at 50% 50%, rgba(253,188,0,0.020) 0%, transparent 60%),
        linear-gradient(160deg, #fff9f5 0%, #fdf4ee 40%, #fff9f5 100%);
    z-index: -1;
    pointer-events: none;
    animation: ambient-shift 18s ease-in-out infinite alternate;
}

@keyframes ambient-shift {
    0%   { opacity: 1; }
    50%  { opacity: 0.85; }
    100% { opacity: 1; }
}

/* Floating orb decorations */
.stApp::after {
    content: '';
    position: fixed;
    width: 600px; height: 600px;
    border-radius: 50%;
    top: -200px; right: -200px;
    background: radial-gradient(circle, rgba(253,188,0,0.035) 0%, transparent 65%);
    z-index: -1;
    pointer-events: none;
    animation: orb-drift 24s ease-in-out infinite alternate;
}

@keyframes orb-drift {
    0%   { transform: translate(0, 0) scale(1); }
    100% { transform: translate(-60px, 80px) scale(1.15); }
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE ENTRANCE ANIMATION
═══════════════════════════════════════════════════════════════════════════ */
@keyframes fade-up {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes fade-in {
    from { opacity: 0; }
    to   { opacity: 1; }
}

@keyframes slide-in-left {
    from { opacity: 0; transform: translateX(-20px); }
    to   { opacity: 1; transform: translateX(0); }
}

@keyframes scale-in {
    from { opacity: 0; transform: scale(0.95); }
    to   { opacity: 1; transform: scale(1); }
}

/* Stagger children — applied via CSS animation-delay */
.main .block-container > * {
    animation: fade-up 0.35s cubic-bezier(0,0,0.2,1) both;
}
.main .block-container > *:nth-child(1) { animation-delay: 0.02s; }
.main .block-container > *:nth-child(2) { animation-delay: 0.06s; }
.main .block-container > *:nth-child(3) { animation-delay: 0.10s; }
.main .block-container > *:nth-child(4) { animation-delay: 0.14s; }
.main .block-container > *:nth-child(5) { animation-delay: 0.18s; }

/* ═══════════════════════════════════════════════════════════════════════════
   MAIN TITLE BANNER — Cinematic Multi-Layer Animation
═══════════════════════════════════════════════════════════════════════════ */

/* ── Particle orbs that float inside the banner ── */
@keyframes orb-float-1 {
    0%   { transform: translate(0px,   0px)   scale(1.0); opacity: 0.18; }
    33%  { transform: translate(30px, -20px)  scale(1.2); opacity: 0.28; }
    66%  { transform: translate(-20px, 15px)  scale(0.9); opacity: 0.14; }
    100% { transform: translate(0px,   0px)   scale(1.0); opacity: 0.18; }
}
@keyframes orb-float-2 {
    0%   { transform: translate(0px,  0px)  scale(1.0); opacity: 0.12; }
    40%  { transform: translate(-40px, 25px) scale(1.3); opacity: 0.22; }
    80%  { transform: translate(20px, -15px) scale(0.85); opacity: 0.10; }
    100% { transform: translate(0px,  0px)  scale(1.0); opacity: 0.12; }
}
@keyframes orb-float-3 {
    0%   { transform: translate(0,  0) scale(1);   opacity: 0.15; }
    50%  { transform: translate(25px, 30px) scale(1.15); opacity: 0.25; }
    100% { transform: translate(0,  0) scale(1);   opacity: 0.15; }
}

/* ── Banner entrance ── */
@keyframes banner-drop-in {
    0%   { opacity: 0; transform: translateY(-24px) scale(0.96); }
    60%  { opacity: 1; transform: translateY(4px)   scale(1.01); }
    100% { opacity: 1; transform: translateY(0)     scale(1.00); }
}

/* ── Shimmer sweeps ── */
@keyframes banner-shimmer {
    0%   { left: -160%; }
    55%  { left: 160%; }
    100% { left: 160%; }
}
@keyframes banner-shimmer-2 {
    0%   { left: -160%; }
    55%  { left: 160%; }
    100% { left: 160%; }
}

/* ── Bottom gold glow ── */
@keyframes gold-glow-pulse {
    0%   { opacity: 0.55; filter: blur(0.5px); }
    100% { opacity: 1.00; filter: blur(2px) drop-shadow(0 0 8px rgba(253,188,0,0.90)); }
}

/* ── Rotating halo ring behind banner ── */
@keyframes halo-spin {
    from { transform: translateX(-50%) rotate(0deg); }
    to   { transform: translateX(-50%) rotate(360deg); }
}

/* ── Title brand letter-by-letter reveal ── */
@keyframes text-shimmer {
    0%   { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
@keyframes title-rise {
    0%   { opacity: 0; transform: translateY(22px) scaleY(0.88); letter-spacing: 4px; }
    60%  { opacity: 1; transform: translateY(-3px)  scaleY(1.02); }
    100% { opacity: 1; transform: translateY(0)     scaleY(1.00); letter-spacing: 12px; }
}

/* ── Subtitle typewriter-style fade ── */
@keyframes subtitle-appear {
    0%   { opacity: 0; transform: translateY(10px); letter-spacing: 2px; }
    100% { opacity: 1; transform: translateY(0);    letter-spacing: 6px; }
}

/* ── Decorative corner ornament pulse ── */
@keyframes ornament-breathe {
    0%, 100% { opacity: 0.28; transform: scale(1)    rotate(0deg);   }
    50%       { opacity: 0.55; transform: scale(1.15) rotate(15deg);  }
}

/* ── Scanning line sweep ── */
@keyframes scan-line {
    0%   { top: 0%;   opacity: 0; }
    5%   { opacity: 0.35; }
    95%  { opacity: 0.35; }
    100% { top: 100%; opacity: 0; }
}

.main-title {
    background:
        linear-gradient(135deg,
            #9b0820 0%,
            #c8102e 25%,
            #a50d26 50%,
            #c8102e 75%,
            #8b0a1e 100%);
    border-radius: var(--r-xl);
    padding: 44px 60px 34px;
    margin-bottom: 32px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow:
        var(--shadow-xl),
        inset 0 1px 0 rgba(255,255,255,0.13),
        inset 0 -1px 0 rgba(0,0,0,0.22);
    animation: banner-drop-in 0.70s cubic-bezier(0.34,1.10,0.64,1) both;
}

/* ── Floating amber orb — top-left ── */
.main-title-orb-1 {
    position: absolute;
    top: -40px; left: -40px;
    width: 180px; height: 180px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(232,135,10,0.35) 0%, transparent 65%);
    pointer-events: none;
    animation: orb-float-1 8s ease-in-out infinite;
}

/* ── Floating gold orb — bottom-right ── */
.main-title-orb-2 {
    position: absolute;
    bottom: -50px; right: -50px;
    width: 220px; height: 220px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(253,188,0,0.28) 0%, transparent 65%);
    pointer-events: none;
    animation: orb-float-2 11s ease-in-out infinite;
}

/* ── Floating crimson orb — center ── */
.main-title-orb-3 {
    position: absolute;
    top: 50%; left: 30%;
    width: 140px; height: 140px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,40,70,0.12) 0%, transparent 65%);
    pointer-events: none;
    animation: orb-float-3 14s ease-in-out infinite;
}

/* ── Primary shimmer sweep ── */
.main-title::before {
    content: '';
    position: absolute;
    top: -50%; left: -160%;
    width: 75%; height: 200%;
    background: linear-gradient(
        100deg,
        transparent 15%,
        rgba(255,225,155,0.16) 40%,
        rgba(253,188,0,0.28)   50%,
        rgba(255,225,155,0.16) 60%,
        transparent 85%
    );
    transform: skewX(-18deg);
    animation: banner-shimmer 5s ease-in-out 0.8s infinite;
    pointer-events: none;
}

/* ── Secondary offset shimmer ── */
.main-title-shimmer2 {
    position: absolute;
    top: -50%; left: -160%;
    width: 40%; height: 200%;
    background: linear-gradient(
        100deg,
        transparent 20%,
        rgba(255,255,255,0.10) 50%,
        transparent 80%
    );
    transform: skewX(-18deg);
    animation: banner-shimmer-2 5s ease-in-out 2.5s infinite;
    pointer-events: none;
    z-index: 1;
}

/* ── Scanning line ── */
.main-title-scan {
    position: absolute;
    left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg,
        transparent,
        rgba(253,188,0,0.45) 30%,
        rgba(255,255,255,0.30) 50%,
        rgba(253,188,0,0.45) 70%,
        transparent);
    animation: scan-line 6s ease-in-out 1s infinite;
    pointer-events: none;
    z-index: 2;
}

/* ── Bottom gold glow bar ── */
.main-title::after {
    content: '';
    position: absolute;
    bottom: 0; left: 4%; right: 4%;
    height: 3px;
    background: linear-gradient(90deg,
        transparent,
        var(--saffron-light) 15%,
        var(--gold) 50%,
        var(--saffron-light) 85%,
        transparent);
    animation: gold-glow-pulse 2.8s ease-in-out infinite alternate;
    pointer-events: none;
}

/* ── Corner ornaments ── */
.main-title .ornament-left,
.main-title .ornament-right {
    position: absolute;
    top: 14px;
    font-size: 22px;
    color: var(--gold);
    animation: ornament-breathe 4s ease-in-out infinite;
}
.main-title .ornament-left  { left: 28px;  animation-delay: 0s;   }
.main-title .ornament-right { right: 28px; animation-delay: 2s;   }

/* ═══════════════════════════════════════════════════════════════════════════
   AGARBATTI (INCENSE STICK) ANIMATION
═══════════════════════════════════════════════════════════════════════════ */

/* ── Smoke particle waft keyframes (4 directions for variety) ── */
@keyframes waft-a {
    0%   { transform: translateY(0px)   translateX(0px)  scale(0.4) rotate(0deg);   opacity: 0.72; border-radius: 50%; }
    20%  { transform: translateY(-18px) translateX(5px)  scale(0.7) rotate(8deg);   opacity: 0.58; border-radius: 60% 40% 55% 45%; }
    45%  { transform: translateY(-40px) translateX(-4px) scale(1.1) rotate(-6deg);  opacity: 0.38; border-radius: 45% 55% 60% 40%; }
    70%  { transform: translateY(-65px) translateX(7px)  scale(1.5) rotate(10deg);  opacity: 0.18; border-radius: 55% 45% 40% 60%; }
    100% { transform: translateY(-95px) translateX(-3px) scale(2.0) rotate(-5deg);  opacity: 0;    border-radius: 50%; }
}
@keyframes waft-b {
    0%   { transform: translateY(0px)   translateX(0px)  scale(0.35) rotate(0deg);  opacity: 0.68; border-radius: 50%; }
    25%  { transform: translateY(-22px) translateX(-6px) scale(0.65) rotate(-9deg); opacity: 0.52; border-radius: 55% 45% 50% 50%; }
    50%  { transform: translateY(-48px) translateX(5px)  scale(1.05) rotate(7deg);  opacity: 0.32; border-radius: 40% 60% 45% 55%; }
    75%  { transform: translateY(-72px) translateX(-8px) scale(1.55) rotate(-8deg); opacity: 0.14; border-radius: 60% 40% 55% 45%; }
    100% { transform: translateY(-100px)translateX(4px)  scale(2.1) rotate(5deg);   opacity: 0;    border-radius: 50%; }
}
@keyframes waft-c {
    0%   { transform: translateY(0px)   translateX(0px)  scale(0.45) rotate(0deg);  opacity: 0.65; border-radius: 50%; }
    30%  { transform: translateY(-28px) translateX(8px)  scale(0.80) rotate(12deg); opacity: 0.48; border-radius: 50% 50% 60% 40%; }
    60%  { transform: translateY(-58px) translateX(-6px) scale(1.20) rotate(-8deg); opacity: 0.26; border-radius: 45% 55% 40% 60%; }
    100% { transform: translateY(-92px) translateX(5px)  scale(1.90) rotate(6deg);  opacity: 0;    border-radius: 55% 45% 50% 50%; }
}
@keyframes waft-d {
    0%   { transform: translateY(0px)   translateX(0px)  scale(0.30) rotate(0deg);  opacity: 0.75; border-radius: 50%; }
    35%  { transform: translateY(-32px) translateX(-7px) scale(0.70) rotate(-11deg);opacity: 0.55; border-radius: 60% 40% 50% 50%; }
    65%  { transform: translateY(-62px) translateX(9px)  scale(1.15) rotate(9deg);  opacity: 0.28; border-radius: 40% 60% 55% 45%; }
    100% { transform: translateY(-98px) translateX(-5px) scale(1.85) rotate(-7deg); opacity: 0;    border-radius: 50%; }
}

/* ── Ember glow pulse ── */
@keyframes ember-glow {
    0%,100% {
        box-shadow:
            0 0 4px 2px rgba(255,100,30,0.90),
            0 0 10px 4px rgba(255,140,0,0.60),
            0 0 18px 8px rgba(200,16,46,0.35);
        background: radial-gradient(circle, #ff8c00 0%, #ff4500 60%, #c8102e 100%);
    }
    50% {
        box-shadow:
            0 0 6px 3px rgba(255,120,40,1.00),
            0 0 16px 6px rgba(255,160,0,0.75),
            0 0 28px 12px rgba(200,16,46,0.50);
        background: radial-gradient(circle, #ffb300 0%, #ff6600 55%, #c8102e 100%);
    }
}

/* ── Stick group wrapper ── */
.agarbatti-group {
    position: absolute;
    bottom: 0;
    display: flex;
    align-items: flex-end;
    gap: 18px;
    z-index: 4;
}
.agarbatti-group.left  { left: 18px; }
.agarbatti-group.right { right: 18px; flex-direction: row-reverse; }

/* ── Single agarbatti wrapper ── */
.agarbatti {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 20px;
}

/* ── Stick itself ── */
.aga-stick {
    width: 3px;
    height: 90px;
    background: linear-gradient(180deg,
        #3a1c00 0%,
        #6b3a10 30%,
        #8b5e2a 60%,
        #a07840 80%,
        #c49a5a 100%);
    border-radius: 2px 2px 0 0;
    position: relative;
    box-shadow: 1px 0 3px rgba(0,0,0,0.35);
}

/* Burnt portion at top of stick (darker, charred look) */
.aga-stick::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 28px;
    background: linear-gradient(180deg, #0a0a0a 0%, #1a0a00 60%, transparent 100%);
    border-radius: 2px 2px 0 0;
}

/* ── Base / holder ── */
.aga-base {
    width: 18px; height: 10px;
    background: linear-gradient(135deg, #b8860b, #fdbc00, #b8860b);
    border-radius: 3px 3px 6px 6px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.25);
    position: relative;
}
.aga-base::after {
    content: '';
    position: absolute;
    top: 3px; left: 50%; transform: translateX(-50%);
    width: 3px; height: 100%;
    background: rgba(0,0,0,0.20);
    border-radius: 1px;
}

/* ── Ember tip ── */
.aga-ember {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: radial-gradient(circle, #ff8c00 0%, #ff4500 60%, #c8102e 100%);
    animation: ember-glow 1.8s ease-in-out infinite;
    position: relative;
    z-index: 5;
    margin-bottom: -1px;
}

/* ── Smoke column ── */
.aga-smoke {
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    height: 100px;
    pointer-events: none;
}

/* ── Individual smoke particles ── */
.smoke-p {
    position: absolute;
    bottom: 0; left: 50%;
    transform: translateX(-50%);
    width: 10px; height: 10px;
    background: rgba(210,190,170,0.55);
    border-radius: 50%;
    filter: blur(2.5px);
}
.smoke-p:nth-child(1) { animation: waft-a 2.8s ease-out 0.0s infinite; }
.smoke-p:nth-child(2) { animation: waft-b 2.8s ease-out 0.56s infinite; }
.smoke-p:nth-child(3) { animation: waft-c 2.8s ease-out 1.12s infinite; }
.smoke-p:nth-child(4) { animation: waft-d 2.8s ease-out 1.68s infinite; }
.smoke-p:nth-child(5) { animation: waft-a 2.8s ease-out 2.24s infinite; }

/* Second stick — slightly offset timing */
.agarbatti:nth-child(2) .smoke-p:nth-child(1) { animation-delay: 0.40s; }
.agarbatti:nth-child(2) .smoke-p:nth-child(2) { animation-delay: 0.96s; }
.agarbatti:nth-child(2) .smoke-p:nth-child(3) { animation-delay: 1.52s; }
.agarbatti:nth-child(2) .smoke-p:nth-child(4) { animation-delay: 2.08s; }
.agarbatti:nth-child(2) .smoke-p:nth-child(5) { animation-delay: 2.64s; }
.agarbatti:nth-child(2) .aga-ember { animation-delay: 0.9s; }

/* Slight lean for second stick */
.agarbatti:nth-child(2) { transform: rotate(-4deg); transform-origin: bottom center; }

/* Right group sticks lean opposite */
.agarbatti-group.right .agarbatti:nth-child(1) { transform: rotate(2deg); transform-origin: bottom center; }
.agarbatti-group.right .agarbatti:nth-child(2) { transform: rotate(6deg);  transform-origin: bottom center; }

/* ── Brand name — rise + flowing gold shimmer ── */
.main-title .title-brand {
    font-family: 'Cinzel', serif;
    font-size: 50px;
    font-weight: 900;
    letter-spacing: 12px;
    text-transform: uppercase;
    background: linear-gradient(135deg,
        #ffd84d 0%,
        #fdbc00 18%,
        #ffffff 40%,
        #ffe88a 55%,
        #fdbc00 72%,
        #f5a832 88%,
        #ffd84d 100%);
    background-size: 250% 100%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: block;
    margin-bottom: 10px;
    filter: drop-shadow(0 4px 18px rgba(0,0,0,0.35));
    animation:
        title-rise   0.80s cubic-bezier(0.34,1.10,0.64,1) 0.15s both,
        text-shimmer 5s   linear                           1.0s  infinite;
    position: relative;
    z-index: 3;
}

/* ── Subtitle ── */
.main-title .title-sub {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 6px;
    text-transform: uppercase;
    color: rgba(255,215,190,0.78);
    display: block;
    margin-top: 6px;
    animation: subtitle-appear 0.70s cubic-bezier(0,0,0.2,1) 0.60s both;
    position: relative;
    z-index: 3;
}

/* ═══════════════════════════════════════════════════════════════════════════
   TAB NAVIGATION — Premium animated
═══════════════════════════════════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--r-lg);
    padding: 5px 6px;
    gap: 3px;
    box-shadow: var(--shadow-sm), inset 0 1px 0 rgba(255,255,255,0.9);
    animation: fade-up 0.30s ease 0.08s both;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 12px;
    padding: 10px 26px;
    font-weight: 600;
    font-size: 12.5px;
    color: var(--text-mid) !important;
    background: transparent !important;
    border: 1px solid transparent !important;
    transition: color var(--t-fast), background var(--t-fast), border-color var(--t-fast), box-shadow var(--t-fast), transform var(--t-fast) !important;
    letter-spacing: 0.4px;
    font-family: 'Inter', sans-serif;
    position: relative;
    text-transform: uppercase;
}

.stTabs [data-baseweb="tab"]:hover {
    color: var(--hem-red) !important;
    background: var(--hem-red-pale) !important;
    border-color: var(--border-red) !important;
    transform: translateY(-1px) !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #c8102e 0%, #a50d26 100%) !important;
    color: #ffffff !important;
    border-color: transparent !important;
    box-shadow: var(--shadow-red) !important;
    transform: translateY(-1px) !important;
}

/* Animated gold dot above active tab */
.stTabs [aria-selected="true"]::before {
    content: '';
    position: absolute;
    top: 4px; left: 50%;
    transform: translateX(-50%);
    width: 4px; height: 4px;
    border-radius: 50%;
    background: var(--gold);
    box-shadow: 0 0 6px 1px rgba(253,188,0,0.75);
    animation: gold-dot-pulse 2s ease-in-out infinite;
}

@keyframes gold-dot-pulse {
    0%, 100% { transform: translateX(-50%) scale(1);   opacity: 1; }
    50%       { transform: translateX(-50%) scale(1.5); opacity: 0.7; }
}

.stTabs [data-baseweb="tab-highlight"] { display: none !important; }

/* ═══════════════════════════════════════════════════════════════════════════
   FOCUS STATES — Accessibility (WCAG AA, priority 1)
═══════════════════════════════════════════════════════════════════════════ */
button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible,
[role="checkbox"]:focus-visible,
[data-testid="stCheckbox"] input:focus-visible,
[data-baseweb="tab"]:focus-visible,
a:focus-visible {
    outline: 2.5px solid var(--hem-red) !important;
    outline-offset: 2px !important;
    box-shadow: 0 0 0 4px rgba(200,16,46,0.15) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   BUTTONS — Premium with micro-interactions
═══════════════════════════════════════════════════════════════════════════ */

/* ── All buttons base ── */
.stButton button, button[kind] {
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition:
        transform var(--t-fast),
        box-shadow var(--t-fast),
        background var(--t-fast),
        border-color var(--t-fast) !important;
}

/* Ripple effect on all buttons */
.stButton button::after, button[kind]::after {
    content: '';
    position: absolute;
    top: 50%; left: 50%;
    width: 0; height: 0;
    border-radius: 50%;
    background: rgba(255,255,255,0.28);
    transform: translate(-50%, -50%);
    transition: width 0.45s ease, height 0.45s ease, opacity 0.45s ease;
    opacity: 0;
    pointer-events: none;
}
.stButton button:active::after, button[kind]:active::after {
    width: 300px; height: 300px;
    opacity: 0;
    transition: 0s;
}

/* Shimmer sweep on primary hover */
.stButton button::before, button[kind="primary"]::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 200%; height: 100%;
    background: linear-gradient(90deg, transparent 30%, rgba(255,255,255,0.18) 50%, transparent 70%);
    transition: left 0.50s ease;
    pointer-events: none;
}
.stButton button:hover::before, button[kind="primary"]:hover::before { left: 100%; }

/* ── Primary ── */
button[kind="primary"],
.stButton button[kind="primary"] {
    background: linear-gradient(135deg,
        #c8102e 0%,
        #e8304a 50%,
        #c8102e 100%) !important;
    color: #ffffff !important;
    border: none !important;
    font-weight: 700 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 11.5px !important;
    letter-spacing: 1.4px !important;
    text-transform: uppercase !important;
    border-radius: var(--r-sm) !important;
    padding: 11px 24px !important;
    box-shadow: var(--shadow-red), inset 0 1px 0 rgba(255,255,255,0.18) !important;
}
button[kind="primary"]:hover,
.stButton button[kind="primary"]:hover {
    background: linear-gradient(135deg, #d42035 0%, #f03050 50%, #d42035 100%) !important;
    box-shadow: 0 8px 28px rgba(200,16,46,0.45), inset 0 1px 0 rgba(255,255,255,0.22) !important;
    transform: translateY(-2px) !important;
}
button[kind="primary"]:active,
.stButton button[kind="primary"]:active {
    transform: translateY(0px) scale(0.98) !important;
    box-shadow: 0 2px 10px rgba(200,16,46,0.30) !important;
}

/* ── Secondary ── */
button[kind="secondary"],
.stButton button[kind="secondary"] {
    background: var(--saffron-pale) !important;
    color: var(--saffron) !important;
    border: 1px solid var(--border-saffron) !important;
    font-weight: 600 !important;
    font-size: 11.5px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border-radius: var(--r-sm) !important;
}
button[kind="secondary"]:hover,
.stButton button[kind="secondary"]:hover {
    background: rgba(232,135,10,0.14) !important;
    border-color: var(--saffron) !important;
    box-shadow: 0 4px 14px rgba(232,135,10,0.25) !important;
    transform: translateY(-2px) !important;
}
button[kind="secondary"]:active { transform: translateY(0) scale(0.98) !important; }

/* ── Tertiary / default ── */
button[kind="tertiary"],
.stButton button {
    background: var(--bg-card) !important;
    color: var(--text-mid) !important;
    border: 1px solid var(--border-light) !important;
    font-weight: 500 !important;
    border-radius: var(--r-sm) !important;
    font-size: 12px !important;
    letter-spacing: 0.3px !important;
}
button[kind="tertiary"]:hover,
.stButton button:hover {
    background: var(--hem-red-pale) !important;
    color: var(--hem-red) !important;
    border-color: var(--border-red) !important;
    transform: translateY(-1px) !important;
    box-shadow: var(--shadow-sm) !important;
}

/* ── Danger button ── */
.btn-danger,
button[data-testid*="clear"],
button[data-testid*="delete"],
button[data-testid*="remove"] {
    background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%) !important;
    color: #ffffff !important;
    border: none !important;
    font-weight: 700 !important;
    border-radius: var(--r-sm) !important;
    box-shadow: 0 4px 16px rgba(220,38,38,0.32) !important;
}
.btn-danger:hover,
button[data-testid*="clear"]:hover,
button[data-testid*="delete"]:hover,
button[data-testid*="remove"]:hover {
    background: linear-gradient(135deg, #b91c1c 0%, #991b1b 100%) !important;
    box-shadow: 0 8px 24px rgba(220,38,38,0.45) !important;
    transform: translateY(-2px) !important;
}
.btn-danger:active { transform: translateY(0) scale(0.98) !important; }

/* ── Download button ── */
[data-testid="stDownloadButton"] button {
    background: linear-gradient(135deg,
        rgba(253,188,0,0.15) 0%,
        rgba(253,188,0,0.08) 100%) !important;
    color: var(--gold-dark) !important;
    border: 1px solid var(--border-gold) !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    font-size: 11.5px !important;
    border-radius: var(--r-sm) !important;
    box-shadow: var(--shadow-gold) !important;
}
[data-testid="stDownloadButton"] button:hover {
    background: rgba(253,188,0,0.22) !important;
    box-shadow: 0 6px 20px rgba(253,188,0,0.35) !important;
    transform: translateY(-2px) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   INPUT FIELDS — Polished focus states
═══════════════════════════════════════════════════════════════════════════ */
.stTextInput input,
.stTextInput textarea {
    background: var(--bg-card) !important;
    color: var(--text-dark) !important;
    border: 1.5px solid var(--border-medium) !important;
    border-radius: var(--r-md) !important;
    padding: 11px 16px !important;
    font-size: 14px !important;
    font-family: 'Inter', sans-serif !important;
    transition: border-color var(--t-fast), box-shadow var(--t-fast) !important;
    box-shadow: var(--shadow-xs) !important;
}
.stTextInput input::placeholder { color: var(--text-muted) !important; opacity: 0.7; }
.stTextInput input:focus {
    border-color: var(--hem-red) !important;
    box-shadow: 0 0 0 3px var(--hem-red-glow), var(--shadow-sm) !important;
    outline: none !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: var(--bg-card) !important;
    border: 1.5px solid var(--border-medium) !important;
    border-radius: var(--r-md) !important;
    color: var(--text-dark) !important;
    box-shadow: var(--shadow-xs) !important;
    transition: border-color var(--t-fast), box-shadow var(--t-fast) !important;
}
.stSelectbox > div > div:focus-within {
    border-color: var(--hem-red) !important;
    box-shadow: 0 0 0 3px var(--hem-red-glow), var(--shadow-sm) !important;
}

/* Multiselect */
.stMultiSelect > div > div {
    background: var(--bg-card) !important;
    border: 1.5px solid var(--border-medium) !important;
    border-radius: var(--r-md) !important;
    box-shadow: var(--shadow-xs) !important;
    transition: border-color var(--t-fast), box-shadow var(--t-fast) !important;
}
.stMultiSelect > div > div:focus-within {
    border-color: var(--hem-red) !important;
    box-shadow: 0 0 0 3px var(--hem-red-glow) !important;
}

/* Chips/Tags */
[data-baseweb="tag"] {
    background: linear-gradient(135deg, rgba(200,16,46,0.10), rgba(200,16,46,0.06)) !important;
    border: 1px solid var(--border-red) !important;
    color: var(--hem-red) !important;
    border-radius: var(--r-pill) !important;
    font-weight: 600 !important;
    font-size: 11px !important;
    animation: tag-appear 0.20s cubic-bezier(0.34,1.56,0.64,1) both;
}
@keyframes tag-appear {
    from { opacity: 0; transform: scale(0.8); }
    to   { opacity: 1; transform: scale(1); }
}

/* Number input */
.stNumberInput input {
    background: var(--bg-card) !important;
    border: 1.5px solid var(--border-medium) !important;
    border-radius: var(--r-md) !important;
    color: var(--text-dark) !important;
    box-shadow: var(--shadow-xs) !important;
}
.stNumberInput input:focus {
    border-color: var(--saffron) !important;
    box-shadow: 0 0 0 3px var(--saffron-glow) !important;
}

/* Textarea */
.stTextArea textarea {
    background: var(--bg-card) !important;
    border: 1.5px solid var(--border-medium) !important;
    border-radius: var(--r-md) !important;
    color: var(--text-dark) !important;
    box-shadow: var(--shadow-xs) !important;
}
.stTextArea textarea:focus {
    border-color: var(--hem-red) !important;
    box-shadow: 0 0 0 3px var(--hem-red-glow) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   SIDEBAR — Deep garnet luxury
═══════════════════════════════════════════════════════════════════════════ */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(170deg,
            #1a0508 0%,
            #230b0e 30%,
            #1f0709 60%,
            #140305 100%) !important;
    border-right: 1.5px solid rgba(200,16,46,0.30) !important;
    box-shadow: 6px 0 32px rgba(0,0,0,0.18), 2px 0 0 rgba(200,16,46,0.12);
    animation: slide-in-left 0.35s cubic-bezier(0,0,0.2,1) both;
}

/* Sidebar shimmer accent on the right border */
section[data-testid="stSidebar"]::before {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 2px; height: 100%;
    background: linear-gradient(180deg,
        transparent 0%,
        rgba(232,135,10,0.35) 20%,
        rgba(253,188,0,0.55) 50%,
        rgba(232,135,10,0.35) 80%,
        transparent 100%);
    animation: sidebar-glow 4s ease-in-out infinite alternate;
    pointer-events: none;
}
@keyframes sidebar-glow {
    0%   { opacity: 0.6; }
    100% { opacity: 1.0; }
}

section[data-testid="stSidebar"] > div { padding-top: 1.5rem; }

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: var(--saffron-light) !important;
    font-family: 'Cinzel', serif !important;
    letter-spacing: 0.5px;
    text-shadow: 0 1px 6px rgba(232,135,10,0.20);
}
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stMarkdown {
    color: var(--text-cream) !important;
}
section[data-testid="stSidebar"] .stCaption {
    color: rgba(200,130,130,0.60) !important;
    font-size: 11px;
}

/* Sidebar inputs */
section[data-testid="stSidebar"] .stTextInput input {
    background: rgba(255,255,255,0.07) !important;
    color: #fff9f5 !important;
    border-color: rgba(232,135,10,0.28) !important;
    backdrop-filter: var(--blur-sm);
}
section[data-testid="stSidebar"] .stTextInput input:focus {
    border-color: rgba(232,135,10,0.65) !important;
    box-shadow: 0 0 0 2px rgba(232,135,10,0.20) !important;
}
section[data-testid="stSidebar"] .stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    color: #fff9f5 !important;
    border-color: rgba(232,135,10,0.28) !important;
}

/* Sidebar buttons */
section[data-testid="stSidebar"] button {
    background: rgba(232,135,10,0.13) !important;
    color: var(--saffron-light) !important;
    border: 1px solid rgba(232,135,10,0.32) !important;
    font-weight: 600 !important;
    font-size: 11.5px !important;
    letter-spacing: 0.5px !important;
    transition: all var(--t-fast) !important;
}
section[data-testid="stSidebar"] button:hover {
    background: rgba(232,135,10,0.26) !important;
    border-color: rgba(232,135,10,0.55) !important;
    box-shadow: 0 0 16px rgba(232,135,10,0.22), 0 2px 8px rgba(0,0,0,0.20) !important;
    transform: translateY(-1px) !important;
}
section[data-testid="stSidebar"] button:active { transform: translateY(0) !important; }

/* Sidebar expanders */
section[data-testid="stSidebar"] .streamlit-expanderHeader {
    background: rgba(255,255,255,0.04) !important;
    color: var(--saffron-light) !important;
    border: 1px solid rgba(200,16,46,0.18) !important;
    border-radius: var(--r-md) !important;
    transition: all var(--t-fast) !important;
    backdrop-filter: var(--blur-sm);
}
section[data-testid="stSidebar"] .streamlit-expanderHeader:hover {
    background: rgba(200,16,46,0.12) !important;
    border-color: rgba(200,16,46,0.35) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   GLASS PANEL — Frosted glassmorphism
═══════════════════════════════════════════════════════════════════════════ */
.glass-panel {
    background: var(--bg-glass-warm);
    backdrop-filter: var(--blur-md) saturate(1.4);
    -webkit-backdrop-filter: var(--blur-md) saturate(1.4);
    border: 1px solid var(--border-glass);
    border-radius: var(--r-lg);
    padding: 22px 26px;
    box-shadow: var(--shadow-md), inset 0 1px 0 rgba(255,255,255,0.8);
    margin: 10px 0;
    transition: box-shadow var(--t-normal), transform var(--t-normal);
}
.glass-panel:hover {
    box-shadow: var(--shadow-lg), inset 0 1px 0 rgba(255,255,255,0.9);
    transform: translateY(-1px);
}

/* ═══════════════════════════════════════════════════════════════════════════
   EXPANDERS
═══════════════════════════════════════════════════════════════════════════ */
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    color: var(--text-body) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--r-md) !important;
    padding: 13px 20px !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
    transition: all var(--t-fast) !important;
    box-shadow: var(--shadow-sm) !important;
    position: relative;
    overflow: hidden;
}

/* Left accent line on expander hover */
.streamlit-expanderHeader::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, var(--hem-red), var(--saffron));
    border-radius: 0 0 0 var(--r-md);
    transform: scaleY(0);
    transform-origin: bottom;
    transition: transform var(--t-normal);
}
.streamlit-expanderHeader:hover::before { transform: scaleY(1); }
.streamlit-expanderHeader:hover {
    border-color: var(--border-red) !important;
    color: var(--hem-red) !important;
    background: var(--hem-red-pale) !important;
    box-shadow: var(--shadow-md) !important;
    padding-left: 24px !important;
}
.streamlit-expanderContent {
    background: var(--bg-card-warm) !important;
    border: 1px solid var(--border-light) !important;
    border-top: none !important;
    border-radius: 0 0 var(--r-md) var(--r-md) !important;
    padding: 14px 20px 18px !important;
    animation: fade-up 0.25s ease both;
}

/* ═══════════════════════════════════════════════════════════════════════════
   SECTION HEADERS
═══════════════════════════════════════════════════════════════════════════ */
.section-header {
    background:
        radial-gradient(ellipse at left, rgba(200,16,46,0.07) 0%, transparent 55%),
        linear-gradient(135deg,
            var(--hem-red-pale) 0%,
            rgba(232,135,10,0.04) 60%,
            var(--hem-red-pale) 100%);
    border: 1px solid var(--border-red);
    border-left: 4px solid var(--hem-red);
    border-radius: 0 var(--r-md) var(--r-md) 0;
    padding: 14px 24px;
    margin: 22px 0 16px;
    font-family: 'Cinzel', serif;
    font-size: 17px;
    font-weight: 700;
    color: var(--hem-red-deep);
    letter-spacing: 0.8px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: var(--shadow-sm);
    position: relative;
    overflow: hidden;
    animation: slide-in-left 0.30s ease both;
}
.section-header::after {
    content: '';
    position: absolute;
    right: 0; top: 0; bottom: 0;
    width: 60px;
    background: linear-gradient(90deg, transparent, rgba(253,188,0,0.06));
}

/* ═══════════════════════════════════════════════════════════════════════════
   GLASS CARD — Elevated white card with animated top border
═══════════════════════════════════════════════════════════════════════════ */
.glass-card {
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--r-xl);
    padding: 26px 30px;
    box-shadow: var(--shadow-md);
    margin: 14px 0;
    transition:
        border-color var(--t-normal),
        box-shadow var(--t-normal),
        transform var(--t-normal);
    position: relative;
    overflow: hidden;
}
.glass-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg,
        var(--hem-red),
        var(--saffron),
        var(--gold),
        var(--saffron),
        var(--hem-red));
    background-size: 200% 100%;
    animation: card-border-flow 5s linear infinite;
}
@keyframes card-border-flow {
    0%   { background-position: 0% 0; }
    100% { background-position: 200% 0; }
}
.glass-card:hover {
    border-color: var(--border-red);
    box-shadow: var(--shadow-lg);
    transform: translateY(-3px);
}

/* ═══════════════════════════════════════════════════════════════════════════
   STATS BAR
═══════════════════════════════════════════════════════════════════════════ */
.stats-bar {
    display: flex;
    gap: 12px;
    align-items: stretch;
    background: transparent;
    margin: 14px 0 20px;
    flex-wrap: wrap;
}
.stat-item {
    font-size: 11px;
    color: var(--text-muted);
    font-weight: 500;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    background: var(--bg-cream);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    padding: 12px 18px;
    flex: 1;
    min-width: 80px;
    transition:
        background var(--t-fast),
        border-color var(--t-fast),
        box-shadow var(--t-fast),
        transform var(--t-fast);
    position: relative;
    overflow: hidden;
}
.stat-item::before {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, var(--hem-red), var(--saffron));
    transform: scaleX(0);
    transition: transform var(--t-normal);
}
.stat-item:hover {
    background: var(--hem-red-pale);
    border-color: var(--border-red);
    box-shadow: var(--shadow-md);
    transform: translateY(-3px);
}
.stat-item:hover::before { transform: scaleX(1); }
.stat-value {
    font-size: 22px;
    font-weight: 700;
    color: var(--hem-red);
    font-family: 'Cinzel', serif;
    display: block;
    line-height: 1.2;
    margin-top: 3px;
    letter-spacing: -0.5px;
}

/* ═══════════════════════════════════════════════════════════════════════════
   PRODUCT BADGES — Animated
═══════════════════════════════════════════════════════════════════════════ */
.badge-new {
    display: inline-block;
    background: linear-gradient(135deg, var(--hem-red), var(--hem-red-deep));
    color: #ffffff;
    font-size: 9px;
    font-weight: 800;
    padding: 2.5px 9px;
    border-radius: var(--r-pill);
    margin-left: 6px;
    text-transform: uppercase;
    letter-spacing: 1px;
    vertical-align: middle;
    animation: badge-pulse 2.2s cubic-bezier(0.4,0,0.6,1) infinite;
    box-shadow: 0 2px 8px rgba(200,16,46,0.35);
}
@keyframes badge-pulse {
    0%, 100% { box-shadow: 0 2px 8px rgba(200,16,46,0.35); }
    50%       { box-shadow: 0 2px 14px rgba(200,16,46,0.60), 0 0 0 3px rgba(200,16,46,0.10); }
}

.badge-modified {
    display: inline-block;
    background: var(--saffron-pale);
    color: var(--saffron);
    font-size: 9px; font-weight: 800;
    padding: 2.5px 9px; border-radius: var(--r-pill);
    border: 1px solid var(--border-saffron);
    margin-left: 6px; text-transform: uppercase; letter-spacing: 1px;
    vertical-align: middle;
    box-shadow: 0 1px 4px rgba(232,135,10,0.18);
}

.badge-custom {
    display: inline-block;
    background: linear-gradient(135deg, rgba(253,188,0,0.18), rgba(253,188,0,0.08));
    color: var(--gold-dark);
    font-size: 9px; font-weight: 800;
    padding: 2.5px 9px; border-radius: var(--r-pill);
    border: 1px solid var(--border-gold);
    margin-left: 6px; text-transform: uppercase; letter-spacing: 1px;
    vertical-align: middle;
    box-shadow: 0 1px 4px rgba(253,188,0,0.20);
}

.badge-in-cart {
    display: inline-block;
    background: linear-gradient(135deg, var(--hem-red), var(--hem-red-deep));
    color: #ffffff;
    font-size: 9px; font-weight: 800;
    padding: 2.5px 9px; border-radius: var(--r-pill);
    margin-left: 6px; text-transform: uppercase; letter-spacing: 1px;
    vertical-align: middle;
    box-shadow: 0 2px 8px rgba(200,16,46,0.30);
}

/* ═══════════════════════════════════════════════════════════════════════════
   SUBCATEGORY HEADER
═══════════════════════════════════════════════════════════════════════════ */
.subcat-header {
    background: linear-gradient(90deg, var(--saffron-pale) 0%, transparent 100%);
    border-left: 3px solid var(--saffron);
    padding: 9px 18px;
    margin: 16px 0 8px;
    border-radius: 0 var(--r-sm) var(--r-sm) 0;
    font-size: 11.5px;
    font-weight: 700;
    color: var(--saffron);
    letter-spacing: 1px;
    text-transform: uppercase;
    animation: slide-in-left 0.22s ease both;
}

/* ═══════════════════════════════════════════════════════════════════════════
   PRODUCT THUMBNAIL — Hover zoom + glow
═══════════════════════════════════════════════════════════════════════════ */
.product-thumb {
    border-radius: var(--r-sm);
    border: 1px solid var(--border-red);
    object-fit: cover;
    background: var(--bg-cream);
    box-shadow: var(--shadow-sm);
    transition: transform var(--t-spring), box-shadow var(--t-normal);
}
.product-thumb:hover {
    transform: scale(1.10);
    box-shadow: 0 6px 20px rgba(200,16,46,0.20);
}
.product-thumb-placeholder {
    border-radius: var(--r-sm);
    border: 1.5px dashed var(--border-medium);
    background: linear-gradient(135deg, var(--bg-cream), var(--bg-cream-deep));
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; color: var(--text-muted);
}

/* ═══════════════════════════════════════════════════════════════════════════
   PRODUCT ROW — Luxury hover lift
═══════════════════════════════════════════════════════════════════════════ */
.product-row-hover {
    border-radius: var(--r-sm);
    transition:
        background var(--t-fast),
        border-color var(--t-fast),
        transform var(--t-fast),
        box-shadow var(--t-fast);
    padding: 7px 12px;
    margin: 2px 0;
    border-left: 3px solid transparent;
    position: relative;
}
.product-row-hover::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: var(--r-sm);
    background: linear-gradient(90deg, rgba(200,16,46,0.04), transparent);
    opacity: 0;
    transition: opacity var(--t-fast);
}
.product-row-hover:hover {
    background: var(--hem-red-pale);
    border-left-color: var(--hem-red);
    transform: translateX(3px);
    box-shadow: -2px 0 0 var(--hem-red);
}
.product-row-hover:hover::before { opacity: 1; }

/* ═══════════════════════════════════════════════════════════════════════════
   CONFIRM DIALOGS
═══════════════════════════════════════════════════════════════════════════ */
.confirm-dialog {
    background: var(--saffron-pale);
    border: 1px solid var(--border-saffron);
    border-left: 4px solid var(--saffron);
    border-radius: var(--r-md);
    padding: 16px 22px;
    margin: 10px 0;
    color: var(--saffron);
    font-size: 13.5px;
    animation: fade-up 0.25s ease both;
}
.confirm-dialog-danger {
    background: var(--hem-red-pale);
    border: 1px solid var(--border-red);
    border-left: 4px solid var(--hem-red);
    border-radius: var(--r-md);
    padding: 16px 22px;
    margin: 10px 0;
    color: var(--hem-red-deep);
    font-size: 13.5px;
    animation: fade-up 0.25s ease both;
}

/* ═══════════════════════════════════════════════════════════════════════════
   DATA EDITOR
═══════════════════════════════════════════════════════════════════════════ */
div[data-testid="stDataEditor"] {
    border: 1px solid var(--border-light) !important;
    border-radius: var(--r-lg) !important;
    overflow: hidden !important;
    box-shadow: var(--shadow-md) !important;
}
div[data-testid="stDataEditor"] thead th {
    background: linear-gradient(135deg, var(--hem-red-pale), rgba(200,16,46,0.04)) !important;
    color: var(--hem-red-deep) !important;
    font-weight: 700 !important;
    font-size: 11px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border-bottom: 2px solid var(--border-red) !important;
}
div[data-testid="stDataEditor"] tbody tr {
    transition: background var(--t-fast);
}
div[data-testid="stDataEditor"] tbody tr:hover {
    background: var(--hem-red-pale) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   METRICS — Animated on hover
═══════════════════════════════════════════════════════════════════════════ */
[data-testid="stMetric"] {
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--r-lg);
    padding: 20px 24px;
    box-shadow: var(--shadow-sm);
    transition: all var(--t-normal);
    position: relative;
    overflow: hidden;
}
[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg,
        var(--hem-red),
        var(--saffron),
        var(--gold));
    background-size: 200% 100%;
    animation: card-border-flow 4s linear infinite;
}
[data-testid="stMetric"]::after {
    content: '';
    position: absolute;
    bottom: -30px; right: -30px;
    width: 100px; height: 100px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(200,16,46,0.06) 0%, transparent 70%);
    transition: transform var(--t-normal);
}
[data-testid="stMetric"]:hover {
    border-color: var(--border-red);
    box-shadow: var(--shadow-lg);
    transform: translateY(-3px);
}
[data-testid="stMetric"]:hover::after { transform: scale(1.5); }
[data-testid="stMetricLabel"] {
    color: var(--text-muted) !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
[data-testid="stMetricValue"] {
    color: var(--hem-red) !important;
    font-family: 'Cinzel', serif !important;
    font-size: 30px !important;
    font-weight: 700 !important;
    line-height: 1.1 !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   ALERTS
═══════════════════════════════════════════════════════════════════════════ */
.stAlert { border-radius: var(--r-md) !important; animation: fade-up 0.25s ease both; }
[data-testid="stAlert"] {
    border-radius: var(--r-md) !important;
    background: var(--bg-card) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   PROGRESS BAR — Animated gradient
═══════════════════════════════════════════════════════════════════════════ */
.stProgress > div > div > div {
    background: linear-gradient(90deg,
        var(--hem-red),
        var(--saffron),
        var(--gold),
        var(--saffron),
        var(--hem-red)) !important;
    background-size: 200% 100% !important;
    border-radius: 6px !important;
    box-shadow: 0 0 10px rgba(232,135,10,0.35) !important;
    animation: progress-flow 2s linear infinite !important;
}
@keyframes progress-flow {
    0%   { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
.stProgress > div > div {
    background: var(--border-light) !important;
    border-radius: 6px !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   FORM
═══════════════════════════════════════════════════════════════════════════ */
.stForm {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--r-xl) !important;
    padding: 26px !important;
    box-shadow: var(--shadow-md) !important;
    position: relative;
    overflow: hidden;
    animation: fade-up 0.30s ease both;
}
.stForm::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg,
        var(--hem-red), var(--saffron), var(--gold), var(--saffron), var(--hem-red));
    background-size: 200% 100%;
    animation: card-border-flow 5s linear infinite;
}

/* ═══════════════════════════════════════════════════════════════════════════
   CHECKBOXES
═══════════════════════════════════════════════════════════════════════════ */
[data-testid="stCheckbox"] label {
    color: var(--text-body) !important;
    font-size: 13px !important;
    transition: color var(--t-fast);
}
[data-testid="stCheckbox"] label:hover { color: var(--hem-red) !important; }
[data-testid="stCheckbox"] input[type="checkbox"]:checked + div {
    background: var(--hem-red) !important;
    border-color: var(--hem-red) !important;
    box-shadow: 0 2px 8px rgba(200,16,46,0.30) !important;
    animation: checkbox-pop 0.20s cubic-bezier(0.34,1.56,0.64,1);
}
@keyframes checkbox-pop {
    from { transform: scale(0.8); }
    to   { transform: scale(1); }
}

/* ═══════════════════════════════════════════════════════════════════════════
   RADIO BUTTONS
═══════════════════════════════════════════════════════════════════════════ */
[data-testid="stRadio"] label {
    color: var(--text-body) !important;
    transition: color var(--t-fast);
}
[data-testid="stRadio"] label:hover { color: var(--hem-red) !important; }

/* ═══════════════════════════════════════════════════════════════════════════
   DIVIDERS — Decorative
═══════════════════════════════════════════════════════════════════════════ */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg,
        transparent 0%,
        var(--border-light) 20%,
        var(--border-light) 80%,
        transparent 100%) !important;
    margin: 28px 0 !important;
    position: relative;
}
hr::after {
    content: '◆';
    position: absolute;
    left: 50%; transform: translateX(-50%) translateY(-55%);
    background: var(--bg-page);
    padding: 0 10px;
    font-size: 9px;
    color: var(--gold);
    letter-spacing: 2px;
}

/* ═══════════════════════════════════════════════════════════════════════════
   SCROLLBAR — Branded
═══════════════════════════════════════════════════════════════════════════ */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: rgba(253,188,0,0.04); border-radius: 3px; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--hem-red-light), var(--saffron));
    border-radius: 3px;
    transition: background var(--t-fast);
}
::-webkit-scrollbar-thumb:hover { background: var(--hem-red); }

/* ═══════════════════════════════════════════════════════════════════════════
   TOAST — Slide-in + branded
═══════════════════════════════════════════════════════════════════════════ */
[data-testid="stToast"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-light) !important;
    border-left: 4px solid var(--hem-red) !important;
    border-radius: var(--r-md) !important;
    color: var(--text-body) !important;
    box-shadow: var(--shadow-xl) !important;
    animation: toast-slide-in 0.30s cubic-bezier(0.34,1.20,0.64,1) both;
}
@keyframes toast-slide-in {
    from { opacity: 0; transform: translateX(60px) scale(0.95); }
    to   { opacity: 1; transform: translateX(0) scale(1); }
}

/* ═══════════════════════════════════════════════════════════════════════════
   SKELETON SHIMMER — Loading placeholder
═══════════════════════════════════════════════════════════════════════════ */
.skeleton {
    background: linear-gradient(90deg,
        var(--bg-cream-deep) 25%,
        var(--bg-cream) 50%,
        var(--bg-cream-deep) 75%);
    background-size: 200% 100%;
    border-radius: var(--r-sm);
    animation: skeleton-shimmer 1.5s ease infinite;
}
@keyframes skeleton-shimmer {
    0%   { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

/* ═══════════════════════════════════════════════════════════════════════════
   EMPTY STATE — Pulsing ring
═══════════════════════════════════════════════════════════════════════════ */
.empty-state {
    text-align: center;
    padding: 64px 20px;
    color: var(--text-muted);
    animation: fade-in 0.40s ease both;
}
.empty-state-icon {
    font-size: 52px;
    margin-bottom: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 84px; height: 84px;
    border-radius: 50%;
    background: var(--hem-red-pale);
    border: 2px solid var(--border-red);
    margin-left: auto; margin-right: auto;
    animation: empty-ring-pulse 3s cubic-bezier(0.4,0,0.6,1) infinite;
    transition: transform var(--t-spring);
}
.empty-state-icon:hover { transform: scale(1.08); }

@keyframes empty-ring-pulse {
    0%, 100% {
        box-shadow:
            0 0 0 0   rgba(200,16,46,0.00),
            0 0 0 8px rgba(200,16,46,0.06);
    }
    50% {
        box-shadow:
            0 0 0 14px rgba(200,16,46,0.04),
            0 0 0 24px rgba(200,16,46,0.02);
    }
}

.empty-state-action {
    color: var(--hem-red);
    text-decoration: underline;
    cursor: pointer;
    font-size: 13px;
    font-weight: 500;
    margin-top: 10px;
    display: inline-block;
    transition: color var(--t-fast), transform var(--t-fast);
}
.empty-state-action:hover {
    color: var(--hem-red-deep);
    transform: translateY(-1px);
}

/* ═══════════════════════════════════════════════════════════════════════════
   HEM GOLD DIVIDER
═══════════════════════════════════════════════════════════════════════════ */
.gold-divider {
    height: 2px;
    background: linear-gradient(90deg,
        transparent 0%,
        var(--hem-red)      20%,
        var(--saffron)      50%,
        var(--gold)         65%,
        var(--saffron)      80%,
        transparent 100%);
    margin: 26px 0;
    border: none;
    opacity: 0.40;
    position: relative;
    animation: gold-divider-glow 4s ease-in-out infinite alternate;
}
@keyframes gold-divider-glow {
    0%   { opacity: 0.30; }
    100% { opacity: 0.55; }
}
.gold-divider::after {
    content: '◆';
    position: absolute;
    left: 50%; top: 50%;
    transform: translate(-50%, -50%);
    background: var(--bg-sidebar);
    padding: 0 8px;
    font-size: 8px;
    color: var(--gold);
    line-height: 1;
    animation: diamond-spin 8s linear infinite;
}
@keyframes diamond-spin {
    0%   { transform: translate(-50%, -50%) rotate(0deg); }
    100% { transform: translate(-50%, -50%) rotate(360deg); }
}

/* ═══════════════════════════════════════════════════════════════════════════
   CART BADGE — Glowing
═══════════════════════════════════════════════════════════════════════════ */
.cart-glow {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, var(--hem-red), var(--hem-red-deep));
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
    min-width: 24px; height: 24px;
    border-radius: var(--r-pill);
    padding: 0 8px;
    margin-left: 8px;
    box-shadow: 0 2px 10px rgba(200,16,46,0.45);
    letter-spacing: 0.5px;
    animation: cart-count-pulse 0.30s cubic-bezier(0.34,1.56,0.64,1);
}
@keyframes cart-count-pulse {
    from { transform: scale(0.7); }
    to   { transform: scale(1); }
}

/* ═══════════════════════════════════════════════════════════════════════════
   RESPONSIVE
═══════════════════════════════════════════════════════════════════════════ */
@media (max-width: 768px) {
    .main-title .title-brand { font-size: 28px; letter-spacing: 4px; }
    .main-title              { padding: 26px 20px 20px; }
    .stats-bar               { flex-direction: column; gap: 8px; }
    .section-header          { font-size: 15px; padding: 12px 18px; }
    .glass-card              { padding: 18px 20px; }
}

@media (max-width: 480px) {
    .main-title .title-brand { font-size: 22px; letter-spacing: 2px; }
    .stTabs [data-baseweb="tab"] { padding: 8px 14px; font-size: 11px; }
}

/* ═══════════════════════════════════════════════════════════════════════════
   REDUCED MOTION — Accessibility (mandatory per UI/UX Pro Max §7)
═══════════════════════════════════════════════════════════════════════════ */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration:   0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration:  0.01ms !important;
    }
}
</style>
"""
