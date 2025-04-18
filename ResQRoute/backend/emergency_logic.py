# backend/emergency_logic.py

from backend.database import fetch_all, execute_query

def assign_vehicle_to_emergency(emergency_id):
    """
    Assigns the nearest available vehicle of the requested type to the given emergency.
    Updates vehicle status and creates a task.
    """
    # 1. Fetch emergency
    em = fetch_all("SELECT * FROM emergencies WHERE id = %s", (emergency_id,))
    if not em:
        return f"[ERROR] Emergency {emergency_id} not found."
    emergency = em[0]
    vehicle_type = emergency['requested_vehicle']

    # 2. Find one available vehicle of that type
    vehicles = fetch_all("""
        SELECT * FROM vehicles 
        WHERE vehicle_type = %s AND status = 'Available'
        ORDER BY ABS(location_lat - %s) + ABS(location_lon - %s) LIMIT 1
    """, (vehicle_type, emergency['location_lat'], emergency['location_lon']))
    if not vehicles:
        return "[ERROR] No available vehicle found."

    vehicle = vehicles[0]
    vid = vehicle['id']

    # 3. Mark vehicle as on duty
    execute_query("UPDATE vehicles SET status = 'On duty' WHERE id = %s", (vid,))

    # 4. Find driver for that vehicle
    drv = fetch_all("SELECT id FROM drivers WHERE vehicle_id = %s", (vid,))
    if not drv:
        return f"[ERROR] No driver assigned to vehicle {vid}."
    driver_id = drv[0]['id']

    # 5. Create task
    execute_query("""
        INSERT INTO tasks (emergency_id, driver_id, status) 
        VALUES (%s, %s, 'Assigned')
    """, (emergency_id, driver_id))

    return f"✅ Emergency {emergency_id} assigned to vehicle {vehicle['vehicle_id']} (Driver ID {driver_id})."
