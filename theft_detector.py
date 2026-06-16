def detect_theft(is_outside_zone, speed, ignition):

    if is_outside_zone:
        return True
    if speed > 0 and not ignition:
        return True
    
    return False

def get_simulated_location():
    # Simulated location and vehicle state values
    latitude = 0.0
    longitude = 0.0
    speed = 0
    ignition = False
    return latitude, longitude, speed, ignition

lat, lon, speed, ignition = get_simulated_location()

print(f"Latitude: {lat}")
print(f"Longitude: {lon}")
print(f"Speed: {speed}")
print(f"Ignition: {ignition}")
   # if speed > 0 and not ignition:
     #   return True

    #return False