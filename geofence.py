import math
from config import SAFE_LAT, SAFE_LON, GEOFENCE_RADIUS_KM

def calculate_distance(lat1, lon1, lat2, lon2):

    return math.sqrt(
        (lat1-lat2)**2 +
        (lon1-lon2)**2
    ) * 111

def check_geofence(lat, lon):

    distance = calculate_distance(
        lat,
        lon,
        SAFE_LAT,
        SAFE_LON
    )

    return distance > GEOFENCE_RADIUS_KM