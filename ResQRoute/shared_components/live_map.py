# shared_components/live_map.py

import folium
from streamlit_folium import st_folium
from backend.database import fetch_all

def show_live_map():
    m = folium.Map(location=[28.61, 77.23], zoom_start=13)

    # 🚦 Signals
    signals = fetch_all("SELECT * FROM signals")
    for s in signals:
        state_color = {
            "RED": "red",
            "GREEN": "green",
            "YELLOW": "orange"
        }.get(s["current_state"], "gray")

        folium.Marker(
            location=[s["location_lat"], s["location_lon"]],
            popup=f"Signal: {s['signal_code']} ({s['current_state']})",
            icon=folium.Icon(color=state_color, icon="traffic-light", prefix="fa")
        ).add_to(m)

    # 🚑 Vehicles
    vehicles = fetch_all("SELECT * FROM vehicles")
    for v in vehicles:
        icon_color = {
            "Ambulance": "blue",
            "Fire": "orange",
            "Police": "black"
        }.get(v["vehicle_type"], "gray")

        folium.Marker(
            location=[v["location_lat"], v["location_lon"]],
            popup=f"{v['vehicle_type']} ({v['vehicle_id']}) - {v['status']}",
            icon=folium.Icon(color=icon_color, icon="ambulance", prefix="fa")
        ).add_to(m)

    # 📍 Emergency destination
    assigned = fetch_all("""
        SELECT e.location_lat, e.location_lon, e.emergency_type
        FROM tasks t JOIN emergencies e ON t.emergency_id = e.id
        WHERE t.status = 'Assigned' LIMIT 1
    """)
    if assigned:
        d = assigned[0]
        folium.Marker(
            location=[d["location_lat"], d["location_lon"]],
            popup=f"📍 Destination ({d['emergency_type']})",
            icon=folium.Icon(color="purple", icon="flag", prefix="fa")
        ).add_to(m)

    return st_folium(m, width=1100, height=600)
