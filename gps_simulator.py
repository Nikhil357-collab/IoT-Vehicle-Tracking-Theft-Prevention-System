import random
import time

SAFE_LAT = 21.1458
SAFE_LON = 79.0882

start_time = time.time()

def get_simulated_location():

    elapsed = int(time.time() - start_time)

    # NORMAL : 0-30 sec
    if elapsed < 30:

        mode = "NORMAL"

        lat = SAFE_LAT + random.uniform(-0.002, 0.002)
        lon = SAFE_LON + random.uniform(-0.002, 0.002)

        speed = random.randint(30, 60)
        ignition = True

    # PARKED : 30-50 sec
    elif elapsed < 50:

        mode = "PARKED"

        lat = SAFE_LAT
        lon = SAFE_LON

        speed = 0
        ignition = False

    # OVERSPEED : 50-70 sec
    elif elapsed < 70:

        mode = "OVERSPEED"

        lat = SAFE_LAT + random.uniform(-0.003, 0.003)
        lon = SAFE_LON + random.uniform(-0.003, 0.003)

        speed = random.randint(90, 120)
        ignition = True

    # GEOFENCE : 70-90 sec
    elif elapsed < 90:

        mode = "GEOFENCE"

        lat = SAFE_LAT + 0.02
        lon = SAFE_LON + 0.02

        speed = random.randint(30, 50)
        ignition = True

    # THEFT : 90-110 sec
    elif elapsed < 110:

        mode = "THEFT"

        lat = SAFE_LAT + 0.03
        lon = SAFE_LON + 0.03

        speed = random.randint(15, 40)
        ignition = False

  
    return lat, lon, speed, ignition, mode