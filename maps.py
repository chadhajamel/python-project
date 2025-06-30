import pandas as pd
import streamlit as st
import pydeck as pdk
coordinates =pd.DataFrame({
    'lat':[51.509865,40.730610],
    'lon':[-0.118092,-73.935242]
})
st.write(coordinates)
st.map(coordinates)
def from_data_file(filename: str) -> pd.DataFrame:
    url = (
        "https://raw.githubusercontent.com/streamlit/"
        f"example-data/master/hello/v1/{filename}"
    )
    return pd.read_json(url)
layer = pdk.Layer(
    "TextLayer",
    data=from_data_file("bart_stop_stats.json"),
    get_position=["lon", "lat"],
    get_text="name",
    get_color=[0, 0, 0, 200],
    get_size=10,
    get_alignment_baseline="'bottom'",
)
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state={
            "latitude": 37.76,
            "longitude": -122.4,
            "zoom": 11,
            "pitch": 50,
        },
        layers=[layer],
    )
)