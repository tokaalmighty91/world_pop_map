import folium
import pandas

data=pandas.read_csv('Volcanoes_USA.txt')
df=data.loc[:,'LAT':'LON']
coord_lst=df.values.tolist()
#name_lst=data['NAME']
elev=data['ELEV']

#color code by elevation, to be used in for look later
def elev_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

#create map object
#Map is the class created the object. help(folium.Map), q to exit help
map=folium.Map(location=[36.519228, -121.940464],zoom_start=8)

fgv=folium.FeatureGroup(name='Vocanoes')

for coordinates,el in zip(coord_lst,elev):
#popup=folium.Popup(pop,parse_html=True) to avoid strings with " ' " in it
    #fg.add_child(folium.CircleMarker(location=coordinates,popup=str(el),
    #icon=folium.Icon(color=elev_color(el))))
    fgv.add_child(folium.CircleMarker(location=coordinates,radius=3,fill=True,
    fill_opacity=0.7,popup=str(el),color=elev_color(el)))

fgp=folium.FeatureGroup(name='Population')

#open is method for creating file object. Add decoding method based on error message
# .read()methods turns a file into a string
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
#change the color of polygon background
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save('Map1.html')
