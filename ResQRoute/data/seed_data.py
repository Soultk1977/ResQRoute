import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.database import execute_query


# 1. Insert emergency vehicles
vehicles = [
    ("AMB001", "Ambulance", "Available", 28.6448, 77.2167),
    ("FIRE002", "Fire", "Available", 28.6542, 77.2024),
    ("POL003", "Police", "Available", 28.6304, 77.2188)
]

for v in vehicles:
    execute_query("""
        INSERT INTO vehicles (vehicle_id, vehicle_type, status, location_lat, location_lon)
        VALUES (%s, %s, %s, %s, %s)
    """, v)

# 2. Insert drivers
drivers = [
    ("Ajay Sharma", 1),
    ("Sunita Mehra", 2),
    ("Rakesh Kumar", 3)
]

for d in drivers:
    execute_query("""
        INSERT INTO drivers (name, vehicle_id)
        VALUES (%s, %s)
    """, d)

# 3. Insert signal points
signals = [
    ("SG101", 28.6440, 77.2150, "RED", 60, 5, 55),
    ("SG102", 28.6500, 77.2100, "GREEN", 60, 5, 55),
    ("SG103", 28.6480, 77.2200, "YELLOW", 60, 5, 55)
]

for s in signals:
    execute_query("""
        INSERT INTO signals (signal_code, location_lat, location_lon, current_state, green_duration, yellow_duration, red_duration)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, s)

print("✅ Sample data inserted successfully.")
