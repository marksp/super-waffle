import geopy
from geopy.distance import VincentyDistance

lat1 = 50.884838252797664
lon1 = 1.3033153909889132
b = 270
d = 2.81

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers

origin = geopy.Point(lat1, lon1)
destination = VincentyDistance(kilometers=d).destination(origin, b)

lat2, lon2 = destination.latitude, destination.longitude

print(lat2, lon2)