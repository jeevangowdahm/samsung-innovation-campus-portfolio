import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import requests

st.set_page_config(
    page_title="Real Universe Explorer | NASA & SpaceX Live",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600&display=swap');

    .stApp {
        background-color: #03030c;
        color: #e0e0ff;
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ff8a00, #e52e71, #9c27b0, #00bcd4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(229, 46, 113, 0.5);
    }

    .glass-card {
        background: rgba(16, 16, 35, 0.7);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
    }

    .metric-value {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #00bcd4;
    }
</style>
""", unsafe_allow_html=True)

# Fetch NASA APOD (Astronomy Picture of the Day)
@st.cache_data(ttl=3600)
def get_nasa_apod():
    try:
        # Public NASA API key demo
        url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            return res.json()
    except:
        pass
    return None

# Fetch SpaceX Next Launch
@st.cache_data(ttl=3600)
def get_spacex_launch():
    try:
        url = "https://api.spacexdata.com/v4/launches/upcoming"
        res = requests.get(url, timeout=5)
        if res.status_code == 200 and len(res.json()) > 0:
            return res.json()[0]
    except:
        pass
    return None

# Sidebar Control Center
with st.sidebar:
    st.markdown("### 🔭 Real-Time Space Hub")
    st.markdown("---")
    view_mode = st.radio("Navigation View", ["🔴 Live NASA APOD & Feeds", "🚀 Live SpaceX Tracker", "🪐 Real Solar System 3D"])
    st.markdown("---")
    st.markdown("<p style='font-size: 0.8rem; color: #888;'>Connected to NASA & SpaceX Live APIs</p>", unsafe_allow_html=True)

# Main Views
if view_mode == "🔴 Live NASA APOD & Feeds":
    st.markdown('<h1 class="hero-title">NASA ASTRONOMY PICTURE OF THE DAY</h1>', unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a0c0; font-size: 1.1rem;'>Direct feed from NASA's official public observatory API.</p>", unsafe_allow_html=True)
    
    apod = get_nasa_apod()
    if apod:
        col1, col2 = st.columns([2, 1])
        with col1:
            if apod.get("media_type") == "image":
                st.image(apod.get("url"), caption=apod.get("title"), use_container_width=True)
            else:
                st.video(apod.get("url"))
        with col2:
            st.markdown(f"""
            <div class="glass-card">
                <h3>{apod.get('title')}</h3>
                <p><b>Date:</b> {apod.get('date')}</p>
                <p style="font-size: 0.9rem; color: #c0c0e0;">{apod.get('explanation')}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Could not fetch live NASA APOD feed at the moment. Please check your internet connection.")

elif view_mode == "🚀 Live SpaceX Tracker":
    st.markdown('<h1 class="hero-title">SPACEX NEXT LAUNCH TRACKER</h1>', unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a0c0; font-size: 1.1rem;'>Live countdown and mission data straight from SpaceX API.</p>", unsafe_allow_html=True)

    launch = get_spacex_launch()
    if launch:
        name = launch.get("name")
        date = launch.get("date_utc")
        details = launch.get("details", "No mission details released yet.")
        success = launch.get("success")
        
        st.markdown(f"""
        <div class="glass-card">
            <h2>Mission: {name}</h2>
            <p><b>Scheduled Launch (UTC):</b> <span class="metric-value">{date}</span></p>
            <p><b>Mission Details:</b> {details if details else 'Classified / Pending details.'}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("No upcoming SpaceX launches currently listed in the active flight manifest.")

elif view_mode == "🪐 Real Solar System 3D":
    st.markdown('<h1 class="hero-title">REAL ORBITAL 3D SIMULATOR</h1>', unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a0c0; font-size: 1.1rem;'>Interactive Orrery representing relative planetary orbits & rotation in real-time.</p>", unsafe_allow_html=True)

    orrery_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.11.3/p5.min.js"></script>
        <style>
            body { margin: 0; padding: 0; overflow: hidden; background: #03030c; }
            canvas { display: block; }
        </style>
    </head>
    <body>
    <script>
        p5.disableFriendlyErrors = true;
        let planets = [
            { name: 'Mercury', dist: 80, size: 6, speed: 0.04, color: [169,169,169] },
            { name: 'Venus', dist: 130, size: 10, speed: 0.015, color: [238,203,173] },
            { name: 'Earth', dist: 190, size: 12, speed: 0.01, color: [0,119,190] },
            { name: 'Mars', dist: 260, size: 8, speed: 0.008, color: [193,68,14] },
            { name: 'Jupiter', dist: 380, size: 28, speed: 0.002, color: [225,198,153] }
        ];

        function setup() {
            createCanvas(windowWidth, windowHeight - 120, WEBGL);
        }

        function draw() {
            background(3, 3, 12);
            
            // Camera control via mouse
            let camX = map(mouseX, 0, width, -300, 300);
            let camY = map(mouseY, 0, height, -300, 300);
            camera(camX, camY - 100, 600, 0, 0, 0, 0, 1, 0);

            // Sun
            push();
            noStroke();
            fill(255, 204, 0);
            emissiveMaterial(255, 150, 0);
            sphere(45);
            pop();

            // Planets & Orbits
            for (let p of planets) {
                // Orbit ring
                noFill();
                stroke(255, 255, 255, 25);
                ellipse(0, 0, p.dist * 2, p.dist * 2);

                // Planet position
                let angle = frameCount * p.speed;
                let x = cos(angle) * p.dist;
                let z = sin(angle) * p.dist;

                push();
                translate(x, 0, z);
                noStroke();
                fill(p.color);
                ambientMaterial(p.color);
                sphere(p.size);
                pop();
            }
        }

        function windowResized() {
            resizeCanvas(windowWidth, windowHeight - 120);
        }
    </script>
    </body>
    </html>
    """
    components.html(orrery_html, height=650)
