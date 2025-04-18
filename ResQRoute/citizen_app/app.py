# citizen_app/app.py

import streamlit as st
import sys, os
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.database import execute_query, fetch_all

st.set_page_config(page_title="Citizen Emergency App", layout="centered")
st.title("🚨 ResQRoute – Citizen Emergency Request")

st.markdown("Report your emergency and get real-time alerts if help is nearby.")

# 📍 Step 1: Enter your current location manually
lat = st.number_input("Your Latitude", value=28.6448, format="%.6f")
lon = st.number_input("Your Longitude", value=77.2167, format="%.6f")

# 🆘 Step 2: Choose type of emergency
emergency_type = st.selectbox("Type of Emergency", ["Ambulance", "Fire", "Police"])

# 📝 Step 3: Additional details (optional)
notes = st.text_area("Any additional notes (optional)")

# 🚨 Step 4: Submit button
if st.button("Submit Emergency Request"):
    execute_query("""
        INSERT INTO emergencies (emergency_type, location_lat, location_lon, status, requested_vehicle)
        VALUES (%s, %s, %s, 'Pending', %s)
    """, (emergency_type, lat, lon, emergency_type))

    st.success("🚨 Your emergency request has been submitted!")
    st.balloons()

# 🛻 Step 5: Check if any emergency vehicle is nearby (within ~2km)
st.markdown("---")
st.header("👀 Live Emergency Vehicle Alert")

# Use Haversine formula manually for now
def haversine(lat1, lon1, lat2, lon2):
    from math import radians, cos, sin, asin, sqrt
    R = 6371  # Earth radius in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return R * c

vehicles = fetch_all("SELECT vehicle_id, vehicle_type, location_lat, location_lon FROM vehicles WHERE status = 'On duty'")

alert_shown = False
for v in vehicles:
    distance = haversine(lat, lon, v['location_lat'], v['location_lon'])
    if distance <= 2:
        st.warning(f"🚨 {v['vehicle_type']} ({v['vehicle_id']}) is within {distance:.2f} km of you!")
        alert_shown = True

if not alert_shown:
    st.success("✅ No emergency vehicles nearby currently.")

# 🗺️ Show Live Map of Signals and Emergency Vehicles
st.markdown("---")
st.subheader("🗺️ Live Emergency Signal Map")

from shared_components.live_map import show_live_map
show_live_map()

