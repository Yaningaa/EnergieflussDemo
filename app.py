# Energiefluss-Demo-App (gekürzt & bereinigt für Deployment)

import streamlit as st
import pandas as pd
import numpy as np

sprachwahl = st.sidebar.selectbox("🌍 Sprache / Language", ["Deutsch", "English"])
lang = "de" if sprachwahl == "Deutsch" else "en"

texts = {
    "de": {"title": "🔋 Energieflusss-Demo"},
    "en": {"title": "🔋 Energy Flow Demo"}
}[lang]

st.set_page_config(layout="wide", page_title=texts["title"], page_icon="☀️")
st.title(texts["title"])

# Dummy-Visualisierung
zeit = pd.date_range("00:00", "23:45", freq="15min")
pv = np.sin(np.linspace(0, np.pi, len(zeit))) * 7
verbrauch = np.random.normal(loc=2.5, scale=0.5, size=len(zeit))

df = pd.DataFrame({"PV [kW]": pv, "Verbrauch [kW]": verbrauch}, index=zeit)
st.line_chart(df)
