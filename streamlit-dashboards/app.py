import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Explore the Universe — Cinematic Cosmos",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu, header, footer { visibility: hidden; }
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="collapsedControl"],
        [data-testid="stDeployButton"] { display: none !important; }
        .stApp {
            background: #000008;
            overflow: hidden;
        }
        .block-container {
            padding: 0 !important;
            max-width: none !important;
        }
        iframe {
            display: block;
            border: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

COSMOS_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Explore the Universe</title>
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Orbitron:wght@400;500;600;700;800;900&display=swap');

/* ═══════════════════════════════════════════════════════════════
   DESIGN TOKENS
   ═══════════════════════════════════════════════════════════════ */
:root {
  --bg: #000008;
  --cyan: #00e5ff;
  --cyan-soft: rgba(0,229,255,.35);
  --blue: #4a90ff;
  --pink: #ff2daa;
  --pink-soft: rgba(255,45,170,.30);
  --violet: #a855f7;
  --amber: #ffb347;
  --amber-soft: rgba(255,179,71,.30);
  --red: #ff3d57;
  --white: #f0f4ff;
  --muted: rgba(200,215,255,.60);
  --glass-bg: rgba(6,12,30,.55);
  --glass-border: rgba(100,200,255,.12);
  --glass-glow: rgba(0,229,255,.06);
  --card-bg: rgba(8,16,40,.60);
  --line: rgba(100,200,255,.08);
}

/* ═══════════════════════════════════════════════════════════════
   RESET & BASE
   ═══════════════════════════════════════════════════════════════ */
*,*::before,*::after { box-sizing:border-box; margin:0; padding:0; }
html {
  scroll-behavior:smooth;
  width:100%; max-width:100%; overflow-x:hidden;
}
body {
  width:100%; max-width:100%; min-height:100vh;
  background:var(--bg);
  color:var(--white);
  font-family:'Inter',system-ui,-apple-system,sans-serif;
  overflow-x:hidden;
  -webkit-font-smoothing:antialiased;
}
body::selection { background:rgba(0,229,255,.30); }
img { display:block; max-width:100%; }
a { color:inherit; text-decoration:none; }

/* ═══════════════════════════════════════════════════════════════
   WEBGL CANVAS (background)
   ═══════════════════════════════════════════════════════════════ */
#bg-canvas {
  position:fixed; inset:0; width:100%; height:100vh;
  z-index:0;
  background:
    radial-gradient(ellipse at 20% 20%, rgba(40,0,80,.30), transparent 50%),
    radial-gradient(ellipse at 80% 80%, rgba(0,60,120,.20), transparent 50%),
    var(--bg);
}

/* ═══════════════════════════════════════════════════════════════
   ATMOSPHERIC OVERLAYS
   ═══════════════════════════════════════════════════════════════ */
.aurora-overlay {
  position:fixed; inset:0; z-index:1; pointer-events:none;
  opacity:.60;
  background:
    radial-gradient(ellipse at 15% 30%, rgba(0,229,255,.12), transparent 45%),
    radial-gradient(ellipse at 85% 25%, rgba(255,45,170,.10), transparent 40%),
    radial-gradient(ellipse at 50% 80%, rgba(168,85,247,.08), transparent 50%);
  filter:blur(30px);
  animation:auroraDrift 40s ease-in-out infinite alternate;
}
.dust-overlay {
  position:fixed; inset:0; z-index:1; pointer-events:none;
  opacity:.18;
  background-image:
    radial-gradient(circle,rgba(255,255,255,.30) 0 .8px,transparent 1.2px),
    radial-gradient(circle,rgba(0,229,255,.20) 0 .6px,transparent 1px);
  background-size:140px 140px,200px 200px;
  animation:dustMove 120s linear infinite;
}
.vignette {
  position:fixed; inset:0; z-index:1; pointer-events:none;
  background:radial-gradient(ellipse at center,transparent 40%,rgba(0,0,0,.70) 100%);
}

@keyframes auroraDrift {
  0%{transform:translate3d(-2%,-1%,0) scale(1.02) rotate(-1deg)}
  100%{transform:translate3d(2%,1%,0) scale(1.06) rotate(1deg)}
}
@keyframes dustMove { to{background-position:600px 900px,-700px 500px} }

/* ═══════════════════════════════════════════════════════════════
   NAVIGATION
   ═══════════════════════════════════════════════════════════════ */
.nav {
  position:fixed; z-index:100; top:16px; left:50%; transform:translateX(-50%);
  width:min(1100px,calc(100vw - 32px));
  display:flex; align-items:center; justify-content:space-between; gap:16px;
  padding:10px 14px 10px 22px;
  border:1px solid rgba(0,229,255,.15);
  border-radius:60px;
  background:linear-gradient(135deg,rgba(4,10,28,.70),rgba(10,6,30,.55));
  backdrop-filter:blur(24px) saturate(1.4);
  box-shadow:
    0 20px 80px rgba(0,0,0,.50),
    inset 0 1px 0 rgba(255,255,255,.04),
    0 0 40px rgba(0,229,255,.04);
  transition:box-shadow .4s,border-color .4s;
}
.nav:hover {
  border-color:rgba(0,229,255,.28);
  box-shadow:0 20px 80px rgba(0,0,0,.50),0 0 60px rgba(0,229,255,.08);
}
.brand {
  font:800 11px/1 'Orbitron',sans-serif;
  letter-spacing:3px;
  color:var(--white);
  white-space:nowrap;
  text-shadow:0 0 20px rgba(0,229,255,.4);
}
.brand-dot {
  display:inline-block; width:6px; height:6px; border-radius:50%;
  background:var(--cyan);
  margin-left:6px; vertical-align:middle;
  box-shadow:0 0 10px var(--cyan),0 0 20px rgba(0,229,255,.3);
  animation:brandPulse 2s ease-in-out infinite;
}
@keyframes brandPulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.6;transform:scale(.8)} }

.nav-links { display:flex; gap:2px; align-items:center; flex-wrap:wrap; justify-content:flex-end; }
.nav a {
  color:rgba(200,220,255,.55);
  font:700 9px/1 'Orbitron',sans-serif;
  letter-spacing:1.2px;
  padding:10px 11px;
  border-radius:40px;
  transition:all .3s cubic-bezier(.25,.8,.25,1);
  position:relative;
}
.nav a:hover, .nav a.active {
  color:var(--white);
  background:rgba(0,229,255,.08);
  text-shadow:0 0 16px rgba(0,229,255,.6);
}
.nav a.active::after {
  content:"";
  position:absolute; bottom:4px; left:50%; transform:translateX(-50%);
  width:12px; height:2px; border-radius:2px;
  background:var(--cyan);
  box-shadow:0 0 8px var(--cyan);
}

/* ═══════════════════════════════════════════════════════════════
   MAIN CONTENT
   ═══════════════════════════════════════════════════════════════ */
main { position:relative; z-index:2; }

.section {
  min-height:100vh;
  display:grid; place-items:center;
  padding:100px max(24px,6vw);
  position:relative;
}
.section.tall { min-height:120vh; }
.section.ultra { min-height:140vh; }
.content { width:min(1200px,100%); margin:0 auto; }
.center { text-align:center; }

/* ═══════════════════════════════════════════════════════════════
   TYPOGRAPHY
   ═══════════════════════════════════════════════════════════════ */
.kicker {
  display:inline-flex; align-items:center; gap:12px;
  margin-bottom:20px;
  color:var(--cyan);
  text-transform:uppercase;
  letter-spacing:4px;
  font:700 10px/1 'Orbitron',sans-serif;
  text-shadow:0 0 20px rgba(0,229,255,.5);
}
.kicker::before,.kicker::after {
  content:"";
  width:50px; height:1px;
}
.kicker::before { background:linear-gradient(90deg,transparent,var(--cyan)); }
.kicker::after { background:linear-gradient(90deg,var(--pink),transparent); }

h1 {
  font-family:'Orbitron',sans-serif;
  font-size:clamp(48px,9vw,130px);
  line-height:.88;
  font-weight:900;
  text-transform:uppercase;
  margin:0;
  text-shadow:
    0 0 40px rgba(0,229,255,.20),
    0 0 100px rgba(168,85,247,.15),
    0 4px 60px rgba(0,0,0,.5);
  letter-spacing:-2px;
}
h2 {
  font-family:'Orbitron',sans-serif;
  font-size:clamp(36px,6vw,80px);
  line-height:.92;
  font-weight:800;
  text-transform:uppercase;
  margin:0;
  text-shadow:0 0 30px rgba(0,229,255,.15),0 0 80px rgba(168,85,247,.10);
}
.lead {
  width:min(680px,100%);
  margin:28px auto 0;
  color:var(--muted);
  font-size:clamp(15px,2vw,20px);
  line-height:1.8;
  font-weight:300;
}
.massive {
  font-size:clamp(52px,10vw,150px);
  text-shadow:0 0 50px rgba(0,229,255,.20),0 0 120px rgba(255,45,170,.12);
}
.subline {
  margin-top:24px;
  color:var(--cyan);
  font:800 clamp(16px,3vw,30px)/1 'Orbitron',sans-serif;
  letter-spacing:3px;
  text-shadow:0 0 20px rgba(0,229,255,.4);
}

/* ═══════════════════════════════════════════════════════════════
   BUTTONS
   ═══════════════════════════════════════════════════════════════ */
.actions {
  margin-top:40px;
  display:flex; justify-content:center; gap:18px;
  flex-wrap:wrap;
}
.btn {
  appearance:none; cursor:pointer;
  border:1.5px solid rgba(0,229,255,.35);
  border-radius:60px;
  background:linear-gradient(135deg,rgba(0,229,255,.12),rgba(168,85,247,.08));
  color:var(--white);
  padding:16px 32px;
  min-width:200px;
  font:800 11px/1 'Orbitron',sans-serif;
  letter-spacing:2px;
  text-transform:uppercase;
  position:relative;
  overflow:hidden;
  transition:all .4s cubic-bezier(.25,.8,.25,1);
  box-shadow:
    0 0 30px rgba(0,229,255,.10),
    inset 0 1px 0 rgba(255,255,255,.06);
}
.btn::before {
  content:"";
  position:absolute; inset:-2px;
  border-radius:62px;
  background:linear-gradient(135deg,var(--cyan),var(--pink),var(--violet));
  z-index:-1;
  opacity:0;
  transition:opacity .4s;
}
.btn:hover {
  transform:translateY(-3px);
  border-color:rgba(0,229,255,.60);
  box-shadow:
    0 0 50px rgba(0,229,255,.25),
    0 0 100px rgba(168,85,247,.12),
    0 8px 40px rgba(0,0,0,.3);
}
.btn:hover::before { opacity:.15; }
.btn:active { transform:translateY(-1px); }

.btn.secondary {
  background:rgba(6,12,30,.50);
  border-color:rgba(255,45,170,.30);
  box-shadow:0 0 30px rgba(255,45,170,.06);
}
.btn.secondary:hover {
  border-color:rgba(255,45,170,.55);
  box-shadow:0 0 50px rgba(255,45,170,.15),0 8px 40px rgba(0,0,0,.3);
}

/* ═══════════════════════════════════════════════════════════════
   SCROLL CUE
   ═══════════════════════════════════════════════════════════════ */
.scroll-cue {
  position:absolute; bottom:40px; left:50%; transform:translateX(-50%);
  color:rgba(200,220,255,.50);
  font:700 9px/1 'Orbitron',sans-serif;
  letter-spacing:3px;
  text-align:center;
}
.scroll-cue::after {
  content:"";
  display:block; width:1px; height:50px;
  margin:14px auto 0;
  background:linear-gradient(to bottom,var(--cyan),transparent);
  animation:scrollPulse 2s ease-in-out infinite;
}
@keyframes scrollPulse {
  0%,100%{transform:scaleY(.3);opacity:.3}
  50%{transform:scaleY(1);opacity:1}
}

/* ═══════════════════════════════════════════════════════════════
   GLASS CARDS
   ═══════════════════════════════════════════════════════════════ */
.glass {
  position:relative; overflow:hidden;
  border:1px solid var(--glass-border);
  border-radius:20px;
  background:linear-gradient(160deg,rgba(8,18,44,.65),rgba(14,8,36,.45));
  box-shadow:
    0 30px 100px rgba(0,0,0,.35),
    inset 0 1px 0 rgba(255,255,255,.05),
    0 0 60px var(--glass-glow);
  backdrop-filter:blur(20px);
}
.glass::before {
  content:"";
  position:absolute; inset:0;
  background:linear-gradient(120deg,transparent 0%,rgba(255,255,255,.05) 50%,transparent 70%);
  transform:translateX(-150%);
  transition:transform .8s cubic-bezier(.25,.8,.25,1);
  pointer-events:none;
}
.glass:hover::before { transform:translateX(150%); }
.glass::after {
  content:"";
  position:absolute; top:0; left:0; right:0; height:1px;
  background:linear-gradient(90deg,transparent,rgba(0,229,255,.20),transparent);
}

/* ═══════════════════════════════════════════════════════════════
   GRID LAYOUTS
   ═══════════════════════════════════════════════════════════════ */
.two-col {
  display:grid; grid-template-columns:1fr 1fr; gap:40px; align-items:center;
}
.grid-4 { display:grid; grid-template-columns:repeat(4,1fr); gap:18px; margin-top:40px; }
.grid-3 { display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin-top:40px; }

/* ═══════════════════════════════════════════════════════════════
   METRIC CARDS
   ═══════════════════════════════════════════════════════════════ */
.metric {
  min-height:160px; padding:28px;
}
.metric .label {
  display:block;
  color:rgba(200,220,255,.50);
  font:700 10px/1 'Orbitron',sans-serif;
  letter-spacing:2px;
  margin-bottom:20px;
}
.metric .value {
  display:block;
  font:900 clamp(28px,4vw,46px)/1 'Orbitron',sans-serif;
  color:var(--white);
  text-shadow:0 0 30px rgba(0,229,255,.3);
}
.metric .desc {
  display:block;
  color:var(--muted);
  margin-top:14px; line-height:1.6;
  font-size:13px;
}

/* ═══════════════════════════════════════════════════════════════
   SCALE VISUAL (CSS orrery)
   ═══════════════════════════════════════════════════════════════ */
.scale-visual {
  height:440px; display:grid; place-items:center; position:relative;
}
.orbit-ring {
  position:absolute; border:1px solid rgba(0,229,255,.10);
  border-radius:50%; animation:orbitSpin linear infinite;
}
.orbit-ring:nth-child(1){width:100px;height:100px;animation-duration:20s}
.orbit-ring:nth-child(2){width:180px;height:180px;animation-duration:32s}
.orbit-ring:nth-child(3){width:280px;height:280px;animation-duration:48s}
.orbit-ring:nth-child(4){width:380px;height:380px;animation-duration:68s}
@keyframes orbitSpin { to{transform:rotate(360deg)} }

.body {
  position:absolute; border-radius:50%;
  box-shadow:0 0 30px currentColor;
}
.sun-css {
  width:72px; height:72px; color:#ffb347;
  background:radial-gradient(circle at 32% 32%,#fff8d4,#ffb347 40%,#ff5b2d 75%);
  box-shadow:0 0 40px rgba(255,179,71,.6),0 0 80px rgba(255,120,40,.3);
}
.earth-css {
  width:28px; height:28px; color:#4db8ff;
  background:radial-gradient(circle at 32% 28%,#d7ffff,#1a8ef1 45%,#0d3979);
  transform:translate(130px,-35px);
}
.moon-css {
  width:8px; height:8px; color:#d0d8e8;
  background:#d0d8e8;
  transform:translate(160px,-46px);
}

/* ═══════════════════════════════════════════════════════════════
   SOLAR SYSTEM SHELL
   ═══════════════════════════════════════════════════════════════ */
.solar-shell {
  height:min(78vh,740px); min-height:580px;
  border-radius:24px;
  border:1px solid rgba(0,229,255,.12);
  background:rgba(0,2,12,.40);
  box-shadow:inset 0 0 100px rgba(0,229,255,.03),0 40px 120px rgba(0,0,0,.50);
  overflow:hidden; position:relative;
}
.solar-toolbar {
  position:absolute; left:20px; top:20px; z-index:4;
  display:flex; gap:10px; flex-wrap:wrap;
}
.chip {
  border:1px solid rgba(0,229,255,.18);
  border-radius:40px;
  padding:8px 14px;
  color:rgba(200,220,255,.65);
  background:rgba(4,12,30,.55);
  font:700 9px/1 'Orbitron',sans-serif;
  letter-spacing:1.2px;
  backdrop-filter:blur(16px);
}
.planet-panel {
  position:absolute; right:22px; bottom:22px; z-index:5;
  width:min(380px,calc(100% - 44px));
  padding:26px;
}
.planet-panel h3 {
  margin:0 0 16px;
  font:800 30px/1 'Orbitron',sans-serif;
  text-shadow:0 0 20px rgba(0,229,255,.3);
}
.planet-panel dl {
  display:grid; grid-template-columns:1fr 1fr; gap:12px 16px; margin:0;
}
.planet-panel dt {
  color:rgba(200,220,255,.45);
  font-size:10px; text-transform:uppercase; letter-spacing:1.5px;
}
.planet-panel dd { margin:4px 0 0; color:var(--white); font-weight:700; }
.planet-panel p { margin:18px 0 0; color:var(--muted); line-height:1.6; }
#solarCanvas { width:100%; height:100%; display:block; }

/* ═══════════════════════════════════════════════════════════════
   BLACK HOLE (CSS)
   ═══════════════════════════════════════════════════════════════ */
.blackhole-wrap { text-align:center; }
.black-hole {
  width:min(560px,82vw); aspect-ratio:1;
  margin:0 auto 50px;
  border-radius:50%; position:relative;
  background:radial-gradient(circle,#000 0 28%,rgba(0,0,0,.97) 32%,transparent 33%);
}
.black-hole::before {
  content:"";
  position:absolute; inset:20%;
  border-radius:50%;
  background:#000;
  box-shadow:0 0 0 20px rgba(0,0,0,.70),0 0 80px rgba(0,0,0,1);
  z-index:2;
}
.black-hole::after {
  content:"";
  position:absolute; inset:14% -10%;
  border-radius:50%;
  background:
    conic-gradient(from 25deg,
      rgba(255,80,40,0),#ff6b35,#ffd080,#e8f4ff,#4ad4ff,#6040ff,
      rgba(255,80,40,.9),rgba(255,80,40,0));
  transform:rotateX(70deg);
  filter:blur(3px);
  box-shadow:0 0 60px rgba(255,140,50,.50),0 0 120px rgba(0,229,255,.15);
  animation:diskSpin 6s linear infinite;
}
.black-hole .lens {
  position:absolute; inset:-10%;
  border-radius:50%;
  background:radial-gradient(circle,transparent 40%,rgba(0,229,255,.06) 43%,rgba(255,179,71,.15) 48%,transparent 56%);
  animation:lensPulse 5s ease-in-out infinite alternate;
}
@keyframes diskSpin { to{transform:rotateX(70deg) rotateZ(360deg)} }
@keyframes lensPulse { 0%{transform:scale(1);opacity:1} 100%{transform:scale(1.06);opacity:.65} }

/* ═══════════════════════════════════════════════════════════════
   DEEP SPACE CARDS
   ═══════════════════════════════════════════════════════════════ */
.deep-card {
  min-height:260px; padding:28px;
  display:flex; flex-direction:column; justify-content:flex-end;
  transition:transform .35s,box-shadow .35s;
}
.deep-card:hover {
  transform:translateY(-6px);
  box-shadow:0 0 60px rgba(0,229,255,.08),0 30px 100px rgba(0,0,0,.4);
}
.deep-card h3 { margin:0 0 12px; font:800 22px/1.1 'Orbitron',sans-serif; }
.deep-card p { margin:0; color:var(--muted); line-height:1.6; }
.nebula-card {
  background:
    radial-gradient(circle at 30% 22%,rgba(255,45,170,.30),transparent 38%),
    linear-gradient(160deg,rgba(8,18,44,.65),rgba(14,8,36,.45));
}
.supernova-card {
  background:
    radial-gradient(circle at 60% 30%,rgba(255,179,71,.35),transparent 30%),
    linear-gradient(160deg,rgba(8,18,44,.65),rgba(14,8,36,.45));
}
.cluster-card {
  background:
    radial-gradient(circle at 45% 28%,rgba(0,229,255,.28),transparent 40%),
    linear-gradient(160deg,rgba(8,18,44,.65),rgba(14,8,36,.45));
}

/* ═══════════════════════════════════════════════════════════════
   EXPLORER
   ═══════════════════════════════════════════════════════════════ */
.explorer-layout {
  display:grid; grid-template-columns:minmax(260px,400px) 1fr; gap:24px; margin-top:40px;
}
.explorer-list { display:grid; gap:12px; }
.explorer-card {
  padding:22px; cursor:pointer;
  transition:all .3s cubic-bezier(.25,.8,.25,1);
}
.explorer-card:hover, .explorer-card.selected {
  transform:translateX(6px);
  border-color:rgba(0,229,255,.40);
  box-shadow:0 0 40px rgba(0,229,255,.10);
}
.explorer-card.selected {
  border-color:rgba(0,229,255,.50);
  background:linear-gradient(135deg,rgba(0,229,255,.06),rgba(168,85,247,.04));
}
.explorer-card h3 { margin:0 0 8px; font:800 18px/1.1 'Orbitron',sans-serif; }
.explorer-card p { margin:0; color:var(--muted); font-size:13px; line-height:1.5; }
.detail-panel { padding:34px; min-height:400px; }
.detail-panel h3 { margin:0 0 18px; font:900 clamp(28px,5vw,56px)/1 'Orbitron',sans-serif; }
.detail-panel p { color:var(--muted); font-size:17px; line-height:1.75; }
.detail-stats { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:28px; }
.detail-stats div {
  padding:16px; border-radius:16px;
  border:1px solid rgba(0,229,255,.10);
  background:rgba(255,255,255,.025);
}
.detail-stats span {
  display:block; color:rgba(200,220,255,.45);
  font-size:10px; text-transform:uppercase; letter-spacing:1.5px;
}
.detail-stats strong {
  display:block; margin-top:10px;
  font:800 20px/1 'Orbitron',sans-serif; color:var(--white);
}

/* ═══════════════════════════════════════════════════════════════
   DATA DASHBOARD
   ═══════════════════════════════════════════════════════════════ */
.data-card { padding:28px; min-height:200px; }
.data-card .data-label {
  color:rgba(200,220,255,.50);
  font:700 10px/1 'Orbitron',sans-serif;
  letter-spacing:2px;
}
.data-card .data-value {
  display:block; margin-top:28px;
  font:900 clamp(28px,4vw,48px)/1 'Orbitron',sans-serif;
  color:var(--white);
  text-shadow:0 0 30px rgba(0,229,255,.25);
}
.data-note {
  margin-top:30px; color:rgba(200,220,255,.55); line-height:1.7; font-size:14px;
}

/* ═══════════════════════════════════════════════════════════════
   FINAL SECTION
   ═══════════════════════════════════════════════════════════════ */
.tiny-earth {
  width:28px; height:28px; border-radius:50%;
  margin:0 auto 50px;
  background:radial-gradient(circle at 32% 28%,#d7ffff,#4db8ff 40%,#0d3979 70%);
  box-shadow:0 0 40px rgba(0,229,255,.8),0 0 200px rgba(0,229,255,.30);
  animation:earthFloat 6s ease-in-out infinite;
}
@keyframes earthFloat { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-14px)} }

/* ═══════════════════════════════════════════════════════════════
   REVEAL ANIMATIONS
   ═══════════════════════════════════════════════════════════════ */
.reveal {
  opacity:0;
  transform:translateY(40px) scale(.97);
  transition:opacity 1s cubic-bezier(.2,.8,.2,1),transform 1s cubic-bezier(.2,.8,.2,1);
}
.reveal.visible {
  opacity:1; transform:translateY(0) scale(1);
}
.reveal-delay-1 { transition-delay:.15s; }
.reveal-delay-2 { transition-delay:.30s; }
.reveal-delay-3 { transition-delay:.45s; }

/* ═══════════════════════════════════════════════════════════════
   RESPONSIVE
   ═══════════════════════════════════════════════════════════════ */
@media (max-width:960px) {
  .nav { top:10px; border-radius:20px; padding:8px; }
  .brand { display:none; }
  .nav-links { justify-content:center; width:100%; gap:0; }
  .nav a { padding:8px 8px; font-size:8px; }
  .two-col,.explorer-layout { grid-template-columns:1fr; }
  .grid-4,.grid-3 { grid-template-columns:repeat(2,1fr); }
  .section { padding:90px 18px; }
  .planet-panel { left:16px; right:16px; bottom:16px; width:auto; }
}
@media (max-width:580px) {
  .nav-links { gap:0; }
  .nav a { font-size:7px; padding:7px 6px; letter-spacing:.8px; }
  .grid-4,.grid-3,.detail-stats { grid-template-columns:1fr; }
  .solar-shell { min-height:640px; }
  .btn { width:100%; }
  .planet-panel dl { grid-template-columns:1fr; }
  h1 { letter-spacing:-1px; }
}

@media (prefers-reduced-motion:reduce) {
  *,*::before,*::after {
    animation-duration:.001ms !important;
    animation-iteration-count:1 !important;
    transition-duration:.001ms !important;
    scroll-behavior:auto !important;
  }
}
</style>
</head>
<body>

<!-- ═══════════════════════════════════════════════════════════
     BACKGROUND CANVAS & OVERLAYS
     ═══════════════════════════════════════════════════════════ -->
<canvas id="bg-canvas" aria-hidden="true"></canvas>
<div class="aurora-overlay"></div>
<div class="dust-overlay"></div>
<div class="vignette"></div>

<!-- ═══════════════════════════════════════════════════════════
     NAVIGATION
     ═══════════════════════════════════════════════════════════ -->
<nav class="nav" aria-label="Primary">
  <div class="brand">COSMOS<span class="brand-dot"></span></div>
  <div class="nav-links">
    <a href="#home">HOME</a>
    <a href="#cosmos">COSMOS</a>
    <a href="#solar">SOLAR</a>
    <a href="#galaxy">GALAXY</a>
    <a href="#blackhole">BLACK HOLE</a>
    <a href="#wormhole">WORMHOLE</a>
    <a href="#explorer">EXPLORER</a>
    <a href="#data">DATA</a>
  </div>
</nav>

<!-- ═══════════════════════════════════════════════════════════
     MAIN CONTENT
     ═══════════════════════════════════════════════════════════ -->
<main>

<!-- ─── SECTION 1: HERO ─── -->
<section id="home" class="section">
  <div class="content center reveal">
    <div class="kicker">Cinematic Digital Universe</div>
    <h1>EXPLORE<br>THE UNIVERSE</h1>
    <p class="lead">Journey beyond the boundaries of space, time, and imagination into a living digital cosmos.</p>
    <div class="actions">
      <button class="btn" onclick="smoothScroll('#cosmos')">BEGIN EXPLORATION</button>
      <button class="btn secondary" onclick="smoothScroll('#solar')">DISCOVER COSMOS</button>
    </div>
  </div>
  <div class="scroll-cue">SCROLL TO EXPLORE</div>
</section>

<!-- ─── SECTION 2: COSMIC SCALE ─── -->
<section id="cosmos" class="section tall">
  <div class="content">
    <div class="two-col">
      <div class="reveal">
        <div class="kicker">Cosmic Scale</div>
        <h2>From one blue world to the observable universe.</h2>
        <p class="lead" style="margin-left:0">A cinematic scale comparison of Earth, the Moon, our Sun, the planets, and the deep field beyond our solar neighborhood.</p>
      </div>
      <div class="scale-visual glass reveal reveal-delay-1" aria-hidden="true">
        <div class="orbit-ring"></div>
        <div class="orbit-ring"></div>
        <div class="orbit-ring"></div>
        <div class="orbit-ring"></div>
        <div class="body sun-css"></div>
        <div class="body earth-css"></div>
        <div class="body moon-css"></div>
      </div>
    </div>
    <div class="grid-4">
      <div class="metric glass reveal"><span class="label">KNOWN PLANETS</span><span class="value counter" data-value="8">0</span><small class="desc">Eight primary planets orbit our Sun.</small></div>
      <div class="metric glass reveal reveal-delay-1"><span class="label">MILKY WAY STARS</span><span class="value counter" data-value="100" data-suffix="+B">0</span><small class="desc">Estimated stellar population in our galaxy.</small></div>
      <div class="metric glass reveal reveal-delay-2"><span class="label">UNIVERSE AGE</span><span class="value counter" data-value="13.8" data-suffix="B YRS">0</span><small class="desc">Approximate age of the observable universe.</small></div>
      <div class="metric glass reveal reveal-delay-3"><span class="label">OBSERVABLE WIDTH</span><span class="value counter" data-value="93" data-suffix="B LY">0</span><small class="desc">Approximate diameter of the observable universe.</small></div>
    </div>
  </div>
</section>

<!-- ─── SECTION 3: SOLAR SYSTEM ─── -->
<section id="solar" class="section">
  <div class="content">
    <div class="center reveal">
      <div class="kicker">Interactive Orrery</div>
      <h2>SOLAR SYSTEM</h2>
      <p class="lead">Hover or click a planet to inspect its orbital profile. Drag to shift the camera perspective.</p>
    </div>
    <div class="solar-shell reveal reveal-delay-1">
      <canvas id="solarCanvas"></canvas>
      <div class="solar-toolbar">
        <span class="chip">WebGL Orbits</span>
        <span class="chip">Mouse Camera</span>
        <span class="chip">Planet Data</span>
      </div>
      <div class="planet-panel glass" id="planetPanel">
        <h3>Earth</h3>
        <dl>
          <div><dt>Diameter</dt><dd>12,742 km</dd></div>
          <div><dt>Distance</dt><dd>149.6M km</dd></div>
          <div><dt>Orbit</dt><dd>365.25 days</dd></div>
          <div><dt>Class</dt><dd>Terrestrial</dd></div>
        </dl>
        <p>The only known world with surface oceans and life.</p>
      </div>
    </div>
  </div>
</section>

<!-- ─── SECTION 4: GALAXY ─── -->
<section id="galaxy" class="section ultra">
  <div class="galaxy-title center reveal">
    <div class="kicker">Spiral Structure</div>
    <h2 class="massive">OUR GALAXY</h2>
    <div class="subline">~100,000 LIGHT-YEARS WIDE</div>
    <p class="lead">A rotating field of stellar particles forms spiral arms, bright clusters, and faint nebula regions across the Milky Way.</p>
  </div>
</section>

<!-- ─── SECTION 5: BLACK HOLE ─── -->
<section id="blackhole" class="section">
  <div class="blackhole-wrap reveal">
    <div class="black-hole"><div class="lens"></div></div>
    <div class="kicker">Singularity</div>
    <h2>BEYOND THE EVENT HORIZON</h2>
    <p class="lead">Where space and time lose their meaning.</p>
  </div>
</section>

<!-- ─── SECTION 6: WORMHOLE ─── -->
<section id="wormhole" class="section tall">
  <div class="center reveal">
    <div class="kicker">Time Warp Corridor</div>
    <h2>WORMHOLE TRANSIT</h2>
    <p class="lead">A luminous spacetime tunnel bends star trails into a cinematic time-warp corridor. Move the mouse to steer the tunnel perspective.</p>
    <div class="actions">
      <button class="btn" onclick="window.dispatchEvent(new CustomEvent('cosmos-boost'))">ENGAGE TIME WARP</button>
    </div>
  </div>
</section>

<!-- ─── SECTION 7: DEEP SPACE ─── -->
<section id="deep" class="section tall">
  <div class="content">
    <div class="center reveal">
      <div class="kicker">Deep Space</div>
      <h2>Nebulas, supernovas, clusters, and ancient light.</h2>
      <p class="lead">Layered cosmic clouds and distant structures move at different speeds to preserve the sense of massive depth.</p>
    </div>
    <div class="grid-3">
      <div class="deep-card glass nebula-card reveal">
        <h3>Emission Nebulas</h3>
        <p>Ionized gas creates luminous clouds across star-forming regions.</p>
      </div>
      <div class="deep-card glass supernova-card reveal reveal-delay-1">
        <h3>Supernova Remnants</h3>
        <p>Explosive shockwaves seed space with heavier elements.</p>
      </div>
      <div class="deep-card glass cluster-card reveal reveal-delay-2">
        <h3>Star Clusters</h3>
        <p>Thousands of stars move through space as gravitational families.</p>
      </div>
    </div>
  </div>
</section>

<!-- ─── SECTION 8: EXPLORER ─── -->
<section id="explorer" class="section">
  <div class="content">
    <div class="center reveal">
      <div class="kicker">Interactive Cosmos</div>
      <h2>EXPLORER CONSOLE</h2>
    </div>
    <div class="explorer-layout reveal reveal-delay-1">
      <div class="explorer-list">
        <div class="explorer-card glass selected" data-kind="galaxy"><h3>🌌 Galaxy Explorer</h3><p>Spiral arms, stellar halos, and ancient galactic cores.</p></div>
        <div class="explorer-card glass" data-kind="planet"><h3>🪐 Planet Explorer</h3><p>Atmospheres, surfaces, magnetospheres, and orbital periods.</p></div>
        <div class="explorer-card glass" data-kind="star"><h3>⭐ Star Explorer</h3><p>Fusion, luminosity classes, temperature, and stellar life cycles.</p></div>
        <div class="explorer-card glass" data-kind="comet"><h3>☄️ Comet Tracker</h3><p>Frozen bodies, tails, perihelion paths, and solar heating.</p></div>
        <div class="explorer-card glass" data-kind="blackhole"><h3>🕳️ Black Hole Explorer</h3><p>Accretion disks, gravity wells, event horizons, and jets.</p></div>
        <div class="explorer-card glass" data-kind="wormhole"><h3>🌀 Wormhole Explorer</h3><p>Curved spacetime, lensing tunnels, and time-warp flight paths.</p></div>
      </div>
      <div class="detail-panel glass" id="explorerDetail"></div>
    </div>
  </div>
</section>

<!-- ─── SECTION 9: DATA ─── -->
<section id="data" class="section">
  <div class="content">
    <div class="reveal">
      <div class="kicker">Cosmic Telemetry</div>
      <h2>LIVE COSMIC DATA</h2>
      <p class="lead" style="margin-left:0">This dashboard is animated client-side and structured so real astronomical APIs can be integrated later. The values below are demonstration telemetry, not live measurements.</p>
    </div>
    <div class="grid-4">
      <div class="data-card glass reveal"><span class="data-label">STAR COUNT</span><span class="data-value counter" data-value="1284921302">0</span></div>
      <div class="data-card glass reveal reveal-delay-1"><span class="data-label">COSMIC DISTANCE</span><span class="data-value counter" data-value="4.37" data-suffix=" LY">0</span></div>
      <div class="data-card glass reveal reveal-delay-2"><span class="data-label">TEMPERATURE</span><span class="data-value counter" data-value="5778" data-suffix=" K">0</span></div>
      <div class="data-card glass reveal reveal-delay-3"><span class="data-label">GALAXIES OBSERVED</span><span class="data-value counter" data-value="2000000000" data-suffix="+">0</span></div>
    </div>
    <p class="data-note">Future integrations can attach NASA, ESA, JPL, or observatory feeds without making Streamlit rerun for every animation frame.</p>
  </div>
</section>

<!-- ─── SECTION 10: FINAL ─── -->
<section id="final" class="section">
  <div class="center reveal">
    <div class="tiny-earth"></div>
    <h2>WE ARE HERE.</h2>
    <p class="lead" style="margin-top:16px">THE UNIVERSE IS WAITING.</p>
    <div class="actions">
      <button class="btn" onclick="smoothScroll('#home')">START AGAIN ↑</button>
    </div>
  </div>
</section>

</main>

<!-- ═══════════════════════════════════════════════════════════
     JAVASCRIPT — THREE.JS + ANIMATIONS
     ═══════════════════════════════════════════════════════════ -->
<script>
(() => {
"use strict";

/* ── UTILITIES ── */
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const mobile = window.matchMedia('(max-width: 700px)').matches;
const isMobile = mobile;
const R = mobile ? 1.3 : 1.7;

function smoothScroll(sel) {
  const el = document.querySelector(sel);
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}
window.smoothScroll = smoothScroll;

/* ── NAV ACTIVE STATE ── */
const sections = [...document.querySelectorAll('section[id]')];
const navLinks = [...document.querySelectorAll('.nav a')];
const activeObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    navLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id));
  });
}, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });
sections.forEach(s => activeObs.observe(s));

/* ── REVEAL ANIMATIONS ── */
const revealObs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

/* ── COUNTER ANIMATIONS ── */
function animateCounter(el) {
  if (el.dataset.done) return;
  el.dataset.done = '1';
  const target = Number(el.dataset.value || 0);
  const suffix = el.dataset.suffix || '';
  const decimals = String(el.dataset.value || '').includes('.') ? 2 : 0;
  const start = performance.now();
  const dur = 1800;
  const tick = now => {
    const p = Math.min(1, (now - start) / dur);
    const ease = 1 - Math.pow(1 - p, 4);
    const val = target * ease;
    el.textContent = val.toLocaleString(undefined, {
      maximumFractionDigits: decimals,
      minimumFractionDigits: decimals && p === 1 ? decimals : 0
    }) + suffix;
    if (p < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}
const counterObs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) animateCounter(e.target); });
}, { threshold: 0.40 });
document.querySelectorAll('.counter').forEach(el => counterObs.observe(el));

/* ── EXPLORER ── */
const explorerData = {
  galaxy: ['Galaxy Explorer','Survey spiral arms, luminous dust lanes, old stellar halos, and dense galactic cores. The Milky Way is modeled here as a slow rotating particle system.',[['Scale','100K LY'],['Motion','Rotation'],['Focus','Spiral arms']]],
  planet: ['Planet Explorer','Compare rocky and gas worlds by atmosphere, orbital period, radius, and solar distance. Select planets in the orrery above for specific details.',[['Worlds','8'],['Types','4'],['Focus','Habitability']]],
  star: ['Star Explorer','Inspect how color, mass, and temperature define stellar lifetimes, from quiet red dwarfs to short-lived blue giants.',[['Fuel','Fusion'],['Output','Light'],['Focus','Lifecycle']]],
  comet: ['Comet Tracker','Trace high-eccentricity paths around the Sun as volatile ice becomes a glowing coma and tail.',[['Path','Elliptic'],['Material','Ice/Rock'],['Focus','Perihelion']]],
  blackhole: ['Black Hole Explorer','Explore extreme gravity, accretion disks, relativistic jets, and the boundary where escape velocity exceeds light.',[['Boundary','Horizon'],['Disk','Accretion'],['Focus','Gravity']]],
  wormhole: ['Wormhole Explorer','A speculative spacetime bridge rendered as layered luminous rings, streaking particles, and mouse-reactive camera distortion.',[['Model','Speculative'],['Effect','Lensing'],['Focus','Time warp']]]
};
const detailEl = document.getElementById('explorerDetail');
function setExplorer(kind) {
  const d = explorerData[kind];
  detailEl.innerHTML = '<h3>'+d[0]+'</h3><p>'+d[1]+'</p><div class="detail-stats">'+d[2].map(x=>'<div><span>'+x[0]+'</span><strong>'+x[1]+'</strong></div>').join('')+'</div>';
}
document.querySelectorAll('.explorer-card').forEach(card => {
  card.addEventListener('click', () => {
    document.querySelectorAll('.explorer-card').forEach(c => c.classList.remove('selected'));
    card.classList.add('selected');
    setExplorer(card.dataset.kind);
  });
});
setExplorer('galaxy');

/* ═══════════════════════════════════════════════════════════════
   THREE.JS — BACKGROUND SCENE
   ═══════════════════════════════════════════════════════════════ */
if (!window.THREE) return;

const canvas = document.getElementById('bg-canvas');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, isMobile ? 1.3 : 1.75));
renderer.setClearColor(0x000008, 1);

const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x000008, 0.012);

const camera = new THREE.PerspectiveCamera(58, innerWidth / innerHeight, 0.1, 3000);
camera.position.set(0, 0, 80);

/* ── MOUSE TRACKING ── */
const mouse = new THREE.Vector2(0, 0);
const mouseTarget = new THREE.Vector2(0, 0);
window.addEventListener('pointermove', e => {
  mouseTarget.x = (e.clientX / innerWidth - .5) * 2;
  mouseTarget.y = (e.clientY / innerHeight - .5) * 2;
}, { passive: true });

function resize() {
  renderer.setSize(innerWidth, innerHeight, false);
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
}
window.addEventListener('resize', resize);
resize();

/* ── TEXTURE SYSTEM ── */
const loader = new THREE.TextureLoader();
loader.setCrossOrigin('anonymous');
const PLANET_URL = 'https://raw.githubusercontent.com/jeromeetienne/threex.planets/master/images/';
const TJS_URL = 'https://threejs.org/examples/textures/planets/';
const texCache = new Map();

function loadTex(urls, onLoad) {
  const key = urls.join('|');
  if (texCache.has(key)) { const t = texCache.get(key); if (t && onLoad) onLoad(t); return; }
  let i = 0;
  const try_ = () => {
    loader.load(urls[i], tex => {
      tex.colorSpace = THREE.SRGBColorSpace;
      texCache.set(key, tex);
      if (onLoad) onLoad(tex);
    }, undefined, () => { i++; if (i < urls.length) try_(); });
  };
  try_();
}

const texUrls = {
  sun: [PLANET_URL+'sunmap.jpg'],
  mercury: [PLANET_URL+'mercurymap.jpg'],
  venus: [PLANET_URL+'venusmap.jpg'],
  earth: [PLANET_URL+'earthmap1k.jpg', TJS_URL+'earth_atmos_2048.jpg'],
  clouds: [PLANET_URL+'earthcloudmap.jpg', TJS_URL+'earth_clouds_1024.png'],
  moon: [PLANET_URL+'moonmap1k.jpg', TJS_URL+'moon_1024.jpg'],
  mars: [PLANET_URL+'marsmap1k.jpg'],
  jupiter: [PLANET_URL+'jupitermap.jpg'],
  saturn: [PLANET_URL+'saturnmap.jpg'],
  saturnRing: [PLANET_URL+'saturnringcolor.jpg'],
  uranus: [PLANET_URL+'uranusmap.jpg'],
  neptune: [PLANET_URL+'neptunemap.jpg']
};

/* ── STAR GENERATOR ── */
function makeStars(count, radius, size, cA, cB) {
  const pos = new Float32Array(count * 3);
  const col = new Float32Array(count * 3);
  const a = new THREE.Color(cA), b = new THREE.Color(cB);
  for (let i = 0; i < count; i++) {
    const r = radius * Math.cbrt(Math.random());
    const th = Math.random() * Math.PI * 2;
    const ph = Math.acos(2 * Math.random() - 1);
    pos[i*3]   = r * Math.sin(ph) * Math.cos(th);
    pos[i*3+1] = r * Math.sin(ph) * Math.sin(th);
    pos[i*3+2] = r * Math.cos(ph);
    const c = a.clone().lerp(b, Math.random());
    const boost = .55 + Math.random() * .9;
    col[i*3] = c.r * boost; col[i*3+1] = c.g * boost; col[i*3+2] = c.b * boost;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
  return new THREE.Points(geo, new THREE.PointsMaterial({
    size, vertexColors: true, transparent: true, opacity: .88,
    depthWrite: false, blending: THREE.AdditiveBlending
  }));
}

/* ── STAR FIELDS ── */
const starNear = makeStars(isMobile ? 2800 : 7000, 480, isMobile ? .44 : .30, '#dff8ff', '#8880ff');
const starMid = makeStars(isMobile ? 2000 : 5000, 700, isMobile ? .52 : .38, '#ffffff', '#60d0ff');
const starFar = makeStars(isMobile ? 3600 : 10000, 1000, isMobile ? .60 : .46, '#ffffff', '#40c0ff');
scene.add(starNear, starMid, starFar);

/* ── NEBULA CLOUDS ── */
const nebulaGroup = new THREE.Group();
const nebulaCount = isMobile ? 18 : 36;
const nebulaPalettes = [
  [new THREE.Color('#00e5ff'), new THREE.Color('#ff2daa')],
  [new THREE.Color('#a855f7'), new THREE.Color('#00e5ff')],
  [new THREE.Color('#ffb347'), new THREE.Color('#ff2daa')]
];
for (let i = 0; i < nebulaCount; i++) {
  const c = document.createElement('canvas');
  c.width = c.height = 128;
  const ctx = c.getContext('2d');
  const g = ctx.createRadialGradient(64,64,0,64,64,64);
  const pal = nebulaPalettes[i % 3];
  g.addColorStop(0, `rgba(${Math.round(pal[0].r*255)},${Math.round(pal[0].g*255)},${Math.round(pal[0].b*255)},.70)`);
  g.addColorStop(.35, `rgba(${Math.round(pal[1].r*255)},${Math.round(pal[1].g*255)},${Math.round(pal[1].b*255)},.22)`);
  g.addColorStop(1, 'rgba(0,0,0,0)');
  ctx.fillStyle = g; ctx.fillRect(0,0,128,128);
  const map = new THREE.CanvasTexture(c);
  const mat = new THREE.SpriteMaterial({ map, transparent: true, opacity: .10 + Math.random() * .14, blending: THREE.AdditiveBlending, depthWrite: false });
  const sprite = new THREE.Sprite(mat);
  sprite.position.set((Math.random()-.5)*460, (Math.random()-.5)*300, -140 - Math.random()*460);
  const s = 44 + Math.random() * 140;
  sprite.scale.set(s, s, 1);
  nebulaGroup.add(sprite);
}
scene.add(nebulaGroup);

/* ── HERO PLANET (Earth) ── */
const heroGroup = new THREE.Group();
const heroEarth = new THREE.Mesh(
  new THREE.SphereGeometry(16, 64, 64),
  new THREE.MeshStandardMaterial({ color: 0x2080e0, roughness: .70, metalness: .02, emissive: 0x061230, emissiveIntensity: .25 })
);
loadTex(texUrls.earth, map => { heroEarth.material.map = map; heroEarth.material.color.set(0xffffff); heroEarth.material.needsUpdate = true; });
loadTex([TJS_URL+'earth_specular_2048.jpg'], map => { heroEarth.material.roughnessMap = map; heroEarth.material.needsUpdate = true; });
heroGroup.add(heroEarth);

const heroClouds = new THREE.Mesh(
  new THREE.SphereGeometry(16.18, 64, 64),
  new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: .25, blending: THREE.AdditiveBlending })
);
loadTex(texUrls.clouds, map => { heroClouds.material.map = map; heroClouds.material.needsUpdate = true; });
heroGroup.add(heroClouds);

const heroAtmo = new THREE.Mesh(
  new THREE.SphereGeometry(16.45, 64, 64),
  new THREE.MeshBasicMaterial({ color: 0x40c8ff, transparent: true, opacity: .12, blending: THREE.AdditiveBlending })
);
heroGroup.add(heroAtmo);

heroGroup.position.set(0, -2, -10);
scene.add(heroGroup);

/* ── LIGHTING ── */
const sunLight = new THREE.PointLight(0x8defff, 2.8, 500);
sunLight.position.set(50, 35, 50);
scene.add(sunLight);
scene.add(new THREE.AmbientLight(0x3050a0, .80));

/* ── SPIRAL GALAXY ── */
function makeGalaxyGeo(count) {
  const pos = new Float32Array(count * 3);
  const col = new Float32Array(count * 3);
  const coreC = new THREE.Color('#fff8e0');
  const armC = new THREE.Color('#00e5ff');
  const pinkC = new THREE.Color('#ff2daa');
  for (let i = 0; i < count; i++) {
    const branch = i % 5;
    const r = Math.pow(Math.random(), .52) * 95;
    const spin = r * .058;
    const angle = branch / 5 * Math.PI * 2 + spin + (Math.random()-.5) * .52;
    const rnd = Math.pow(Math.random(), 2.6) * (Math.random() < .5 ? -1 : 1);
    pos[i*3]   = Math.cos(angle) * r + rnd * 10;
    pos[i*3+1] = (Math.random()-.5) * 5.5 * (1 - r/110);
    pos[i*3+2] = Math.sin(angle) * r + rnd * 10;
    const mixed = coreC.clone().lerp(i % 3 ? armC : pinkC, Math.min(1, r/95));
    col[i*3] = mixed.r; col[i*3+1] = mixed.g; col[i*3+2] = mixed.b;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
  return geo;
}

const galaxy = new THREE.Points(
  makeGalaxyGeo(isMobile ? 5500 : 13000),
  new THREE.PointsMaterial({ size: isMobile ? .36 : .22, vertexColors: true, transparent: true, opacity: .84, depthWrite: false, blending: THREE.AdditiveBlending })
);
galaxy.position.set(0, 0, -240);
galaxy.scale.setScalar(.08);
scene.add(galaxy);

/* ── WORMHOLE ── */
function makeWormhole() {
  const g = new THREE.Group();
  const matA = new THREE.MeshBasicMaterial({ color: 0x00e5ff, transparent: true, opacity: .20, blending: THREE.AdditiveBlending, side: THREE.DoubleSide });
  const matB = new THREE.MeshBasicMaterial({ color: 0xff2daa, transparent: true, opacity: .16, blending: THREE.AdditiveBlending, side: THREE.DoubleSide });
  for (let i = 0; i < 42; i++) {
    const rad = 10 + Math.sin(i*.62)*3 + i*.18;
    const tube = .032 + i*.0012;
    const ring = new THREE.Mesh(new THREE.TorusGeometry(rad, tube, 8, 144), i % 2 ? matA.clone() : matB.clone());
    ring.position.z = -i * 6.5;
    ring.rotation.z = i * .21;
    g.add(ring);
  }
  const cnt = isMobile ? 1000 : 1900;
  const pos = new Float32Array(cnt * 3);
  const col = new Float32Array(cnt * 3);
  const cCyan = new THREE.Color('#00e5ff'), cPink = new THREE.Color('#ff2daa');
  for (let i = 0; i < cnt; i++) {
    const z = -Math.random() * 300;
    const a = Math.random() * Math.PI * 2;
    const r = 3 + Math.random() * 20;
    pos[i*3] = Math.cos(a) * r;
    pos[i*3+1] = Math.sin(a) * r;
    pos[i*3+2] = z;
    const m = cCyan.clone().lerp(cPink, Math.random());
    col[i*3] = m.r; col[i*3+1] = m.g; col[i*3+2] = m.b;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
  const streaks = new THREE.Points(geo, new THREE.PointsMaterial({ size: .44, vertexColors: true, transparent: true, opacity: .84, depthWrite: false, blending: THREE.AdditiveBlending }));
  streaks.userData.pos = pos;
  g.add(streaks);
  g.position.set(0, 0, 28);
  g.userData.streaks = streaks;
  return g;
}
const wormhole = makeWormhole();
wormhole.visible = false;
scene.add(wormhole);

/* ── COMETS (background) ── */
const comets = [];
for (let i = 0; i < 6; i++) {
  const geo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0,0,0), new THREE.Vector3(-12 - Math.random()*18, .8, 0)]);
  const mat = new THREE.LineBasicMaterial({ color: i % 2 ? 0x00e5ff : 0xfff4d0, transparent: true, opacity: .50, blending: THREE.AdditiveBlending });
  const line = new THREE.Line(geo, mat);
  line.position.set(-260 - i*100, 100 + Math.random()*200, -140 - Math.random()*400);
  line.userData.speed = .44 + Math.random() * .52;
  scene.add(line);
  comets.push(line);
}

/* ── SECTION SCROLL PROGRESS ── */
function secProgress(id) {
  const el = document.getElementById(id);
  if (!el) return 0;
  const r = el.getBoundingClientRect();
  return 1 - Math.min(1, Math.max(0, r.top / innerHeight));
}

/* ── SHOOTING STARS (occasional) ── */
const shootingStars = [];
function spawnShootingStar() {
  if (shootingStars.length > 3) return;
  const geo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0,0,0), new THREE.Vector3(30, -20, 0)]);
  const mat = new THREE.LineBasicMaterial({ color: 0xffffff, transparent: true, opacity: .9, blending: THREE.AdditiveBlending });
  const star = new THREE.Line(geo, mat);
  star.position.set((Math.random()-.5)*600, 200 + Math.random()*200, -200 - Math.random()*300);
  star.userData.life = 0;
  star.userData.maxLife = 60 + Math.random() * 40;
  scene.add(star);
  shootingStars.push(star);
}
let shootTimer = 0;

/* ═══════════════════════════════════════════════════════════════
   MAIN ANIMATION LOOP
   ═══════════════════════════════════════════════════════════════ */
let lastTime = 0;
function animate(now) {
  if (reduced && now - lastTime < 100) { requestAnimationFrame(animate); return; }
  lastTime = now;
  const t = now * .001;
  const scroll = window.scrollY || document.documentElement.scrollTop;

  /* smooth mouse */
  mouse.x += (mouseTarget.x - mouse.x) * .04;
  mouse.y += (mouseTarget.y - mouse.y) * .04;

  const galaxyP = secProgress('galaxy');
  const blackP = secProgress('blackhole');
  const wormP = secProgress('wormhole');

  /* star fields */
  starNear.rotation.y = t * .020 + scroll * .00005;
  starNear.rotation.x = mouse.y * .032;
  starMid.rotation.y = -t * .012 + scroll * .00003;
  starFar.rotation.y = t * .006 + scroll * .00002;

  /* nebula parallax */
  nebulaGroup.rotation.z = t * .005;
  nebulaGroup.position.x = mouse.x * -8;
  nebulaGroup.position.y = mouse.y * 6;

  /* hero planet */
  heroGroup.rotation.y += .0030;
  heroGroup.rotation.x = mouse.y * .06;
  heroGroup.position.x = mouse.x * 3;
  heroClouds.rotation.y += .0040;
  const heroVisible = scroll < innerHeight * 2.5 || scroll > document.body.scrollHeight - innerHeight * 1.8;
  heroGroup.visible = heroVisible;
  heroGroup.scale.setScalar(scroll > document.body.scrollHeight - innerHeight * 1.8 ? .10 : 1);

  /* galaxy */
  galaxy.rotation.y = t * .038 + scroll * .00006;
  galaxy.rotation.z = .24 + t * .010;
  const gScale = .08 + Math.min(1.15, Math.max(0, galaxyP)) * 2.0;
  galaxy.scale.setScalar(gScale);
  galaxy.position.z = -280 + Math.min(1.15, Math.max(0, galaxyP)) * 200 - Math.max(0, blackP) * 140;

  /* wormhole */
  wormhole.visible = wormP > .06 && wormP < 1.75;
  if (wormhole.visible) {
    wormhole.rotation.z = t * .28 + mouse.x * .14;
    wormhole.rotation.x = mouse.y * .10;
    wormhole.position.x = mouse.x * -6;
    wormhole.position.y = mouse.y * 5;
    const wp = Math.min(1, Math.max(0, wormP));
    wormhole.scale.setScalar(.40 + wp * 1.45);
    wormhole.children.forEach((child, i) => {
      if (child.geometry && child.geometry.type === 'TorusGeometry') {
        child.rotation.z += .005 + i * .00004;
        child.material.opacity = .06 + Math.sin(t * 2.2 + i * .38) * .030 + wp * .16;
      }
    });
    const strk = wormhole.userData.streaks;
    const arr = strk.geometry.attributes.position.array;
    for (let i = 2; i < arr.length; i += 3) {
      arr[i] += .55 + wp * 2.0;
      if (arr[i] > 20) arr[i] = -300;
    }
    strk.geometry.attributes.position.needsUpdate = true;
  }

  /* comets */
  comets.forEach((c, i) => {
    c.position.x += c.userData.speed;
    c.position.y -= c.userData.speed * .20;
    if (c.position.x > 280) c.position.set(-300 - i*85, 90 + Math.random()*240, -140 - Math.random()*450);
  });

  /* shooting stars */
  shootTimer++;
  if (shootTimer > 300 && !isMobile) { spawnShootingStar(); shootTimer = 0; }
  for (let i = shootingStars.length - 1; i >= 0; i--) {
    const ss = shootingStars[i];
    ss.userData.life++;
    ss.position.x += 4; ss.position.y -= 2.5;
    ss.material.opacity = 1 - ss.userData.life / ss.userData.maxLife;
    if (ss.userData.life >= ss.userData.maxLife) {
      scene.remove(ss);
      shootingStars.splice(i, 1);
    }
  }

  /* camera */
  camera.position.x += (mouse.x * 6 - camera.position.x) * .032;
  camera.position.y += (-mouse.y * 5 - camera.position.y) * .032;
  camera.position.z = 80 + Math.sin(t * .12) * 2.5;
  camera.lookAt(0, 0, -80);

  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);

/* ── WORMHOLE BOOST EVENT ── */
window.addEventListener('cosmos-boost', () => {
  wormhole.children.forEach(child => {
    if (child.material) child.material.opacity = Math.min(.65, (child.material.opacity || .2) + .20);
  });
});

/* ═══════════════════════════════════════════════════════════════
   THREE.JS — SOLAR SYSTEM SCENE
   ═══════════════════════════════════════════════════════════════ */
function setupSolarSystem() {
  const cvs = document.getElementById('solarCanvas');
  if (!cvs) return;
  const box = cvs.parentElement;
  const r = new THREE.WebGLRenderer({ canvas: cvs, antialias: true, alpha: true, powerPreference: 'high-performance' });
  r.setPixelRatio(Math.min(devicePixelRatio || 1, isMobile ? 1.2 : 1.5));
  const s = new THREE.Scene();
  const c = new THREE.PerspectiveCamera(50, 1, .1, 1200);
  c.position.set(0, 92, 180);
  const ray = new THREE.Raycaster();
  const ptr = new THREE.Vector2(99, 99);
  const panel = document.getElementById('planetPanel');

  s.add(new THREE.AmbientLight(0x5080c0, .65));
  const light = new THREE.PointLight(0xffd890, 5.5, 600);
  light.position.set(0, 0, 0);
  s.add(light);

  /* sun */
  const sunM = new THREE.Mesh(
    new THREE.SphereGeometry(14, 56, 56),
    new THREE.MeshBasicMaterial({ color: 0xffb347 })
  );
  loadTex(texUrls.sun, map => { sunM.material.map = map; sunM.material.needsUpdate = true; });
  s.add(sunM);
  const sunGlow = new THREE.Mesh(new THREE.SphereGeometry(18, 56, 56), new THREE.MeshBasicMaterial({ color: 0xff8830, transparent: true, opacity: .20, blending: THREE.AdditiveBlending }));
  s.add(sunGlow);
  const sunCorona = new THREE.Mesh(new THREE.SphereGeometry(26, 56, 56), new THREE.MeshBasicMaterial({ color: 0xff6020, transparent: true, opacity: .08, blending: THREE.AdditiveBlending }));
  s.add(sunCorona);

  /* planet data: [name, radius, orbit, speed, color, diameter, dist, orbitDays, desc, texUrls] */
  const planetData = [
    ['Mercury', 4, 24, .044, 0xb8b0a4, '4,879 km', '57.9M km', '88 days', 'The smallest planet with extreme day-night temperature swings.', texUrls.mercury],
    ['Venus', 7, 34, .030, 0xe3b06f, '12,104 km', '108.2M km', '225 days', 'Dense atmosphere produces the hottest surface of any planet.', texUrls.venus],
    ['Earth', 7.5, 46, .024, 0x3b9dff, '12,742 km', '149.6M km', '365.25 days', 'The only known world with surface oceans and life.', texUrls.earth],
    ['Mars', 5.8, 58, .020, 0xd65b35, '6,779 km', '227.9M km', '687 days', 'Home to Olympus Mons, the largest volcano in the solar system.', texUrls.mars],
    ['Jupiter', 16, 80, .012, 0xd8ad82, '139,820 km', '778.5M km', '11.9 years', 'A gas giant with a storm larger than Earth.', texUrls.jupiter],
    ['Saturn', 14, 102, .009, 0xe8d09b, '116,460 km', '1.43B km', '29.5 years', 'Its ring system is made of countless icy particles.', texUrls.saturn],
    ['Uranus', 10, 124, .006, 0x8feaff, '50,724 km', '2.87B km', '84 years', 'This ice giant rotates on its side.', texUrls.uranus],
    ['Neptune', 10, 146, .005, 0x4f75ff, '49,244 km', '4.50B km', '164.8 years', 'Supersonic winds race through its deep blue atmosphere.', texUrls.neptune]
  ];

  const meshes = [];
  const labels = [];
  let earthM = null, moonM = null;

  /* orbit rings */
  planetData.forEach(p => {
    const geo = new THREE.RingGeometry(p[2] - .05, p[2] + .05, 180);
    const mat = new THREE.MeshBasicMaterial({ color: 0x50d8ff, transparent: true, opacity: .14, side: THREE.DoubleSide });
    const ring = new THREE.Mesh(geo, mat);
    ring.rotation.x = Math.PI / 2;
    s.add(ring);
  });

  /* asteroid belt */
  const astCount = isMobile ? 500 : 1400;
  const astPos = new Float32Array(astCount * 3);
  const astCol = new Float32Array(astCount * 3);
  const rA = new THREE.Color('#8a7a68'), rB = new THREE.Color('#c8b898');
  for (let i = 0; i < astCount; i++) {
    const a = Math.random() * Math.PI * 2;
    const rad = 64 + Math.random() * 10;
    astPos[i*3] = Math.cos(a) * rad;
    astPos[i*3+1] = (Math.random()-.5) * 3.8;
    astPos[i*3+2] = Math.sin(a) * rad;
    const c = rA.clone().lerp(rB, Math.random());
    astCol[i*3] = c.r; astCol[i*3+1] = c.g; astCol[i*3+2] = c.b;
  }
  const astGeo = new THREE.BufferGeometry();
  astGeo.setAttribute('position', new THREE.BufferAttribute(astPos, 3));
  astGeo.setAttribute('color', new THREE.BufferAttribute(astCol, 3));
  const astBelt = new THREE.Points(astGeo, new THREE.PointsMaterial({ size: .65, vertexColors: true, transparent: true, opacity: .78, depthWrite: false }));
  s.add(astBelt);

  /* planets */
  function makeLabel(text) {
    const cv = document.createElement('canvas');
    cv.width = 256; cv.height = 72;
    const ctx = cv.getContext('2d');
    ctx.font = '700 26px Orbitron, Arial';
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.shadowColor = 'rgba(0,229,255,.9)'; ctx.shadowBlur = 14;
    ctx.fillStyle = 'rgba(240,250,255,.90)';
    ctx.fillText(text, 128, 36);
    const map = new THREE.CanvasTexture(cv);
    const sprite = new THREE.Sprite(new THREE.SpriteMaterial({ map, transparent: true, opacity: .90, depthWrite: false }));
    sprite.scale.set(20, 5.5, 1);
    return sprite;
  }

  planetData.forEach(p => {
    const mat = new THREE.MeshStandardMaterial({ color: p[4], roughness: .72, emissive: p[4], emissiveIntensity: .025 });
    const mesh = new THREE.Mesh(new THREE.SphereGeometry(p[1], 40, 40), mat);
    mesh.userData.info = p;
    loadTex(p[9], map => { mesh.material.map = map; mesh.material.color.set(0xffffff); mesh.material.needsUpdate = true; });
    s.add(mesh);
    meshes.push(mesh);
    const lbl = makeLabel(p[0]);
    lbl.userData.host = mesh;
    s.add(lbl);
    labels.push(lbl);
    if (p[0] === 'Earth') {
      earthM = mesh;
      moonM = new THREE.Mesh(
        new THREE.SphereGeometry(2.2, 32, 32),
        new THREE.MeshStandardMaterial({ color: 0xd8d0c4, roughness: .84 })
      );
      loadTex(texUrls.moon, map => { moonM.material.map = map; moonM.material.color.set(0xffffff); moonM.material.needsUpdate = true; });
      moonM.userData.info = ['Moon', 2.2, 8, .065, 0xd8d0c4, '3,474 km', '384,400 km', '27.3 days', "Earth's natural satellite stabilizes our planet's axial tilt.", texUrls.moon];
      s.add(moonM);
      meshes.push(moonM);
    }
    if (p[0] === 'Saturn') {
      const ring = new THREE.Mesh(
        new THREE.RingGeometry(p[1] + 3.5, p[1] + 10, 110),
        new THREE.MeshBasicMaterial({ color: 0xf0d898, transparent: true, opacity: .42, side: THREE.DoubleSide })
      );
      ring.rotation.x = Math.PI / 2.3;
      loadTex(texUrls.saturnRing, map => { ring.material.map = map; ring.material.needsUpdate = true; });
      mesh.add(ring);
    }
  });

  /* solar comets */
  const sComets = [];
  for (let i = 0; i < 3; i++) {
    const comet = new THREE.Group();
    const nuc = new THREE.Mesh(new THREE.SphereGeometry(1.3, 18, 18), new THREE.MeshBasicMaterial({ color: 0xeaf8ff }));
    const tailGeo = new THREE.ConeGeometry(3, 32, 18, 1, true);
    const tail = new THREE.Mesh(tailGeo, new THREE.MeshBasicMaterial({ color: i % 2 ? 0x00e5ff : 0xfff0c0, transparent: true, opacity: .20, blending: THREE.AdditiveBlending, side: THREE.DoubleSide }));
    tail.rotation.z = Math.PI / 2; tail.position.x = -14;
    comet.add(nuc, tail);
    comet.userData.seed = i * 2.2;
    s.add(comet);
    sComets.push(comet);
  }

  /* panel update */
  function setPanel(info) {
    const cls = ['Mercury','Venus','Earth','Mars'].includes(info[0]) ? 'Terrestrial' : 'Giant';
    panel.innerHTML = '<h3>'+info[0]+'</h3><dl><div><dt>Diameter</dt><dd>'+info[5]+'</dd></div><div><dt>Distance</dt><dd>'+info[6]+'</dd></div><div><dt>Orbit</dt><dd>'+info[7]+'</dd></div><div><dt>Class</dt><dd>'+cls+'</dd></div></dl><p>'+info[8]+'</p>';
  }

  /* resize */
  function resizeS() {
    const rect = box.getBoundingClientRect();
    r.setSize(rect.width, rect.height, false);
    c.aspect = rect.width / rect.height;
    c.updateProjectionMatrix();
  }
  new ResizeObserver(resizeS).observe(box);
  resizeS();

  /* interactions */
  cvs.addEventListener('pointermove', ev => {
    const rect = cvs.getBoundingClientRect();
    ptr.x = ((ev.clientX - rect.left) / rect.width) * 2 - 1;
    ptr.y = -((ev.clientY - rect.top) / rect.height) * 2 + 1;
  }, { passive: true });
  cvs.addEventListener('click', () => {
    ray.setFromCamera(ptr, c);
    const hit = ray.intersectObjects(meshes, true).find(h => h.object.userData.info);
    if (hit) setPanel(hit.object.userData.info);
  });

  /* solar loop */
  function solarLoop(now) {
    const t = now * .001;
    sunM.scale.setScalar(1 + Math.sin(t * 3) * .022);
    sunGlow.scale.setScalar(1 + Math.sin(t * 2.2) * .07);
    sunCorona.scale.setScalar(1 + Math.sin(t * 1.5) * .12);
    astBelt.rotation.y += .0006;

    meshes.forEach((mesh, i) => {
      const p = mesh.userData.info;
      if (p[0] === 'Moon') return;
      const a = t * p[3] * 16 + i;
      mesh.position.set(Math.cos(a) * p[2], 0, Math.sin(a) * p[2]);
      mesh.rotation.y += .012 + i * .001;
    });
    if (earthM && moonM) {
      const a = t * 2;
      moonM.position.set(earthM.position.x + Math.cos(a) * 12, earthM.position.y + Math.sin(a * .35) * 1.3, earthM.position.z + Math.sin(a) * 12);
      moonM.rotation.y += .014;
    }
    labels.forEach(lbl => {
      const h = lbl.userData.host;
      lbl.position.set(h.position.x, h.position.y + h.geometry.parameters.radius + 7, h.position.z);
      lbl.quaternion.copy(c.quaternion);
    });
    sComets.forEach((comet, i) => {
      const a = t * (.22 + i * .04) + comet.userData.seed;
      const rx = 130 + i * 20;
      const rz = 45 + i * 14;
      comet.position.set(Math.cos(a) * rx, 8 + Math.sin(a * 2) * 12, Math.sin(a) * rz);
      comet.rotation.y = -a;
    });

    ray.setFromCamera(ptr, c);
    const hit = ray.intersectObjects(meshes, true).find(h => h.object.userData.info);
    meshes.forEach(m => m.scale.setScalar(hit && hit.object === m ? 1.28 : 1));
    if (hit) setPanel(hit.object.userData.info);

    c.position.x += (ptr.x * 24 - c.position.x) * .022;
    c.position.y += (92 + ptr.y * 14 - c.position.y) * .022;
    c.lookAt(0, 0, 0);
    r.render(s, c);
    requestAnimationFrame(solarLoop);
  }
  requestAnimationFrame(solarLoop);
}

setupSolarSystem();

})();
</script>
</body>
</html>
"""

components.html(COSMOS_HTML, height=920, scrolling=True)
