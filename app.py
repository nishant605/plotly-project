import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")


df = pd.read_csv("C:\\Users\\ADMIN\\Downloads\\india.csv")

list_of_state = list(df['State'].unique())
list_of_state.insert(0,'Overall India')

st.sidebar.title('India visulization')

selected_state = st.sidebar.selectbox('Select a state',list_of_state)
primary_ip = st.sidebar.selectbox('Select a Primary parameter',sorted(df.columns[5:]))
secondary_ip= st.sidebar.selectbox('Select a secondary parameter',sorted(df.columns[5:]))
plot = st.sidebar.button('Plot graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('Colour represent secondary Parameter')
    
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        size=primary_ip,
        color=secondary_ip,
        zoom = 4,
        size_max=35,
        mapbox_style="carto-positron",
        width=1200,
        height=700,
        color_continuous_scale='Viridis',
        hover_name='District'
        )
        st.plotly_chart(
        fig,
        use_container_width=True,
        config={"scrollZoom": True}
        )
    

    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(
        state_df,
        lat="Latitude",
        lon="Longitude",
        size=primary_ip,
        color=secondary_ip,
        zoom = 4,
        size_max=35,
        mapbox_style="carto-positron",
        width=1200,
        height=700,
        color_continuous_scale='Viridis',
        hover_name='District'
        )
        st.plotly_chart(
        fig,
        use_container_width=True,
        config={"scrollZoom": True},
        )