import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# STREAMLIT CONFIG
# ============================================================

st.set_page_config(
    page_title="Explore the Universe — Cinematic Cosmos",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu,
        header,
        footer {
            visibility: hidden;
        }

        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="collapsedControl"],
        [data-testid="stDeployButton"] {
            display: none !important;
        }

        .stApp {
            background: #000008;
            overflow-x: hidden;
        }

        .block-container {
            padding: 0 !important;
            max-width: none !important;
        }

        iframe {
            display: block;
            border: 0 !important;
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# COMPLETE CINEMATIC COSMOS WEBSITE
# ============================================================

COSMOS_HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>Cinematic Cosmos</title>

<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>

<style>

/* ============================================================
   ROOT
   ============================================================ */

:root {
    --bg: #000008;

    --cyan: #00e5ff;
    --blue: #4a90ff;
    --pink: #ff2daa;
    --purple: #a855f7;
    --amber: #ffb347;

    --white: #f3f7ff;
    --muted: rgba(205,220,255,.62);

    --glass:
        linear-gradient(
            145deg,
            rgba(8,18,45,.68),
            rgba(12,7,34,.48)
        );

    --border: rgba(100,210,255,.14);
}


/* ============================================================
   RESET
   ============================================================ */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    overflow-x: hidden;
}

body {
    min-height: 100vh;
    background: #000008;
    color: var(--white);

    font-family:
        Inter,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
}

a {
    color: inherit;
    text-decoration: none;
}

button {
    font-family: inherit;
}


/* ============================================================
   BACKGROUND
   ============================================================ */

#bg-canvas {
    position: fixed;
    inset: 0;

    width: 100%;
    height: 100vh;

    z-index: 0;

    background:
        radial-gradient(
            ellipse at 20% 20%,
            rgba(50,0,100,.28),
            transparent 50%
        ),
        radial-gradient(
            ellipse at 80% 80%,
            rgba(0,70,150,.20),
            transparent 50%
        ),
        #000008;
}

.aurora {
    position: fixed;
    inset: -20%;

    z-index: 1;
    pointer-events: none;

    background:
        radial-gradient(
            ellipse at 15% 30%,
            rgba(0,229,255,.13),
            transparent 40%
        ),
        radial-gradient(
            ellipse at 85% 25%,
            rgba(255,45,170,.10),
            transparent 42%
        ),
        radial-gradient(
            ellipse at 50% 80%,
            rgba(168,85,247,.10),
            transparent 48%
        );

    filter: blur(50px);

    animation:
        auroraMove 35s ease-in-out infinite alternate;
}

.dust {
    position: fixed;
    inset: 0;

    z-index: 1;
    pointer-events: none;

    opacity: .20;

    background-image:
        radial-gradient(
            circle,
            rgba(255,255,255,.35) 0 1px,
            transparent 1.5px
        ),
        radial-gradient(
            circle,
            rgba(0,229,255,.25) 0 .7px,
            transparent 1.2px
        );

    background-size:
        150px 150px,
        220px 220px;

    animation:
        dustMove 100s linear infinite;
}

.vignette {
    position: fixed;
    inset: 0;

    z-index: 1;
    pointer-events: none;

    background:
        radial-gradient(
            ellipse at center,
            transparent 38%,
            rgba(0,0,0,.72) 100%
        );
}

@keyframes auroraMove {

    from {
        transform:
            translate3d(-2%,-1%,0)
            scale(1.02)
            rotate(-1deg);
    }

    to {
        transform:
            translate3d(2%,1%,0)
            scale(1.08)
            rotate(1deg);
    }
}

@keyframes dustMove {

    to {
        background-position:
            700px 900px,
            -600px 500px;
    }
}


/* ============================================================
   MAIN
   ============================================================ */

main {
    position: relative;
    z-index: 2;
}


/* ============================================================
   NAVIGATION
   ============================================================ */

.nav {
    position: fixed;

    top: 18px;
    left: 50%;

    transform: translateX(-50%);

    width: min(
        1150px,
        calc(100vw - 32px)
    );

    z-index: 100;

    display: flex;
    align-items: center;
    justify-content: space-between;

    gap: 20px;

    padding: 12px 16px 12px 24px;

    border:
        1px solid
        rgba(0,229,255,.16);

    border-radius: 60px;

    background:
        linear-gradient(
            135deg,
            rgba(4,10,30,.76),
            rgba(12,5,35,.58)
        );

    backdrop-filter:
        blur(25px)
        saturate(1.4);

    box-shadow:
        0 20px 80px rgba(0,0,0,.55),
        inset 0 1px rgba(255,255,255,.05),
        0 0 50px rgba(0,229,255,.04);
}

.brand {
    font-family: Orbitron, sans-serif;

    font-size: 12px;
    font-weight: 900;

    letter-spacing: 4px;

    white-space: nowrap;

    text-shadow:
        0 0 20px
        rgba(0,229,255,.55);
}

.brand-dot {
    display: inline-block;

    width: 7px;
    height: 7px;

    margin-left: 7px;

    border-radius: 50%;

    background: var(--cyan);

    box-shadow:
        0 0 10px var(--cyan),
        0 0 25px rgba(0,229,255,.45);

    animation:
        pulse 2s ease-in-out infinite;
}

.nav-links {
    display: flex;
    align-items: center;

    gap: 2px;

    flex-wrap: wrap;
    justify-content: flex-end;
}

.nav-links a {
    position: relative;

    padding: 10px 11px;

    border-radius: 30px;

    color:
        rgba(205,220,255,.55);

    font-family: Orbitron, sans-serif;

    font-size: 9px;
    font-weight: 700;

    letter-spacing: 1.1px;

    transition:
        .3s ease;
}

.nav-links a:hover,
.nav-links a.active {
    color: white;

    background:
        rgba(0,229,255,.08);

    text-shadow:
        0 0 18px
        rgba(0,229,255,.7);
}

.nav-links a.active::after {
    content: "";

    position: absolute;

    left: 50%;
    bottom: 4px;

    transform:
        translateX(-50%);

    width: 13px;
    height: 2px;

    border-radius: 5px;

    background:
        var(--cyan);

    box-shadow:
        0 0 10px
        var(--cyan);
}

@keyframes pulse {

    0%,100% {
        transform: scale(1);
        opacity: 1;
    }

    50% {
        transform: scale(.75);
        opacity: .6;
    }
}


/* ============================================================
   SECTIONS
   ============================================================ */

.section {
    position: relative;

    min-height: 100vh;

    display: grid;
    place-items: center;

    padding:
        110px
        max(22px,6vw);
}

.section.tall {
    min-height: 120vh;
}

.section.hero {
    min-height: 100vh;
}

.content {
    width: min(
        1200px,
        100%
    );

    margin: auto;
}

.center {
    text-align: center;
}


/* ============================================================
   TYPOGRAPHY
   ============================================================ */

.kicker {
    display: inline-flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 20px;

    color: var(--cyan);

    font-family: Orbitron, sans-serif;

    font-size: 10px;
    font-weight: 700;

    letter-spacing: 4px;

    text-transform: uppercase;

    text-shadow:
        0 0 20px
        rgba(0,229,255,.6);
}

.kicker::before,
.kicker::after {
    content: "";

    width: 50px;
    height: 1px;
}

.kicker::before {
    background:
        linear-gradient(
            90deg,
            transparent,
            var(--cyan)
        );
}

.kicker::after {
    background:
        linear-gradient(
            90deg,
            var(--pink),
            transparent
        );
}

h1,
h2,
h3 {
    font-family: Orbitron, sans-serif;
}

h1 {
    font-size:
        clamp(
            50px,
            9vw,
            135px
        );

    line-height: .88;

    font-weight: 900;

    letter-spacing: -3px;

    text-transform: uppercase;

    text-shadow:
        0 0 40px rgba(0,229,255,.20),
        0 0 100px rgba(168,85,247,.14);
}

h2 {
    font-size:
        clamp(
            36px,
            6vw,
            82px
        );

    line-height: .92;

    font-weight: 800;

    text-transform: uppercase;

    text-shadow:
        0 0 30px
        rgba(0,229,255,.16);
}

.massive {
    font-size:
        clamp(
            52px,
            10vw,
            150px
        );
}

.lead {
    width: min(
        700px,
        100%
    );

    margin:
        28px
        auto
        0;

    color: var(--muted);

    font-size:
        clamp(
            15px,
            2vw,
            20px
        );

    line-height: 1.8;

    font-weight: 300;
}

.subline {
    margin-top: 24px;

    color: var(--cyan);

    font-family: Orbitron, sans-serif;

    font-size:
        clamp(
            16px,
            3vw,
            30px
        );

    font-weight: 800;

    letter-spacing: 3px;

    text-shadow:
        0 0 20px
        rgba(0,229,255,.45);
}


/* ============================================================
   BUTTONS
   ============================================================ */

.actions {
    display: flex;

    justify-content: center;

    gap: 18px;

    flex-wrap: wrap;

    margin-top: 40px;
}

.btn {
    position: relative;

    min-width: 205px;

    padding:
        17px
        32px;

    cursor: pointer;

    border:
        1px solid
        rgba(0,229,255,.38);

    border-radius: 60px;

    color: white;

    background:
        linear-gradient(
            135deg,
            rgba(0,229,255,.12),
            rgba(168,85,247,.09)
        );

    font-family: Orbitron, sans-serif;

    font-size: 10px;
    font-weight: 800;

    letter-spacing: 2px;

    overflow: hidden;

    transition:
        .4s cubic-bezier(.2,.8,.2,1);

    box-shadow:
        0 0 35px
        rgba(0,229,255,.10);
}

.btn:hover {
    transform:
        translateY(-4px);

    border-color:
        rgba(0,229,255,.70);

    box-shadow:
        0 0 55px
        rgba(0,229,255,.25),
        0 15px 50px
        rgba(0,0,0,.35);
}

.btn.secondary {
    border-color:
        rgba(255,45,170,.32);

    background:
        rgba(10,5,30,.55);
}

.btn.secondary:hover {
    border-color:
        rgba(255,45,170,.65);

    box-shadow:
        0 0 55px
        rgba(255,45,170,.18);
}


/* ============================================================
   SCROLL INDICATOR
   ============================================================ */

.scroll-cue {
    position: absolute;

    left: 50%;
    bottom: 38px;

    transform:
        translateX(-50%);

    color:
        rgba(205,220,255,.48);

    font-family: Orbitron, sans-serif;

    font-size: 9px;
    font-weight: 700;

    letter-spacing: 3px;

    text-align: center;
}

.scroll-cue::after {
    content: "";

    display: block;

    width: 1px;
    height: 50px;

    margin:
        14px
        auto
        0;

    background:
        linear-gradient(
            to bottom,
            var(--cyan),
            transparent
        );

    animation:
        scrollPulse 2s ease-in-out infinite;
}

@keyframes scrollPulse {

    0%,100% {
        transform: scaleY(.3);
        opacity: .3;
    }

    50% {
        transform: scaleY(1);
        opacity: 1;
    }
}


/* ============================================================
   GLASS
   ============================================================ */

.glass {
    position: relative;

    overflow: hidden;

    border:
        1px solid
        var(--border);

    border-radius: 20px;

    background: var(--glass);

    backdrop-filter:
        blur(20px)
        saturate(1.25);

    box-shadow:
        0 30px 100px
        rgba(0,0,0,.36),
        inset 0 1px
        rgba(255,255,255,.05),
        0 0 60px
        rgba(0,229,255,.04);
}

.glass::before {
    content: "";

    position: absolute;

    inset: 0;

    pointer-events: none;

    background:
        linear-gradient(
            120deg,
            transparent,
            rgba(255,255,255,.055),
            transparent
        );

    transform:
        translateX(-150%);

    transition:
        .8s ease;
}

.glass:hover::before {
    transform:
        translateX(150%);
}


/* ============================================================
   GRID
   ============================================================ */

.two-col {
    display: grid;

    grid-template-columns:
        1fr
        1fr;

    gap: 45px;

    align-items: center;
}

.grid-4 {
    display: grid;

    grid-template-columns:
        repeat(4,1fr);

    gap: 18px;

    margin-top: 45px;
}

.grid-3 {
    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 18px;

    margin-top: 45px;
}


/* ============================================================
   COSMIC SCALE
   ============================================================ */

.scale-visual {
    position: relative;

    height: 440px;

    display: grid;

    place-items: center;
}

.orbit {
    position: absolute;

    border:
        1px solid
        rgba(0,229,255,.10);

    border-radius: 50%;

    animation:
        orbitSpin
        linear
        infinite;
}

.orbit:nth-child(1) {
    width: 100px;
    height: 100px;

    animation-duration: 20s;
}

.orbit:nth-child(2) {
    width: 180px;
    height: 180px;

    animation-duration: 32s;
}

.orbit:nth-child(3) {
    width: 280px;
    height: 280px;

    animation-duration: 45s;
}

.orbit:nth-child(4) {
    width: 380px;
    height: 380px;

    animation-duration: 65s;
}

@keyframes orbitSpin {
    to {
        transform:
            rotate(360deg);
    }
}

.sun-css {
    position: absolute;

    width: 72px;
    height: 72px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 30% 30%,
            #fff9d5,
            #ffb347 40%,
            #ff5428 80%
        );

    box-shadow:
        0 0 45px
        rgba(255,179,71,.75),
        0 0 100px
        rgba(255,100,30,.35);

    animation:
        sunPulse 3s ease-in-out infinite;
}

@keyframes sunPulse {

    0%,100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.06);
    }
}

.earth-css {
    position: absolute;

    width: 28px;
    height: 28px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 30% 25%,
            #d8ffff,
            #1c91f2 45%,
            #082d6d 80%
        );

    transform:
        translate(130px,-35px);

    box-shadow:
        0 0 20px
        rgba(50,170,255,.65);
}


/* ============================================================
   METRICS
   ============================================================ */

.metric {
    min-height: 165px;

    padding: 28px;
}

.metric-label {
    display: block;

    margin-bottom: 20px;

    color:
        rgba(205,220,255,.50);

    font-family: Orbitron, sans-serif;

    font-size: 9px;
    font-weight: 700;

    letter-spacing: 2px;
}

.metric-value {
    display: block;

    font-family: Orbitron, sans-serif;

    font-size:
        clamp(
            28px,
            4vw,
            46px
        );

    font-weight: 900;

    text-shadow:
        0 0 30px
        rgba(0,229,255,.30);
}

.metric-desc {
    display: block;

    margin-top: 14px;

    color: var(--muted);

    font-size: 12px;

    line-height: 1.6;
}


/* ============================================================
   SOLAR SYSTEM
   ============================================================ */

.solar-shell {
    position: relative;

    height:
        min(
            78vh,
            740px
        );

    min-height: 580px;

    margin-top: 45px;

    overflow: hidden;

    border:
        1px solid
        rgba(0,229,255,.12);

    border-radius: 25px;

    background:
        rgba(0,2,12,.42);

    box-shadow:
        inset 0 0 100px
        rgba(0,229,255,.03),
        0 40px 120px
        rgba(0,0,0,.50);
}

#solarCanvas {
    display: block;

    width: 100%;
    height: 100%;
}

.solar-toolbar {
    position: absolute;

    top: 20px;
    left: 20px;

    z-index: 5;

    display: flex;

    gap: 10px;

    flex-wrap: wrap;
}

.chip {
    padding:
        8px
        14px;

    border:
        1px solid
        rgba(0,229,255,.18);

    border-radius: 40px;

    background:
        rgba(4,12,30,.60);

    color:
        rgba(205,220,255,.65);

    font-family: Orbitron, sans-serif;

    font-size: 8px;
    font-weight: 700;

    letter-spacing: 1.2px;

    backdrop-filter:
        blur(15px);
}

.planet-panel {
    position: absolute;

    right: 22px;
    bottom: 22px;

    z-index: 5;

    width:
        min(
            380px,
            calc(100% - 44px)
        );

    padding: 26px;
}

.planet-panel h3 {
    margin-bottom: 18px;

    font-size: 30px;

    text-shadow:
        0 0 20px
        rgba(0,229,255,.3);
}

.planet-panel dl {
    display: grid;

    grid-template-columns:
        1fr
        1fr;

    gap: 14px;
}

.planet-panel dt {
    color:
        rgba(205,220,255,.45);

    font-size: 9px;

    text-transform: uppercase;

    letter-spacing: 1.5px;
}

.planet-panel dd {
    margin-top: 5px;

    color: white;

    font-weight: 700;
}

.planet-panel p {
    margin-top: 18px;

    color: var(--muted);

    line-height: 1.6;

    font-size: 13px;
}


/* ============================================================
   BLACK HOLE
   ============================================================ */

.blackhole-wrap {
    width: 100%;

    text-align: center;
}

.black-hole {
    position: relative;

    width:
        min(
            560px,
            82vw
        );

    aspect-ratio: 1;

    margin:
        0
        auto
        50px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            #000 0 25%,
            rgba(0,0,0,.98) 31%,
            transparent 32%
        );
}

.black-hole::before {
    content: "";

    position: absolute;

    inset: 16% -8%;

    border-radius: 50%;

    background:
        conic-gradient(
            from 20deg,
            transparent,
            #ff4c25,
            #ffd38b,
            #f4fbff,
            #42d8ff,
            #6847ff,
            #ff3c28,
            transparent
        );

    transform:
        rotateX(70deg);

    filter: blur(4px);

    box-shadow:
        0 0 60px
        rgba(255,130,40,.55),
        0 0 130px
        rgba(0,229,255,.15);

    animation:
        blackholeSpin
        6s
        linear
        infinite;
}

.black-hole::after {
    content: "";

    position: absolute;

    inset: 26%;

    border-radius: 50%;

    background: #000;

    box-shadow:
        0 0 50px
        #000,
        0 0 100px
        rgba(0,0,0,.9);
}

@keyframes blackholeSpin {

    to {
        transform:
            rotateX(70deg)
            rotateZ(360deg);
    }
}


/* ============================================================
   DEEP SPACE
   ============================================================ */

.deep-card {
    min-height: 270px;

    padding: 30px;

    display: flex;

    flex-direction: column;

    justify-content: flex-end;

    transition:
        .35s ease;
}

.deep-card:hover {
    transform:
        translateY(-8px);

    box-shadow:
        0 0 60px
        rgba(0,229,255,.10),
        0 30px 100px
        rgba(0,0,0,.45);
}

.deep-card h3 {
    margin-bottom: 12px;

    font-size: 21px;
}

.deep-card p {
    color: var(--muted);

    line-height: 1.65;
}

.nebula {
    background:
        radial-gradient(
            circle at 30% 25%,
            rgba(255,45,170,.30),
            transparent 40%
        ),
        var(--glass);
}

.supernova {
    background:
        radial-gradient(
            circle at 60% 30%,
            rgba(255,179,71,.35),
            transparent 32%
        ),
        var(--glass);
}

.cluster {
    background:
        radial-gradient(
            circle at 45% 30%,
            rgba(0,229,255,.30),
            transparent 42%
        ),
        var(--glass);
}


/* ============================================================
   EXPLORER
   ============================================================ */

.explorer-layout {
    display: grid;

    grid-template-columns:
        minmax(260px,400px)
        1fr;

    gap: 24px;

    margin-top: 45px;
}

.explorer-list {
    display: grid;

    gap: 12px;
}

.explorer-card {
    padding: 22px;

    cursor: pointer;

    transition:
        .3s ease;
}

.explorer-card:hover,
.explorer-card.selected {
    transform:
        translateX(6px);

    border-color:
        rgba(0,229,255,.45);

    box-shadow:
        0 0 40px
        rgba(0,229,255,.10);
}

.explorer-card h3 {
    margin-bottom: 8px;

    font-size: 17px;
}

.explorer-card p {
    color: var(--muted);

    font-size: 12px;

    line-height: 1.55;
}

.detail-panel {
    min-height: 430px;

    padding: 35px;
}

.detail-panel h3 {
    margin-bottom: 18px;

    font-size:
        clamp(
            28px,
            5vw,
            56px
        );
}

.detail-panel p {
    color: var(--muted);

    font-size: 16px;

    line-height: 1.75;
}

.detail-stats {
    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 14px;

    margin-top: 30px;
}

.detail-stat {
    padding: 16px;

    border:
        1px solid
        rgba(0,229,255,.10);

    border-radius: 16px;

    background:
        rgba(255,255,255,.025);
}

.detail-stat span {
    display: block;

    color:
        rgba(205,220,255,.45);

    font-size: 9px;

    text-transform: uppercase;

    letter-spacing: 1.5px;
}

.detail-stat strong {
    display: block;

    margin-top: 10px;

    font-family: Orbitron, sans-serif;

    font-size: 19px;
}


/* ============================================================
   DATA
   ============================================================ */

.data-card {
    min-height: 200px;

    padding: 28px;
}

.data-label {
    color:
        rgba(205,220,255,.48);

    font-family: Orbitron, sans-serif;

    font-size: 9px;
    font-weight: 700;

    letter-spacing: 2px;
}

.data-value {
    display: block;

    margin-top: 28px;

    font-family: Orbitron, sans-serif;

    font-size:
        clamp(
            26px,
            4vw,
            48px
        );

    font-weight: 900;

    text-shadow:
        0 0 30px
        rgba(0,229,255,.25);
}

.data-note {
    margin-top: 30px;

    color:
        rgba(205,220,255,.55);

    line-height: 1.7;

    font-size: 13px;
}


/* ============================================================
   FINAL
   ============================================================ */

.tiny-earth {
    width: 30px;
    height: 30px;

    margin:
        0
        auto
        50px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 30% 25%,
            #e4ffff,
            #4db8ff 40%,
            #092e75 75%
        );

    box-shadow:
        0 0 40px
        rgba(0,229,255,.8),
        0 0 200px
        rgba(0,229,255,.3);

    animation:
        earthFloat
        6s
        ease-in-out
        infinite;
}

@keyframes earthFloat {

    0%,100% {
        transform:
            translateY(0);
    }

    50% {
        transform:
            translateY(-14px);
    }
}


/* ============================================================
   REVEAL
   ============================================================ */

.reveal {
    opacity: 0;

    transform:
        translateY(40px)
        scale(.97);

    transition:
        opacity 1s
        cubic-bezier(.2,.8,.2,1),

        transform 1s
        cubic-bezier(.2,.8,.2,1);
}

.reveal.visible {
    opacity: 1;

    transform:
        translateY(0)
        scale(1);
}

.delay-1 {
    transition-delay: .15s;
}

.delay-2 {
    transition-delay: .30s;
}

.delay-3 {
    transition-delay: .45s;
}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 960px) {

    .nav {
        top: 10px;

        padding: 8px;

        border-radius: 20px;
    }

    .brand {
        display: none;
    }

    .nav-links {
        width: 100%;

        justify-content: center;
    }

    .nav-links a {
        padding: 8px 7px;

        font-size: 7px;
    }

    .two-col {
        grid-template-columns: 1fr;
    }

    .grid-4,
    .grid-3 {
        grid-template-columns:
            repeat(2,1fr);
    }

    .explorer-layout {
        grid-template-columns: 1fr;
    }

    .section {
        padding:
            90px
            18px;
    }
}

@media (max-width: 580px) {

    .nav-links a {
        padding:
            7px
            5px;

        font-size: 6px;

        letter-spacing: .6px;
    }

    .grid-4,
    .grid-3,
    .detail-stats {
        grid-template-columns: 1fr;
    }

    .solar-shell {
        min-height: 640px;
    }

    .planet-panel {
        left: 14px;
        right: 14px;

        bottom: 14px;

        width: auto;
    }

    .planet-panel dl {
        grid-template-columns: 1fr;
    }

    .actions {
        width: 100%;
    }

    .btn {
        width: 100%;
    }

    h1 {
        letter-spacing: -1px;
    }
}

@media (prefers-reduced-motion: reduce) {

    *,
    *::before,
    *::after {

        animation-duration:
            .001ms !important;

        animation-iteration-count:
            1 !important;

        transition-duration:
            .001ms !important;

        scroll-behavior:
            auto !important;
    }
}

</style>
</head>


<body>

<!-- ============================================================
     BACKGROUND
     ============================================================ -->

<canvas id="bg-canvas"></canvas>

<div class="aurora"></div>
<div class="dust"></div>
<div class="vignette"></div>


<!-- ============================================================
     NAVIGATION
     ============================================================ -->

<nav class="nav">

    <div class="brand">
        COSMOS<span class="brand-dot"></span>
    </div>

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


<main>


<!-- ============================================================
     HERO
     ============================================================ -->

<section
    id="home"
    class="section hero"
>

    <div class="content center reveal">

        <div class="kicker">
            Cinematic Digital Universe
        </div>

        <h1>
            EXPLORE<br>
            THE UNIVERSE
        </h1>

        <p class="lead">

            Journey beyond the boundaries
            of space, time, and imagination
            into a living digital cosmos.

        </p>

        <div class="actions">

            <button
                class="btn"
                onclick="smoothScroll('#cosmos')"
            >
                BEGIN EXPLORATION
            </button>

            <button
                class="btn secondary"
                onclick="smoothScroll('#solar')"
            >
                DISCOVER COSMOS
            </button>

        </div>

    </div>

    <div class="scroll-cue">
        SCROLL TO EXPLORE
    </div>

</section>


<!-- ============================================================
     COSMIC SCALE
     ============================================================ -->

<section
    id="cosmos"
    class="section tall"
>

<div class="content">

    <div class="two-col">

        <div class="reveal">

            <div class="kicker">
                Cosmic Scale
            </div>

            <h2>
                From one blue world
                to the observable universe.
            </h2>

            <p
                class="lead"
                style="margin-left:0"
            >

                Explore a visual journey
                from Earth and the Moon
                through our solar system
                and into the deep universe.

            </p>

        </div>


        <div
            class="scale-visual glass reveal delay-1"
        >

            <div class="orbit"></div>
            <div class="orbit"></div>
            <div class="orbit"></div>
            <div class="orbit"></div>

            <div class="sun-css"></div>
            <div class="earth-css"></div>

        </div>

    </div>


    <div class="grid-4">

        <div class="metric glass reveal">

            <span class="metric-label">
                KNOWN PLANETS
            </span>

            <span
                class="metric-value counter"
                data-value="8"
            >
                0
            </span>

            <span class="metric-desc">
                Eight primary planets orbit our Sun.
            </span>

        </div>


        <div class="metric glass reveal delay-1">

            <span class="metric-label">
                MILKY WAY STARS
            </span>

            <span
                class="metric-value counter"
                data-value="100"
                data-suffix="+B"
            >
                0
            </span>

            <span class="metric-desc">
                Estimated stellar population.
            </span>

        </div>


        <div class="metric glass reveal delay-2">

            <span class="metric-label">
                UNIVERSE AGE
            </span>

            <span
                class="metric-value counter"
                data-value="13.8"
                data-suffix="B YRS"
            >
                0
            </span>

            <span class="metric-desc">
                Approximate age of the universe.
            </span>

        </div>


        <div class="metric glass reveal delay-3">

            <span class="metric-label">
                OBSERVABLE WIDTH
            </span>

            <span
                class="metric-value counter"
                data-value="93"
                data-suffix="B LY"
            >
                0
            </span>

            <span class="metric-desc">
                Approximate observable diameter.
            </span>

        </div>

    </div>

</div>

</section>


<!-- ============================================================
     SOLAR SYSTEM
     ============================================================ -->

<section
    id="solar"
    class="section"
>

<div class="content">

    <div class="center reveal">

        <div class="kicker">
            Interactive Orrery
        </div>

        <h2>
            SOLAR SYSTEM
        </h2>

        <p class="lead">

            Explore an interactive 3D
            solar system. Move your mouse
            to control the camera and click
            planets to inspect them.

        </p>

    </div>


    <div
        class="solar-shell reveal delay-1"
    >

        <canvas id="solarCanvas"></canvas>


        <div class="solar-toolbar">

            <span class="chip">
                WEBGL ORBITS
            </span>

            <span class="chip">
                INTERACTIVE
            </span>

            <span class="chip">
                PLANET DATA
            </span>

        </div>


        <div
            class="planet-panel glass"
            id="planetPanel"
        >

            <h3>Earth</h3>

            <dl>

                <div>
                    <dt>Diameter</dt>
                    <dd>12,742 km</dd>
                </div>

                <div>
                    <dt>Distance</dt>
                    <dd>149.6M km</dd>
                </div>

                <div>
                    <dt>Orbit</dt>
                    <dd>365.25 days</dd>
                </div>

                <div>
                    <dt>Class</dt>
                    <dd>Terrestrial</dd>
                </div>

            </dl>

            <p>
                The only known world with
                surface oceans and life.
            </p>

        </div>

    </div>

</div>

</section>


<!-- ============================================================
     GALAXY
     ============================================================ -->

<section
    id="galaxy"
    class="section tall"
>

<div class="center reveal">

    <div class="kicker">
        Spiral Structure
    </div>

    <h2 class="massive">
        OUR GALAXY
    </h2>

    <div class="subline">
        ~100,000 LIGHT-YEARS WIDE
    </div>

    <p class="lead">

        A rotating field of stellar particles
        forms spiral arms, glowing clusters,
        and cosmic dust across the Milky Way.

    </p>

</div>

</section>


<!-- ============================================================
     BLACK HOLE
     ============================================================ -->

<section
    id="blackhole"
    class="section"
>

<div class="blackhole-wrap reveal">

    <div class="black-hole"></div>

    <div class="kicker">
        Singularity
    </div>

    <h2>
        BEYOND THE
        EVENT HORIZON
    </h2>

    <p class="lead">
        Where space and time
        lose their meaning.
    </p>

</div>

</section>


<!-- ============================================================
     WORMHOLE
     ============================================================ -->

<section
    id="wormhole"
    class="section tall"
>

<div class="center reveal">

    <div class="kicker">
        Time Warp Corridor
    </div>

    <h2>
        WORMHOLE TRANSIT
    </h2>

    <p class="lead">

        Enter a speculative spacetime tunnel
        surrounded by luminous particles
        and cinematic distortion.

    </p>

    <div class="actions">

        <button
            class="btn"
            onclick="activateWarp()"
        >
            ENGAGE TIME WARP
        </button>

    </div>

</div>

</section>


<!-- ============================================================
     DEEP SPACE
     ============================================================ -->

<section
    id="deep"
    class="section tall"
>

<div class="content">

    <div class="center reveal">

        <div class="kicker">
            Deep Space
        </div>

        <h2>
            NEBULAS,
            SUPERNOVAS,
            AND ANCIENT LIGHT.
        </h2>

        <p class="lead">

            Explore the structures that
            populate the cosmic web.

        </p>

    </div>


    <div class="grid-3">


        <div
            class="deep-card
                   glass
                   nebula
                   reveal"
        >

            <h3>
                Emission Nebulas
            </h3>

            <p>
                Ionized gas creates luminous
                clouds across star-forming regions.
            </p>

        </div>


        <div
            class="deep-card
                   glass
                   supernova
                   reveal
                   delay-1"
        >

            <h3>
                Supernova Remnants
            </h3>

            <p>
                Explosive stellar events spread
                heavier elements across space.
            </p>

        </div>


        <div
            class="deep-card
                   glass
                   cluster
                   reveal
                   delay-2"
        >

            <h3>
                Star Clusters
            </h3>

            <p>
                Thousands of stars can travel
                through space as gravitational families.
            </p>

        </div>


    </div>

</div>

</section>


<!-- ============================================================
     EXPLORER
     ============================================================ -->

<section
    id="explorer"
    class="section"
>

<div class="content">

    <div class="center reveal">

        <div class="kicker">
            Interactive Cosmos
        </div>

        <h2>
            EXPLORER CONSOLE
        </h2>

    </div>


    <div
        class="explorer-layout
               reveal
               delay-1"
    >


        <div class="explorer-list">


            <div
                class="explorer-card
                       glass
                       selected"
                data-kind="galaxy"
            >

                <h3>
                    🌌 Galaxy Explorer
                </h3>

                <p>
                    Spiral arms, stellar halos,
                    and ancient galactic cores.
                </p>

            </div>


            <div
                class="explorer-card glass"
                data-kind="planet"
            >

                <h3>
                    🪐 Planet Explorer
                </h3>

                <p>
                    Atmospheres, surfaces,
                    and orbital periods.
                </p>

            </div>


            <div
                class="explorer-card glass"
                data-kind="star"
            >

                <h3>
                    ⭐ Star Explorer
                </h3>

                <p>
                    Fusion, temperature,
                    luminosity, and stellar evolution.
                </p>

            </div>


            <div
                class="explorer-card glass"
                data-kind="comet"
            >

                <h3>
                    ☄️ Comet Tracker
                </h3>

                <p>
                    Frozen bodies,
                    tails, and orbital paths.
                </p>

            </div>


            <div
                class="explorer-card glass"
                data-kind="blackhole"
            >

                <h3>
                    🕳️ Black Hole Explorer
                </h3>

                <p>
                    Accretion disks,
                    event horizons, and gravity.
                </p>

            </div>


            <div
                class="explorer-card glass"
                data-kind="wormhole"
            >

                <h3>
                    🌀 Wormhole Explorer
                </h3>

                <p>
                    Curved spacetime
                    and speculative time travel.
                </p>

            </div>


        </div>


        <div
            class="detail-panel glass"
            id="explorerDetail"
        ></div>


    </div>

</div>

</section>


<!-- ============================================================
     DATA
     ============================================================ -->

<section
    id="data"
    class="section"
>

<div class="content">

    <div class="reveal">

        <div class="kicker">
            Cosmic Telemetry
        </div>

        <h2>
            LIVE COSMIC DATA
        </h2>

        <p
            class="lead"
            style="margin-left:0"
        >

            Animated demonstration telemetry.
            This interface is structured so
            real astronomy APIs can be connected later.

        </p>

    </div>


    <div class="grid-4">


        <div
            class="data-card
                   glass
                   reveal"
        >

            <span class="data-label">
                STAR COUNT
            </span>

            <span
                class="data-value counter"
                data-value="1284921302"
            >
                0
            </span>

        </div>


        <div
            class="data-card
                   glass
                   reveal
                   delay-1"
        >

            <span class="data-label">
                COSMIC DISTANCE
            </span>

            <span
                class="data-value counter"
                data-value="4.37"
                data-suffix=" LY"
            >
                0
            </span>

        </div>


        <div
            class="data-card
                   glass
                   reveal
                   delay-2"
        >

            <span class="data-label">
                TEMPERATURE
            </span>

            <span
                class="data-value counter"
                data-value="5778"
                data-suffix=" K"
            >
                0
            </span>

        </div>


        <div
            class="data-card
                   glass
                   reveal
                   delay-3"
        >

            <span class="data-label">
                GALAXIES OBSERVED
            </span>

            <span
                class="data-value counter"
                data-value="2000000000"
                data-suffix="+"
            >
                0
            </span>

        </div>


    </div>


    <p class="data-note">

        Demonstration values only.
        They are not live astronomical measurements.

    </p>

</div>

</section>


<!-- ============================================================
     FINAL
     ============================================================ -->

<section
    id="final"
    class="section"
>

<div class="center reveal">

    <div class="tiny-earth"></div>

    <h2>
        WE ARE HERE.
    </h2>

    <p class="lead">
        THE UNIVERSE IS WAITING.
    </p>

    <div class="actions">

        <button
            class="btn"
            onclick="smoothScroll('#home')"
        >
            START AGAIN ↑
        </button>

    </div>

</div>

</section>


</main>


<script>

/* ============================================================
   BASIC UTILITIES
   ============================================================ */

"use strict";

const reducedMotion =
    window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

const isMobile =
    window.matchMedia(
        "(max-width: 700px)"
    ).matches;


function smoothScroll(selector) {

    const element =
        document.querySelector(selector);

    if (!element) return;

    element.scrollIntoView({
        behavior:
            reducedMotion
                ? "auto"
                : "smooth"
    });
}

window.smoothScroll =
    smoothScroll;


/* ============================================================
   ACTIVE NAVIGATION
   ============================================================ */

const sections =
    [...document.querySelectorAll(
        "section[id]"
    )];

const navLinks =
    [...document.querySelectorAll(
        ".nav-links a"
    )];

const navObserver =
    new IntersectionObserver(
        entries => {

            entries.forEach(entry => {

                if (!entry.isIntersecting)
                    return;

                navLinks.forEach(link => {

                    link.classList.toggle(
                        "active",
                        link.getAttribute("href")
                        ===
                        "#" + entry.target.id
                    );

                });

            });

        },
        {
            rootMargin:
                "-40% 0px -55% 0px"
        }
    );

sections.forEach(
    section =>
        navObserver.observe(section)
);


/* ============================================================
   REVEAL ANIMATIONS
   ============================================================ */

const revealObserver =
    new IntersectionObserver(
        entries => {

            entries.forEach(entry => {

                if (
                    entry.isIntersecting
                ) {

                    entry.target
                        .classList
                        .add("visible");

                }

            });

        },
        {
            threshold: .12
        }
    );

document
    .querySelectorAll(".reveal")
    .forEach(element =>
        revealObserver.observe(element)
    );


/* ============================================================
   COUNTERS
   ============================================================ */

function animateCounter(element) {

    if (element.dataset.done)
        return;

    element.dataset.done = "true";

    const target =
        Number(
            element.dataset.value || 0
        );

    const suffix =
        element.dataset.suffix || "";

    const hasDecimal =
        String(
            element.dataset.value
        ).includes(".");

    const decimals =
        hasDecimal ? 2 : 0;

    const start =
        performance.now();

    const duration =
        reducedMotion
            ? 1
            : 1800;


    function tick(now) {

        const progress =
            Math.min(
                1,
                (now - start) /
                duration
            );

        const eased =
            1 -
            Math.pow(
                1 - progress,
                4
            );

        const value =
            target * eased;

        element.textContent =
            value.toLocaleString(
                undefined,
                {
                    maximumFractionDigits:
                        decimals
                }
            )
            + suffix;

        if (progress < 1) {

            requestAnimationFrame(
                tick
            );

        }

    }

    requestAnimationFrame(tick);
}


const counterObserver =
    new IntersectionObserver(
        entries => {

            entries.forEach(entry => {

                if (
                    entry.isIntersecting
                ) {

                    animateCounter(
                        entry.target
                    );

                }

            });

        },
        {
            threshold: .4
        }
    );


document
    .querySelectorAll(".counter")
    .forEach(counter =>
        counterObserver.observe(counter)
    );


/* ============================================================
   EXPLORER
   ============================================================ */

const explorerData = {

    galaxy: {
        title:
            "Galaxy Explorer",

        description:
            "Survey spiral arms, stellar halos, luminous dust lanes, and dense galactic cores. The Milky Way is represented as a rotating particle system.",

        stats: [
            ["Scale","100K LY"],
            ["Motion","Rotation"],
            ["Focus","Spiral Arms"]
        ]
    },

    planet: {
        title:
            "Planet Explorer",

        description:
            "Compare rocky and gas worlds by atmosphere, radius, orbital period, and solar distance.",

        stats: [
            ["Worlds","8"],
            ["Types","4"],
            ["Focus","Habitability"]
        ]
    },

    star: {
        title:
            "Star Explorer",

        description:
            "Explore how stellar mass, temperature, and luminosity influence the life cycle of a star.",

        stats: [
            ["Fuel","Fusion"],
            ["Output","Light"],
            ["Focus","Lifecycle"]
        ]
    },

    comet: {
        title:
            "Comet Tracker",

        description:
            "Trace high-eccentricity paths around the Sun as frozen material heats and produces a glowing coma and tail.",

        stats: [
            ["Path","Elliptic"],
            ["Material","Ice/Rock"],
            ["Focus","Perihelion"]
        ]
    },

    blackhole: {
        title:
            "Black Hole Explorer",

        description:
            "Explore extreme gravity, accretion disks, relativistic effects, and the event horizon.",

        stats: [
            ["Boundary","Horizon"],
            ["Disk","Accretion"],
            ["Focus","Gravity"]
        ]
    },

    wormhole: {
        title:
            "Wormhole Explorer",

        description:
            "A speculative spacetime bridge rendered as luminous rings, particles, and camera-reactive distortion.",

        stats: [
            ["Model","Speculative"],
            ["Effect","Lensing"],
            ["Focus","Time Warp"]
        ]
    }

};


const detail =
    document.getElementById(
        "explorerDetail"
    );


function setExplorer(kind) {

    const data =
        explorerData[kind];

    if (!data) return;

    detail.innerHTML = `

        <h3>
            ${data.title}
        </h3>

        <p>
            ${data.description}
        </p>

        <div class="detail-stats">

            ${data.stats.map(
                item => `

                    <div class="detail-stat">

                        <span>
                            ${item[0]}
                        </span>

                        <strong>
                            ${item[1]}
                        </strong>

                    </div>

                `
            ).join("")}

        </div>

    `;
}


document
    .querySelectorAll(".explorer-card")
    .forEach(card => {

        card.addEventListener(
            "click",
            () => {

                document
                    .querySelectorAll(
                        ".explorer-card"
                    )
                    .forEach(
                        c =>
                            c.classList
                                .remove(
                                    "selected"
                                )
                    );

                card.classList.add(
                    "selected"
                );

                setExplorer(
                    card.dataset.kind
                );

            }
        );

    });


setExplorer("galaxy");


/* ============================================================
   THREE.JS BACKGROUND
   ============================================================ */

if (!window.THREE) {

    console.error(
        "Three.js failed to load."
    );

} else {

    const THREE =
        window.THREE;


    const canvas =
        document.getElementById(
            "bg-canvas"
        );


    const renderer =
        new THREE.WebGLRenderer({

            canvas,

            antialias:
                !isMobile,

            alpha:
                true,

            powerPreference:
                "high-performance"

        });


    renderer.setPixelRatio(
        Math.min(
            window.devicePixelRatio || 1,
            isMobile ? 1.25 : 1.6
        )
    );


    renderer.setClearColor(
        0x000008,
        1
    );


    const scene =
        new THREE.Scene();


    const camera =
        new THREE.PerspectiveCamera(
            58,
            window.innerWidth /
                window.innerHeight,
            .1,
            3000
        );


    camera.position.set(
        0,
        0,
        80
    );


    const mouse =
        new THREE.Vector2();

    const mouseTarget =
        new THREE.Vector2();


    window.addEventListener(
        "pointermove",
        event => {

            mouseTarget.x =
                (
                    event.clientX /
                    window.innerWidth -
                    .5
                ) * 2;

            mouseTarget.y =
                (
                    event.clientY /
                    window.innerHeight -
                    .5
                ) * 2;

        },
        {
            passive: true
        }
    );


    function resize() {

        renderer.setSize(
            window.innerWidth,
            window.innerHeight,
            false
        );

        camera.aspect =
            window.innerWidth /
            window.innerHeight;

        camera.updateProjectionMatrix();

    }


    window.addEventListener(
        "resize",
        resize
    );

    resize();


    /* ========================================================
       STAR FIELD
       ======================================================== */

    function createStars(
        count,
        radius,
        size,
        colorA,
        colorB
    ) {

        const positions =
            new Float32Array(
                count * 3
            );

        const colors =
            new Float32Array(
                count * 3
            );

        const a =
            new THREE.Color(
                colorA
            );

        const b =
            new THREE.Color(
                colorB
            );


        for (
            let i = 0;
            i < count;
            i++
        ) {

            const r =
                radius *
                Math.cbrt(
                    Math.random()
                );

            const theta =
                Math.random() *
                Math.PI * 2;

            const phi =
                Math.acos(
                    2 *
                    Math.random() -
                    1
                );


            positions[i * 3] =
                r *
                Math.sin(phi) *
                Math.cos(theta);

            positions[i * 3 + 1] =
                r *
                Math.sin(phi) *
                Math.sin(theta);

            positions[i * 3 + 2] =
                r *
                Math.cos(phi);


            const color =
                a.clone().lerp(
                    b,
                    Math.random()
                );


            const brightness =
                .55 +
                Math.random() *
                .8;


            colors[i * 3] =
                color.r *
                brightness;

            colors[i * 3 + 1] =
                color.g *
                brightness;

            colors[i * 3 + 2] =
                color.b *
                brightness;

        }


        const geometry =
            new THREE.BufferGeometry();


        geometry.setAttribute(
            "position",
            new THREE.BufferAttribute(
                positions,
                3
            )
        );


        geometry.setAttribute(
            "color",
            new THREE.BufferAttribute(
                colors,
                3
            )
        );


        const material =
            new THREE.PointsMaterial({

                size,

                vertexColors:
                    true,

                transparent:
                    true,

                opacity:
                    .85,

                depthWrite:
                    false,

                blending:
                    THREE.AdditiveBlending

            });


        return new THREE.Points(
            geometry,
            material
        );

    }


    const nearStars =
        createStars(
            isMobile
                ? 2500
                : 6500,
            480,
            isMobile
                ? .42
                : .30,
            "#dffaff",
            "#7777ff"
        );


    const midStars =
        createStars(
            isMobile
                ? 1800
                : 4500,
            700,
            isMobile
                ? .48
                : .36,
            "#ffffff",
            "#55d8ff"
        );


    const farStars =
        createStars(
            isMobile
                ? 3000
                : 8500,
            1000,
            isMobile
                ? .55
                : .42,
            "#ffffff",
            "#40bfff"
        );


    scene.add(
        nearStars,
        midStars,
        farStars
    );


    /* ========================================================
       NEBULA PARTICLES
       ======================================================== */

    const nebula =
        new THREE.Group();


    const nebulaCount =
        isMobile ? 15 : 32;


    for (
        let i = 0;
        i < nebulaCount;
        i++
    ) {

        const textureCanvas =
            document.createElement(
                "canvas"
            );

        textureCanvas.width =
            128;

        textureCanvas.height =
            128;


        const ctx =
            textureCanvas.getContext(
                "2d"
            );


        const gradient =
            ctx.createRadialGradient(
                64,
                64,
                0,
                64,
                64,
                64
            );


        const colors = [

            ["0,229,255",
             "255,45,170"],

            ["168,85,247",
             "0,229,255"],

            ["255,179,71",
             "255,45,170"]

        ];


        const pair =
            colors[i % colors.length];


        gradient.addColorStop(
            0,
            `rgba(${pair[0]},.65)`
        );

        gradient.addColorStop(
            .35,
            `rgba(${pair[1]},.20)`
        );

        gradient.addColorStop(
            1,
            "rgba(0,0,0,0)"
        );


        ctx.fillStyle =
            gradient;

        ctx.fillRect(
            0,
            0,
            128,
            128
        );


        const texture =
            new THREE.CanvasTexture(
                textureCanvas
            );


        const material =
            new THREE.SpriteMaterial({

                map:
                    texture,

                transparent:
                    true,

                opacity:
                    .08 +
                    Math.random() *
                    .12,

                blending:
                    THREE.AdditiveBlending,

                depthWrite:
                    false

            });


        const sprite =
            new THREE.Sprite(
                material
            );


        sprite.position.set(

            (
                Math.random() -
                .5
            ) * 500,

            (
                Math.random() -
                .5
            ) * 320,

            -150 -
            Math.random() *
            500

        );


        const size =
            50 +
            Math.random() *
            150;


        sprite.scale.set(
            size,
            size,
            1
        );


        nebula.add(
            sprite
        );

    }


    scene.add(
        nebula
    );


    /* ========================================================
       EARTH
       ======================================================== */

    const earthGroup =
        new THREE.Group();


    const earth =
        new THREE.Mesh(

            new THREE.SphereGeometry(
                16,
                48,
                48
            ),

            new THREE.MeshStandardMaterial({

                color:
                    0x2080e0,

                roughness:
                    .72,

                metalness:
                    .02,

                emissive:
                    0x061230,

                emissiveIntensity:
                    .20

            })

        );


    earthGroup.add(
        earth
    );


    const atmosphere =
        new THREE.Mesh(

            new THREE.SphereGeometry(
                16.5,
                48,
                48
            ),

            new THREE.MeshBasicMaterial({

                color:
                    0x40c8ff,

                transparent:
                    true,

                opacity:
                    .12,

                blending:
                    THREE.AdditiveBlending

            })

        );


    earthGroup.add(
        atmosphere
    );


    earthGroup.position.set(
        0,
        -3,
        -20
    );


    scene.add(
        earthGroup
    );


    /* ========================================================
       LIGHT
       ======================================================== */

    const light =
        new THREE.PointLight(
            0x8defff,
            3,
            500
        );


    light.position.set(
        50,
        35,
        50
    );


    scene.add(
        light
    );


    scene.add(
        new THREE.AmbientLight(
            0x304f9c,
            .8
        )
    );


    /* ========================================================
       GALAXY
       ======================================================== */

    function createGalaxy(
        count
    ) {

        const positions =
            new Float32Array(
                count * 3
            );

        const colors =
            new Float32Array(
                count * 3
            );


        const core =
            new THREE.Color(
                "#fff6d5"
            );

        const cyan =
            new THREE.Color(
                "#00e5ff"
            );

        const pink =
            new THREE.Color(
                "#ff2daa"
            );


        for (
            let i = 0;
            i < count;
            i++
        ) {

            const arm =
                i % 5;

            const radius =
                Math.pow(
                    Math.random(),
                    .52
                ) * 95;


            const angle =
                arm / 5 *
                Math.PI * 2 +
                radius * .058 +
                (
                    Math.random() -
                    .5
                ) * .55;


            const scatter =
                (
                    Math.random() -
                    .5
                ) * 8;


            positions[i * 3] =
                Math.cos(angle) *
                radius +
                scatter;

            positions[i * 3 + 1] =
                (
                    Math.random() -
                    .5
                ) *
                5;

            positions[i * 3 + 2] =
                Math.sin(angle) *
                radius +
                scatter;


            const color =
                core.clone().lerp(
                    i % 3
                        ? cyan
                        : pink,
                    Math.min(
                        1,
                        radius / 95
                    )
                );


            colors[i * 3] =
                color.r;

            colors[i * 3 + 1] =
                color.g;

            colors[i * 3 + 2] =
                color.b;

        }


        const geometry =
            new THREE.BufferGeometry();


        geometry.setAttribute(
            "position",
            new THREE.BufferAttribute(
                positions,
                3
            )
        );


        geometry.setAttribute(
            "color",
            new THREE.BufferAttribute(
                colors,
                3
            )
        );


        return geometry;

    }


    const galaxy =
        new THREE.Points(

            createGalaxy(
                isMobile
                    ? 5000
                    : 12000
            ),

            new THREE.PointsMaterial({

                size:
                    isMobile
                        ? .35
                        : .22,

                vertexColors:
                    true,

                transparent:
                    true,

                opacity:
                    .82,

                depthWrite:
                    false,

                blending:
                    THREE.AdditiveBlending

            })

        );


    galaxy.position.set(
        0,
        0,
        -280
    );


    galaxy.scale.setScalar(
        .08
    );


    scene.add(
        galaxy
    );


    /* ========================================================
       WORMHOLE
       ======================================================== */

    const wormhole =
        new THREE.Group();


    for (
        let i = 0;
        i < 36;
        i++
    ) {

        const radius =
            10 +
            Math.sin(
                i * .6
            ) * 3 +
            i * .18;


        const material =
            new THREE.MeshBasicMaterial({

                color:
                    i % 2
                        ? 0x00e5ff
                        : 0xff2daa,

                transparent:
                    true,

                opacity:
                    .12,

                blending:
                    THREE.AdditiveBlending,

                side:
                    THREE.DoubleSide

            });


        const ring =
            new THREE.Mesh(

                new THREE.TorusGeometry(
                    radius,
                    .045,
                    8,
                    100
                ),

                material

            );


        ring.position.z =
            -i * 6;


        ring.rotation.z =
            i * .2;


        wormhole.add(
            ring
        );

    }


    wormhole.position.set(
        0,
        0,
        40
    );


    wormhole.visible =
        false;


    scene.add(
        wormhole
    );


    /* ========================================================
       COMETS
       ======================================================== */

    const comets = [];


    for (
        let i = 0;
        i < 5;
        i++
    ) {

        const geometry =
            new THREE.BufferGeometry()
                .setFromPoints([

                    new THREE.Vector3(
                        0,
                        0,
                        0
                    ),

                    new THREE.Vector3(
                        -25,
                        10,
                        0
                    )

                ]);


        const material =
            new THREE.LineBasicMaterial({

                color:
                    i % 2
                        ? 0x00e5ff
                        : 0xfff3cf,

                transparent:
                    true,

                opacity:
                    .45,

                blending:
                    THREE.AdditiveBlending

            });


        const comet =
            new THREE.Line(
                geometry,
                material
            );


        comet.position.set(

            -300 -
            i * 90,

            100 +
            Math.random() *
            200,

            -150 -
            Math.random() *
            400

        );


        comet.userData.speed =
            .35 +
            Math.random() *
            .45;


        scene.add(
            comet
        );


        comets.push(
            comet
        );

    }


    /* ========================================================
       WORMHOLE BUTTON
       ======================================================== */

    window.activateWarp =
        function () {

            wormhole.visible =
                true;

            wormhole.scale.setScalar(
                1.7
            );

            setTimeout(
                () => {

                    wormhole.scale.setScalar(
                        1
                    );

                },
                900
            );

        };


    /* ========================================================
       ANIMATION
       ======================================================== */

    let previousTime =
        0;


    function animate(time) {

        if (
            reducedMotion &&
            time -
            previousTime <
            100
        ) {

            requestAnimationFrame(
                animate
            );

            return;

        }


        previousTime =
            time;


        const t =
            time * .001;


        const scroll =
            window.scrollY ||
            document.documentElement
                .scrollTop;


        mouse.x +=
            (
                mouseTarget.x -
                mouse.x
            ) * .04;


        mouse.y +=
            (
                mouseTarget.y -
                mouse.y
            ) * .04;


        /* Stars */

        nearStars.rotation.y =
            t * .018;

        nearStars.rotation.x =
            mouse.y * .03;


        midStars.rotation.y =
            -t * .011;


        farStars.rotation.y =
            t * .006;


        /* Nebula */

        nebula.rotation.z =
            t * .004;

        nebula.position.x =
            mouse.x * -8;

        nebula.position.y =
            mouse.y * 5;


        /* Earth */

        earth.rotation.y +=
            .0028;

        earthGroup.rotation.x =
            mouse.y * .05;

        earthGroup.position.x =
            mouse.x * 3;


        /* Galaxy */

        galaxy.rotation.y =
            t * .035 +
            scroll * .00005;

        galaxy.rotation.z =
            .25 +
            t * .008;


        const galaxyProgress =
            Math.max(
                0,
                Math.min(
                    1,
                    (
                        document
                            .getElementById(
                                "galaxy"
                            )
                            .getBoundingClientRect()
                            .top
                    ) /
                    -window.innerHeight +
                    1
                )
            );


        galaxy.scale.setScalar(
            .08 +
            galaxyProgress *
            1.8
        );


        galaxy.position.z =
            -280 +
            galaxyProgress *
            190;


        /* Wormhole */

        if (
            wormhole.visible
        ) {

            wormhole.rotation.z =
                t * .25 +
                mouse.x * .15;

            wormhole.rotation.x =
                mouse.y * .08;

            wormhole.position.x =
                mouse.x * -6;

            wormhole.position.y =
                mouse.y * 5;

        }


        /* Comets */

        comets.forEach(
            comet => {

                comet.position.x +=
                    comet.userData.speed;

                comet.position.y -=
                    comet.userData.speed *
                    .18;


                if (
                    comet.position.x >
                    300
                ) {

                    comet.position.x =
                        -350;

                }

            }
        );


        /* Camera */

        camera.position.x +=
            (
                mouse.x * 6 -
                camera.position.x
            ) * .03;


        camera.position.y +=
            (
                -mouse.y * 5 -
                camera.position.y
            ) * .03;


        camera.position.z =
            80 +
            Math.sin(
                t * .12
            ) * 2;


        camera.lookAt(
            0,
            0,
            -80
        );


        renderer.render(
            scene,
            camera
        );


        requestAnimationFrame(
            animate
        );

    }


    requestAnimationFrame(
        animate
    );

}


/* ============================================================
   SOLAR SYSTEM
   ============================================================ */

function setupSolarSystem() {

    if (!window.THREE)
        return;


    const THREE =
        window.THREE;


    const canvas =
        document.getElementById(
            "solarCanvas"
        );


    const container =
        canvas.parentElement;


    const renderer =
        new THREE.WebGLRenderer({

            canvas,

            antialias:
                !isMobile,

            alpha:
                true,

            powerPreference:
                "high-performance"

        });


    renderer.setPixelRatio(
        Math.min(
            window.devicePixelRatio || 1,
            isMobile ? 1.2 : 1.5
        )
    );


    const scene =
        new THREE.Scene();


    const camera =
        new THREE.PerspectiveCamera(
            50,
            1,
            .1,
            1000
        );


    camera.position.set(
        0,
        90,
        180
    );


    scene.add(
        new THREE.AmbientLight(
            0x5080c0,
            .65
        )
    );


    const sunLight =
        new THREE.PointLight(
            0xffd890,
            5,
            600
        );


    scene.add(
        sunLight
    );


    /* ========================================================
       SUN
       ======================================================== */

    const sun =
        new THREE.Mesh(

            new THREE.SphereGeometry(
                14,
                48,
                48
            ),

            new THREE.MeshBasicMaterial({
                color:
                    0xffb347
            })

        );


    scene.add(
        sun
    );


    const sunGlow =
        new THREE.Mesh(

            new THREE.SphereGeometry(
                19,
                40,
                40
            ),

            new THREE.MeshBasicMaterial({

                color:
                    0xff8530,

                transparent:
                    true,

                opacity:
                    .20,

                blending:
                    THREE.AdditiveBlending

            })

        );


    scene.add(
        sunGlow
    );


    /* ========================================================
       PLANETS
       ======================================================== */

    const planets = [

        {
            name: "Mercury",
            radius: 3,
            orbit: 24,
            speed: .045,
            color: 0xb9afa1,
            diameter: "4,879 km",
            distance: "57.9M km",
            period: "88 days",
            type: "Terrestrial",
            description:
                "The smallest planet, with extreme temperature changes."
        },

        {
            name: "Venus",
            radius: 5,
            orbit: 34,
            speed: .030,
            color: 0xe0ae6b,
            diameter: "12,104 km",
            distance: "108.2M km",
            period: "225 days",
            type: "Terrestrial",
            description:
                "A world covered by a dense atmosphere and intense heat."
        },

        {
            name: "Earth",
            radius: 6,
            orbit: 46,
            speed: .024,
            color: 0x348eff,
            diameter: "12,742 km",
            distance: "149.6M km",
            period: "365.25 days",
            type: "Terrestrial",
            description:
                "The only known world with surface oceans and life."
        },

        {
            name: "Mars",
            radius: 4.5,
            orbit: 58,
            speed: .020,
            color: 0xd75a3c,
            diameter: "6,779 km",
            distance: "227.9M km",
            period: "687 days",
            type: "Terrestrial",
            description:
                "The red planet, home to Olympus Mons."
        },

        {
            name: "Jupiter",
            radius: 12,
            orbit: 80,
            speed: .012,
            color: 0xd8ad82,
            diameter: "139,820 km",
            distance: "778.5M km",
            period: "11.9 years",
            type: "Gas Giant",
            description:
                "The largest planet with enormous atmospheric storms."
        },

        {
            name: "Saturn",
            radius: 11,
            orbit: 102,
            speed: .009,
            color: 0xe5d09a,
            diameter: "116,460 km",
            distance: "1.43B km",
            period: "29.5 years",
            type: "Gas Giant",
            description:
                "Famous for its spectacular system of icy rings."
        },

        {
            name: "Uranus",
            radius: 8,
            orbit: 124,
            speed: .006,
            color: 0x8de8ff,
            diameter: "50,724 km",
            distance: "2.87B km",
            period: "84 years",
            type: "Ice Giant",
            description:
                "An ice giant that rotates almost completely on its side."
        },

        {
            name: "Neptune",
            radius: 8,
            orbit: 146,
            speed: .005,
            color: 0x4d75ff,
            diameter: "49,244 km",
            distance: "4.50B km",
            period: "164.8 years",
            type: "Ice Giant",
            description:
                "A distant blue world with extremely fast winds."
        }

    ];


    const meshes = [];


    /* Orbit rings */

    planets.forEach(
        planet => {

            const ring =
                new THREE.Mesh(

                    new THREE.RingGeometry(
                        planet.orbit -
                            .04,
                        planet.orbit +
                            .04,
                        160
                    ),

                    new THREE.MeshBasicMaterial({

                        color:
                            0x50d8ff,

                        transparent:
                            true,

                        opacity:
                            .12,

                        side:
                            THREE.DoubleSide

                    })

                );


            ring.rotation.x =
                Math.PI / 2;


            scene.add(
                ring
            );

        }
    );


    /* Planet meshes */

    planets.forEach(
        planet => {

            const material =
                new THREE.MeshStandardMaterial({

                    color:
                        planet.color,

                    roughness:
                        .72,

                    metalness:
                        .02

                });


            const mesh =
                new THREE.Mesh(

                    new THREE.SphereGeometry(
                        planet.radius,
                        32,
                        32
                    ),

                    material

                );


            mesh.userData.info =
                planet;


            scene.add(
                mesh
            );


            meshes.push(
                mesh
            );


            /* Saturn ring */

            if (
                planet.name ===
                "Saturn"
            ) {

                const ring =
                    new THREE.Mesh(

                        new THREE.RingGeometry(
                            14,
                            21,
                            100
                        ),

                        new THREE.MeshBasicMaterial({

                            color:
                                0xe5d09a,

                            transparent:
                                true,

                            opacity:
                                .45,

                            side:
                                THREE.DoubleSide

                        })

                    );


                ring.rotation.x =
                    Math.PI / 2.4;


                mesh.add(
                    ring
                );

            }

        }
    );


    /* ========================================================
       POINTER
       ======================================================== */

    const pointer =
        new THREE.Vector2(
            99,
            99
        );


    const raycaster =
        new THREE.Raycaster();


    canvas.addEventListener(
        "pointermove",
        event => {

            const rect =
                canvas.getBoundingClientRect();


            pointer.x =
                (
                    (
                        event.clientX -
                        rect.left
                    ) /
                    rect.width
                ) * 2 - 1;


            pointer.y =
                -(
                    (
                        event.clientY -
                        rect.top
                    ) /
                    rect.height
                ) * 2 + 1;

        },
        {
            passive: true
        }
    );


    const panel =
        document.getElementById(
            "planetPanel"
        );


    function updatePanel(
        planet
    ) {

        panel.innerHTML = `

            <h3>
                ${planet.name}
            </h3>

            <dl>

                <div>
                    <dt>Diameter</dt>
                    <dd>
                        ${planet.diameter}
                    </dd>
                </div>

                <div>
                    <dt>Distance</dt>
                    <dd>
                        ${planet.distance}
                    </dd>
                </div>

                <div>
                    <dt>Orbit</dt>
                    <dd>
                        ${planet.period}
                    </dd>
                </div>

                <div>
                    <dt>Class</dt>
                    <dd>
                        ${planet.type}
                    </dd>
                </div>

            </dl>

            <p>
                ${planet.description}
            </p>

        `;

    }


    canvas.addEventListener(
        "click",
        () => {

            raycaster.setFromCamera(
                pointer,
                camera
            );


            const hits =
                raycaster.intersectObjects(
                    meshes
                );


            if (
                hits.length
            ) {

                const info =
                    hits[0]
                        .object
                        .userData
                        .info;


                if (info) {

                    updatePanel(
                        info
                    );

                }

            }

        }
    );


    /* ========================================================
       RESIZE
       ======================================================== */

    function resizeSolar() {

        const rect =
            container
                .getBoundingClientRect();


        renderer.setSize(
            rect.width,
            rect.height,
            false
        );


        camera.aspect =
            rect.width /
            rect.height;


        camera.updateProjectionMatrix();

    }


    const resizeObserver =
        new ResizeObserver(
            resizeSolar
        );


    resizeObserver.observe(
        container
    );


    resizeSolar();


    /* ========================================================
       SOLAR LOOP
       ======================================================== */

    function solarLoop(
        time
    ) {

        const t =
            time * .001;


        sun.scale.setScalar(
            1 +
            Math.sin(t * 3) *
            .025
        );


        sunGlow.scale.setScalar(
            1 +
            Math.sin(t * 2) *
            .08
        );


        planets.forEach(
            (planet, index) => {

                const mesh =
                    meshes[index];


                const angle =
                    t *
                    planet.speed *
                    16 +
                    index;


                mesh.position.set(

                    Math.cos(angle) *
                        planet.orbit,

                    Math.sin(
                        angle * .35
                    ) * .8,

                    Math.sin(angle) *
                        planet.orbit

                );


                mesh.rotation.y +=
                    .01;

            }
        );


        /* Hover */

        raycaster.setFromCamera(
            pointer,
            camera
        );


        const hits =
            raycaster.intersectObjects(
                meshes
            );


        meshes.forEach(
            mesh => {

                mesh.scale.setScalar(
                    1
                );

            }
        );


        if (
            hits.length
        ) {

            hits[0]
                .object
                .scale
                .setScalar(
                    1.22
                );

        }


        /* Camera */

        camera.position.x +=
            (
                pointer.x * 22 -
                camera.position.x
            ) * .02;


        camera.position.y +=
            (
                90 +
                pointer.y * 14 -
                camera.position.y
            ) * .02;


        camera.lookAt(
            0,
            0,
            0
        );


        renderer.render(
            scene,
            camera
        );


        requestAnimationFrame(
            solarLoop
        );

    }


    requestAnimationFrame(
        solarLoop
    );

}


setupSolarSystem();


</script>

</body>
</html>
"""


# ============================================================
# RENDER
# ============================================================

components.html(
    COSMOS_HTML,
    height=10000,
    scrolling=True,
)
