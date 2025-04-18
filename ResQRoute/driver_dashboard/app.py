import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.database import fetch_all
from shared_components.live_map import show_live_map

st.set_page_config(page_title="Driver Dashboard", layout="wide")
st.title("🚓 ResQRoute – Driver Dashboard")

# Live Emergency Map
st.subheader("🗺️ Live Emergency Signal Map")
show_live_map()

# Assigned Tasks
st.subheader("📋 Assigned Emergency Tasks")

tasks = fetch_all("""
    SELECT t.id, t.driver_id, e.emergency_type, e.location_lat, e.location_lon, t.status
    FROM tasks t
    JOIN emergencies e ON t.emergency_id = e.id
    WHERE t.status = 'Assigned'
""")

if tasks:
    for task in tasks:
        st.write(f"🚨 Task ID: {task['id']}")
        st.write(f"Driver ID: {task['driver_id']} – Type: {task['emergency_type']}")
        st.write(f"Pickup Location: ({task['location_lat']}, {task['location_lon']})")
        st.write(f"Status: {task['status']}")
        st.markdown("---")
else:
    st.success("✅ No active emergency tasks assigned.")

