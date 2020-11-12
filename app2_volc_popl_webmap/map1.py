"""
Create a map html with the help of folium.
"""
import folium
import pandas as pd

volcanos_df = pd.read_csv("Volcanoes.txt")
lat = list(volcanos_df["LAT"])
lon = list(volcanos_df["LON"])
elev = list(volcanos_df["ELEV"])
name = list(volcanos_df["NAME"])

POPUP_HTML = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""


my_map = folium.Map(location=[38.58, -99.09],
                    zoom_start=6,
                    tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Volcanos")

for lt, ln, el, name in zip(lat, lon, elev, name):
    popup_iframe = folium.IFrame(html=POPUP_HTML % (name, name, el),
                                 width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln],
                               popup=folium.Popup(popup_iframe),
                               icon=folium.Icon(color="green")))

my_map.add_child(fg)
my_map.save("Map1.html")
