import streamlit as st
import pandas as pd
import numpy as np

st.title('Skill-Scoring Weather Predictions')

st.write('Average hourly observed weather values across all weather stations in BC from April 1 - October 31, 2022:')

mean_wx_values = {
    'temp': 9.52,
    'rh': 68.67,
    'wind_dir': 182.31,
    'wind_speed': 6.39
}

col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", str(mean_wx_values['temp']) + " °C")
col2.metric("Relative Humidity", str(mean_wx_values['rh']) + "%")
col3.metric("Wind Speed", str(mean_wx_values['wind_speed']) + " km/h")
col4.metric("Wind Direction", str(mean_wx_values['wind_dir']) + "°")

st.write("R² baseline score of 0.0")

