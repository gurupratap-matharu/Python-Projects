import folium, pandas
import webbrowser

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="MapBox Control Room")

fg = folium.FeatureGroup("name=MyMap")

for lat, lon, elev in zip(lat, long, elev):
	fg.add_child(folium.Marker(location=[lat,long], popup = str(elev), icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map.html")
webbrowser.open("Map.html")
