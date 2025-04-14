# Energiefluss-Demo-App (visuell angepasst mit animierten Unicode-Flüssen)

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

# --- Konfiguration ---
st.set_page_config(layout="wide", page_title="Energiefluss-Demo", page_icon="☀️")
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #042f2e;
        color: white;
    }
    .metric-label { color: #a8d97f !important; }
    .stSlider > div > div { background-color: #97bf0d; }
    </style>
""", unsafe_allow_html=True)

st.title("🔋 Energieflusss-Demo")

# --- Simulationsdaten ---
zeit = pd.date_range("00:00", "23:45", freq="15min")
pv_wert = 5.0
verbrauch_wert = 1.0
soc_wert = 80  # in %
co2_kg = 62
kosten_eur = 0.80

# Dummy-Daten für Diagramm oben
strompreise = np.random.uniform(0.07, 0.16, len(zeit))

# --- Diagramm ---
st.line_chart(pd.Series(strompreise, index=zeit, name="Strompreis [€/kWh]"))

# --- Layout Aufbau ---
col_steuerung, col_visual, col_metrics = st.columns([1, 2, 1])

# --- Linke Spalte: Steuerung ---
with col_steuerung:
    st.subheader("Haushaltsgröße")
    haushalt = st.slider("", 1, 6, 4, label_visibility="collapsed")
    st.markdown("---")

    wallbox = st.toggle("🚗 Wallbox", True)
    waermepumpe = st.toggle("❄️ Wärmepumpe", False)
    klimaanlage = st.toggle("🌿 Klimaanlage", False)

# --- Mitte: Hauptvisualisierung ---
with col_visual:
    st.image("https://img.icons8.com/color/96/solar-panel.png", width=40)
    st.markdown("## 🏡 Energiefluss")
    st.markdown(f"**PV-Erzeugung:** {pv_wert:.1f} kW")
    st.markdown(f"**Hausverbrauch:** {verbrauch_wert:.1f} kW")
    st.markdown("**Batterie:**")
    st.progress(soc_wert / 100)
    st.markdown(f"Füllstand: **{soc_wert}%**")

    # Animierter Unicode-Energiefluss
    with st.empty():
        for i in range(3):
            arrow = ["→", "➡️", "➞"]
            if wallbox:
                st.markdown(f"### ☀️ {arrow[i%3]} 🏡 {arrow[i%3]} 🚗")
            elif waermepumpe:
                st.markdown(f"### ☀️ {arrow[i%3]} 🏡 {arrow[i%3]} ❄️")
            elif klimaanlage:
                st.markdown(f"### ☀️ {arrow[i%3]} 🏡 {arrow[i%3]} 🌿")
            else:
                st.markdown(f"### ☀️ {arrow[i%3]} 🏡")
            time.sleep(0.4)

# --- Rechte Spalte: Metriken ---
with col_metrics:
    st.metric("CO₂ Ersparnis", f"{co2_kg} kg")
    st.metric("Ersparnis", f"{kosten_eur:.2f} €")

# --- Hinweis oder zukünftiger Button für Export / Details ---
st.markdown("---")
st.markdown("*Diese Demo dient der Veranschaulichung typischer Energieflüsse eines modernen Haushalts.*")
