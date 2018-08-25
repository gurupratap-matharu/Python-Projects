import folium, pandas
import webbrowser

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="MapBox Control Room")

fg = folium.FeatureGroup("name=MyMap")

for lat, lon, elev in zip(lat, long, elev):
	fg.add_child(folium.Marker(location=[lat,long], popup = str(elev), icon=folium.Icon(color="green")))
	# print(lat, long, elev)
map.add_child(fg)

map.save("Map1.html")
webbrowser.open("Map1.html")
