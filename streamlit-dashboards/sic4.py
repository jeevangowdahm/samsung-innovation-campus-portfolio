import streamlit as st
import pandas as pd
import random

# =====================================================================
# ⚙️ Page Configurations
# =====================================================================
st.set_page_config(
    page_title="NEO-TOKYO // Home Core",
    page_icon="⚡",
    layout="wide"
)

# =====================================================================
# ⚡ Header & Branding (Text Elements)
# =====================================================================
st.markdown('# 🏙️ NEO-TOKYO // SMART HOME CORE')
st.caption('System Status: OPERATIONAL // Security: SECURE // Protocol: v4.8.2')
st.divider()

# =====================================================================
# 📊 Main Dashboard Metrics & Inputs (Interactive Elements)
# =====================================================================
# Creating a side-by-side grid layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎛️ Environmental Control Interface")
    
    # Interactive Slider for Room Temperature
    room_temp = st.slider("Target Zone Temperature (°C)", min_value=16, max_value=32, value=22)
    
    # Interactive Selectbox for Ambience Profile
    mood_profile = st.selectbox(
        "Select Lighting Profile:",
        ["Cyberpunk Neon", "Midnight Noir", "Solar Flare Gold", "Matrix Green Deep"]
    )
    
    # Checkbox to toggle defense perimeter
    perimeter_lock = st.checkbox("Engage External Defense Perimeter Security Grid", value=True)

with col2:
    st.subheader("📈 Real-time Power Consumables")
    
    # Generate dynamic simulated data based on user input temperature
    base_load = [240, 290, 310, 350, 420]
    modified_load = [x + (room_temp * 2) for x in base_load]
    
    # Put the calculated metrics into a Pandas DataFrame
    power_df = pd.DataFrame({
        'Grid Zone': ['Main Core', 'Cyber Lab', 'Hydro-Bay', 'Shield Generator', 'Life Support'],
        'Energy Drain (kW/h)': modified_load
    })
    
    # Displaying formatting tools and dataframes
    st.write("Current Power Matrix Shift:", power_df)
    
    if perimeter_lock:
        st.success("🔒 Cyber Security Shielding is actively drawing power.")
    else:
        st.warning("⚠️ Security Grid Offline! Internal sectors vulnerable.")

st.divider()

# =====================================================================
# 🎬 Multimedia Stream (Media Elements)
# =====================================================================
st.markdown('### 📡 Active Neural Audio & Video Core Up-Links')
st.text('Streaming data streams straight from orbital and deep atmosphere nodes.')

# Creating two distinct layout columns for media files
media_col1, media_col2 = st.columns(2)

with media_col1:
    st.write("**🔊 Ambience Synthwave Uplink (Audio)**")
    # Live retro synthwave instrumental sample track (No download required)
    st.audio('https://soundhelix.com')

with media_col2:
    st.write("**🌌 Deep Space Observational Uplink (Video)**")
    # Stunning cinematic deep space web visualizer stream (No download required)
    st.video('https://youtube.com')

# =====================================================================
# 📝 System Log Terminal
# =====================================================================
st.divider()
st.subheader("🗒️ Mainframe System Log Code")
st.code(f'''
def system_heartbeat():
    zone_temp = {room_temp}
    profile_selected = "{mood_profile}"
    shield_status = {perimeter_lock}
    print(f"[LOG] System initialized. Temp set to {{zone_temp}}C using {{profile_selected}} protocol.")
''', language='python')
