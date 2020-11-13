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

def color_from_elevation(elevation):
    """Returns a color based on elevation
    Keyword Arguments:
    elevation -- the elevation value
    """
    if elevation < 1000:
        return 'green'
    if 1000 <= elevation < 3000:
        return 'orange'

    return 'red'


my_map = folium.Map(location=[38.58, -99.09],
                    zoom_start=6,
                    tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Volcanos")

for lt, ln, el, name in zip(lat, lon, elev, name):
    popup_iframe = folium.IFrame(html=POPUP_HTML % (name, name, el),
                                 width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln],
									 color='grey',
									 fill=True,
									 fill_color=color_from_elevation(el),
									 fill_opacity=0.7,
                                	 popup=folium.Popup(popup_iframe)))
    # fg.add_child(folium.Marker(location=[lt, ln],
    #                            popup=folium.Popup(popup_iframe),
    #                            icon=folium.Icon(color=color_from_elevation(el))))


# world population
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open("world.json",
										   "r",
										   encoding="utf-8-sig").read()),
								style_function=lambda x: {
									'fillColor':'green' if x['properties']['POP2005'] < 10000000
									else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
									else 'red'}))

my_map.add_child(fg)
my_map.add_child(fgp)
# layer control
my_map.add_child(folium.LayerControl())
my_map.save("Map1.html")
