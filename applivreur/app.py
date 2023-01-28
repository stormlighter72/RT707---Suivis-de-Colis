#pip3 install folium

import folium
from folium import PolyLine

# Création de la carte
map = folium.Map(location=[48.85, 2.35], zoom_start=13)

# Liste des coordonnées pour tracer le chemin
coordinates = [[48.85, 2.35], [48.86, 2.36], [48.87, 2.37], [48.88, 2.38], [48.89, 2.39], [49.236275, 4.063538]]

# Tracer le chemin sur la carte
PolyLine(coordinates, color="red", weight=2.5, opacity=1).add_to(map)

# Ajout des marqueurs pour chaque coordonnée
for coord in coordinates:
    folium.Marker(location=coord, icon=folium.Icon(icon_url='')).add_to(map)

# Afficher la carte
map.save("chemin.html")
