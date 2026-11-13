import folium
import streamlit as st

m = folium.Map(
    location=[12.902342901448975, 77.51783807813474],
    zoom_start=13,
    tiles="Esri.WorldStreetMap",
)

m