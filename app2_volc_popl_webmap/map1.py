"""
Create a map html with the help of folium.
"""
import folium as flm
import pandas as pd


class ColorRange:
    """Grades colors based on a lower and upper value
    """
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.l_color = 'green'
        self.m_color = 'orange'
        self.h_color = 'red'

    def get_color(self, value):
        """Returns a color based on value
        Keyword Arguments:
        value -- the elevation value
        Returns:
        string -- a color name
        """
        # print(value)
        if value < self.low:
            return self.l_color
        if self.low <= value <= self.high:
            return self.m_color
        return self.h_color


def generate_volcanos_feature(volcanos_df):
    """ Generate a folium feature group for volcanoes
    Keyword Arguments:
    volcanos_df -- pandas dataframe consisting of the volcano info.
    """
    lat = list(volcanos_df["LAT"])
    lon = list(volcanos_df["LON"])
    elev = list(volcanos_df["ELEV"])
    name = list(volcanos_df["NAME"])

    popup_html = """
    Volcano name:<br>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
    Height: %s m
    """

    feature_group = flm.FeatureGroup(name="Volcanos")
    clr_grdr = ColorRange(1000, 3000)
    for lt, ln, el, name in zip(lat, lon, elev, name):
        popup_iframe = flm.IFrame(html=popup_html % (name, name, el),
                                  width=200, height=100)
        feature_group.add_child(flm.CircleMarker(location=[lt, ln],
                                color='grey',
                                fill=True,
                                fill_color=clr_grdr.get_color(el),
                                fill_opacity=0.7,
                                popup=flm.Popup(popup_iframe)))
        # feature_group.add_child(flm.Marker(location=[lt, ln],
        #                            popup=flm.Popup(popup_iframe),
        #                            icon=flm.Icon(color=color_from_elevation(el))))

    return feature_group


def generate_population_feature():
    """ Generate World Population Feature Group"""
    clr_grdr1 = ColorRange(10000000, 20000000)
    fgp = flm.FeatureGroup(name="Population")
    fgp.add_child(flm.GeoJson(data=(open("world.json",
                                         "r",
                                         encoding="utf-8-sig").read()),
                              style_function=lambda x: {
                                  'fillColor':clr_grdr1.get_color(
                                      x['properties']['POP2005'])}))

    return fgp


def main():
    """ Generate volcano and population feature map """
    vlcn_df = pd.read_csv("Volcanoes.txt")
    my_map = flm.Map(location=[38.58, -99.09],
                     zoom_start=6,
                     tiles="Stamen Terrain")
    my_map.add_child(generate_volcanos_feature(vlcn_df))
    my_map.add_child(generate_population_feature())
    # layer control
    my_map.add_child(flm.LayerControl())
    my_map.save("Map1.html")


if __name__ == '__main__':
    main()
