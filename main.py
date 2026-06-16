from datetime import datetime
import time

from gps_simulator import get_simulated_location
from geofence import check_geofence
from theft_detector import detect_theft
from logger import save_log

print("=" * 60)
print("🚗 IoT Vehicle Tracking & Theft Prevention System")
print("=" * 60)

while True:

    # Get simulated vehicle data
    lat, lon, speed, ignition, mode = get_simulated_location()

    # Geofence check
    outside = check_geofence(
        lat,
        lon
    )

    # Theft detection
    theft = detect_theft(
        outside,
        speed,
        ignition
    )

    # Default values
    status = "MOVING"
    alert = "NONE"

    # --------------------------
    # Vehicle State Logic
    # --------------------------

    if mode == "PARKED":

        status = "PARKED"
        alert = "NONE"

    elif mode == "OVERSPEED":

        status = "MOVING"
        alert = "OVERSPEED"

    elif mode == "GEOFENCE":

        status = "OUTSIDE_ZONE"
        alert = "GEOFENCE_ALERT"

    elif mode == "THEFT":

        status = "THEFT"
        alert = "VEHICLE_THEFT"

    # --------------------------
    # Google Maps URL
    # --------------------------

    maps_url = f"https://maps.google.com/?q={lat},{lon}"

    # --------------------------
    # Alerts

    if alert == "VEHICLE_THEFT":

        print("\n🚨 VEHICLE THEFT DETECTED")
        print("🚨 BUZZER ON")
        print("🚨 ENGINE LOCK ACTIVATED")

    elif alert == "GEOFENCE_ALERT":

        print("\n⚠ VEHICLE LEFT SAFE ZONE")

    elif alert == "OVERSPEED":
        print("\n⚠ OVERSPEED DETECTED")

    # --------------------------
    # Log Record
    record = {

        "Timestamp": datetime.now(),

        "Latitude": lat,
        "Longitude": lon,

        "Speed": speed,
        "Ignition": ignition,

        "Mode": mode,

        "Status": status,
        "Alert": alert,

        "Maps": maps_url
    }

    save_log(record)
    # Terminal Output

    print("\n" + "=" * 60)

    print(
        f"""
🚗 VEHICLE TELEMATICS DATA

Time      : {datetime.now()}
Mode      : {mode}
Latitude  : {lat:.6f}
Longitude : {lon:.6f}

Speed     : {speed} km/h
Ignition  : {ignition}
Status    : {status}
Alert     : {alert}
Maps Link :
{maps_url}
"""  )
    print("=" * 60)
    time.sleep(5)