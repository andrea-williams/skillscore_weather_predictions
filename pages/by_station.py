import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

TEMPS_JSON_PATH = './temperatures_with_station_data.json'
RH_JSON_PATH = './rh_with_station_data.json'
WIND_DIR_JSON_PATH = './wind_dir_with_station_data.json'
WIND_SPEED_JSON_PATH = './wind_speed_with_station_data.json'

CATEGORIES = ['raw_gdps_r2', 'bias_adj_gdps_train_r2', 'bias_adj_gdps_train_r2', 'raw_rdps_r2', 'bias_adj_rdps_train_r2', 'bias_adj_rdps_test_r2', 'raw_hrdps_r2', 'bias_adj_hrdps_train_r2', 'bias_adj_hrdps_test_r2']

initial_mapview_state = pdk.ViewState(
        zoom=4,
        latitude=49.8832,
        longitude=-119.5695
    )

def get_tooltip_text():
    if category == 'raw_gdps_r2':
        return {"text": "{name}\n{raw_gdps_r2}"}
    if category == 'bias_adj_gdps_train_r2':
        return {"text": "{name}\n{bias_adj_gdps_train_r2}"}
    if category == 'bias_adj_gdps_test_r2':
        return {"text": "{name}\n{bias_adj_gdps_test_r2}"}
    if category == 'raw_rdps_r2':
        return {"text": "{name}\n{raw_rdps_r2}"}
    if category == 'bias_adj_rdps_train_r2':
        return {"text": "{name}\n{bias_adj_rdps_train_r2}"}
    if category == 'bias_adj_rdps_test_r2':
        return {"text": "{name}\n{bias_adj_rdps_test_r2}"}
    if category == 'raw_hrdps_r2':
        return {"text": "{name}\n{raw_hrdps_r2}"}
    if category == 'bias_adj_hrdps_train_r2':
        return {"text": "{name}\n{bias_adj_hrdps_train_r2}"}
    if category == 'bias_adj_hrdps_test_r2':
        return {"text": "{name}\n{bias_adj_hrdps_test_r2}"}



st.title('Skill-Scoring by Weather Station')

st.subheader('How to interpret the map')
st.write('Each dot on the map represents a weather station. Green dots correspond to positive R² scores, while red dots correspond to negative R² scores.')
st.write('The larger the dot on the map, the larger the absolute value of a station\'s R² score. For example, a large green dot means that the station has a large positive R² score. A small red dot means that the station has an R² score that is slightly below zero.')

st.header('Temperature')

temps_df = pd.read_json(TEMPS_JSON_PATH, orient='index')

category = st.radio('Select which values to plot on map', CATEGORIES)

map_temps_df = temps_df[['lon','lat','name', category]]
map_temps_df['radius'] = map_temps_df[category].apply(lambda x: abs(x))
map_temps_df['colour'] = map_temps_df[category].apply(lambda x: [34, 139, 34] if x > 0 else [220, 20, 60])
map_temps_df.dropna(inplace=True)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=initial_mapview_state,
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_temps_df,
            get_position='[lon, lat]',
            pickable=True,
            opacity=0.8,
            filled=True,
            stroked=True,
            radius_min_pixels=1,
            radius_max_pixels=100,
            radius_scale=30000,
            line_width_min_pixels=1,
            get_radius="radius",
            get_line_color=[0, 0, 0],
            get_fill_color="colour"
        )
    ],
    tooltip=get_tooltip_text()
))

temps_df.drop(columns=['forecast_r2', 'forecast_sample_size'], inplace=True)
st.dataframe(temps_df, use_container_width=True)


st.header('Relative Humidity')

rh_df = pd.read_json(RH_JSON_PATH, orient='index')


map_rh_df = rh_df[['lon','lat','name', category]]
map_rh_df.dropna(inplace=True)
map_rh_df['radius'] = map_rh_df[category].apply(lambda x: abs(x))
map_rh_df['colour'] = map_rh_df[category].apply(lambda x: [34, 139, 34] if x > 0 else [220, 20, 60])



st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=initial_mapview_state,
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_rh_df,
            get_position='[lon, lat]',
            pickable=True,
            opacity=0.8,
            filled=True,
            stroked=True,
            radius_min_pixels=1,
            radius_max_pixels=100,
            radius_scale=50000,
            line_width_min_pixels=1,
            get_radius="radius",
            get_line_color=[0, 0, 0],
            get_fill_color="colour"
        )
    ],
    tooltip=get_tooltip_text()
))

rh_df.drop(columns=['forecast_r2', 'forecast_sample_size'], inplace=True)
st.dataframe(rh_df)

st.header('Wind Speed')

wind_speed_df = pd.read_json(WIND_SPEED_JSON_PATH, orient='index')

map_ws_df = wind_speed_df[['lon', 'lat', 'name', category]]
map_ws_df.dropna(inplace=True)
map_ws_df['radius'] = map_ws_df[category].apply(lambda x: abs(x))
map_ws_df['colour'] = map_ws_df[category].apply(lambda x: [34, 139, 34] if x > 0 else [220, 20, 60])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=initial_mapview_state,
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_ws_df,
            get_position='[lon, lat]',
            pickable=True,
            opacity=0.8,
            filled=True,
            stroked=True,
            radius_min_pixels=1,
            radius_max_pixels=100,
            radius_scale=10000,
            line_width_min_pixels=1,
            get_radius="radius",
            get_line_color=[0, 0, 0],
            get_fill_color="colour"
        )
    ],
    tooltip=get_tooltip_text()
))

wind_speed_df.drop(columns=['forecast_r2', 'forecast_sample_size'], inplace=True)
st.dataframe(wind_speed_df)

st.header('Wind Direction')

wind_dir_df = pd.read_json(WIND_DIR_JSON_PATH, orient='index')

map_wind_dir_df = wind_dir_df[['lon', 'lat', 'name', category]]
map_wind_dir_df.dropna(inplace=True)
map_wind_dir_df['radius'] = map_wind_dir_df[category].apply(lambda x: abs(x))
map_wind_dir_df['colour'] = map_wind_dir_df[category].apply(lambda x: [34, 139, 34] if x > 0 else [220, 20, 60])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=initial_mapview_state,
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_wind_dir_df,
            get_position='[lon, lat]',
            pickable=True,
            opacity=0.8,
            filled=True,
            stroked=True,
            radius_min_pixels=1,
            radius_max_pixels=100,
            radius_scale=10000,
            line_width_min_pixels=1,
            get_radius="radius",
            get_line_color=[0, 0, 0],
            get_fill_color="colour"
        )
    ],
    tooltip=get_tooltip_text()
))

wind_dir_df.drop(columns=['forecast_r2', 'forecast_sample_size'], inplace=True)
st.dataframe(wind_dir_df)