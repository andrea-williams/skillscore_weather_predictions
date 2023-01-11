import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

TEMPS_JSON_PATH = './temp_by_hours_in_advance.json'
RH_JSON_PATH = './rh_by_hours_in_advance.json'
WIND_DIR_JSON_PATH = './wind_dir_by_hours_in_advance.json'
WIND_SPEED_JSON_PATH = './wind_speed_by_hours_in_advance.json'

st.title('Skill-Scoring by Duration of Time in Advance')

st.header('What does "duration of time in advance" mean?')
st.write('Different EC models extend their forecasts to different lengths of time into the future.')
st.write('**GDPS**: 10 days')
st.write('**RDPS**: 7 days')
st.write('**HRDPS**: 2 days')
st.write('The purpose of this analysis is to compare the performance of the EC models when they are forecasting weather for the same weather date at the same prediction time.')

st.header('Temperature')
temp_df = pd.read_json(TEMPS_JSON_PATH, orient='index')
temp_df.drop(columns=['forecast_r2', 'forecast_sample_size'], inplace=True)

serieses = []
for row in temp_df.itertuples():
    serieses.append({'timeframe': row[0], 'category': 'raw_gdps', 'r2': row[1]})
    serieses.append({'timeframe': row[0], 'category': 'raw_rdps', 'r2': row[3]})
    serieses.append({'timeframe': row[0], 'category': 'raw_hrdps', 'r2': row[5]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_gdps_train', 'r2': row[7]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_gdps_test', 'r2': row[10]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_rdps_train', 'r2': row[8]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_rdps_test', 'r2': row[11]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_hrdps_train', 'r2': row[9]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_hrdps_test', 'r2': row[12]})
temp_df_to_chart = pd.DataFrame(data=serieses, columns=['timeframe', 'category', 'r2'])

temp_chart = alt.Chart(temp_df_to_chart).mark_line().encode(
    x=alt.X('timeframe', sort=None),
    y='r2',
    color='category',
    strokeDash='category',
).properties(
    title='Temperature R²'
)

st.altair_chart(temp_chart, use_container_width=True)

st.dataframe(temp_df)

st.header('Relative Humidity')
rh_df = pd.read_json(RH_JSON_PATH, orient='index')
rh_df.drop(columns=['forecast_r2','forecast_sample_size'], inplace=True)

serieses = []
for row in rh_df.itertuples():
    serieses.append({'timeframe': row[0], 'category': 'raw_gdps', 'r2': row[1]})
    serieses.append({'timeframe': row[0], 'category': 'raw_rdps', 'r2': row[3]})
    serieses.append({'timeframe': row[0], 'category': 'raw_hrdps', 'r2': row[5]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_gdps_train', 'r2': row[7]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_gdps_test', 'r2': row[10]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_rdps_train', 'r2': row[8]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_rdps_test', 'r2': row[11]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_hrdps_train', 'r2': row[9]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_hrdps_test', 'r2': row[12]})
rh_df_to_chart = pd.DataFrame(data=serieses, columns=['timeframe', 'category', 'r2'])

rh_chart = alt.Chart(rh_df_to_chart).mark_line().encode(
    x=alt.X('timeframe', sort=None),
    y='r2',
    color='category',
    strokeDash='category',
).properties(
    title='Relative Humidity R²'
)

st.altair_chart(rh_chart, use_container_width=True)

st.dataframe(rh_df)

st.header('Wind Speed')

wind_sp_df = pd.read_json(WIND_SPEED_JSON_PATH, orient='index')
wind_sp_df.drop(columns=['forecast_r2','forecast_sample_size'], inplace=True)

serieses = []
for row in wind_sp_df.itertuples():
    serieses.append({'timeframe': row[0], 'category': 'raw_gdps', 'r2': row[1]})
    serieses.append({'timeframe': row[0], 'category': 'raw_rdps', 'r2': row[3]})
    serieses.append({'timeframe': row[0], 'category': 'raw_hrdps', 'r2': row[5]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_gdps_train', 'r2': row[7]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_gdps_test', 'r2': row[10]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_rdps_train', 'r2': row[8]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_rdps_test', 'r2': row[11]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_hrdps_train', 'r2': row[9]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_hrdps_test', 'r2': row[12]})
wind_sp_df_to_chart = pd.DataFrame(data=serieses, columns=['timeframe', 'category', 'r2'])

wind_sp_chart = alt.Chart(wind_sp_df_to_chart).mark_line().encode(
    x=alt.X('timeframe', sort=None),
    y='r2',
    color='category',
    strokeDash='category'
).properties(
    title='Wind Speed R²'
)

st.altair_chart(wind_sp_chart, use_container_width=True)

st.dataframe(wind_sp_df)

st.header('Wind Direction')

wind_dir_df = pd.read_json(WIND_DIR_JSON_PATH, orient='index')
wind_dir_df.drop(columns=['forecast_r2','forecast_sample_size'], inplace=True)

serieses = []
for row in wind_dir_df.itertuples():
    serieses.append({'timeframe': row[0], 'category': 'raw_gdps', 'r2': row[1]})
    serieses.append({'timeframe': row[0], 'category': 'raw_rdps', 'r2': row[3]})
    serieses.append({'timeframe': row[0], 'category': 'raw_hrdps', 'r2': row[5]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_gdps_train', 'r2': row[7]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_gdps_test', 'r2': row[10]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_rdps_train', 'r2': row[8]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_rdps_test', 'r2': row[11]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_hrdps_train', 'r2': row[9]})
    serieses.append({'timeframe': row[0], 'category': 'bias_adj_hrdps_test', 'r2': row[12]})
wind_dir_df_to_chart = pd.DataFrame(data=serieses, columns=['timeframe', 'category', 'r2'])

wind_dir_chart = alt.Chart(wind_dir_df_to_chart).mark_line().encode(
    x=alt.X('timeframe', sort=None),
    y='r2',
    color='category',
    strokeDash='category'
).properties(
    title='Wind Direction R²'
)

st.altair_chart(wind_dir_chart, use_container_width=True)

st.dataframe(wind_dir_df)