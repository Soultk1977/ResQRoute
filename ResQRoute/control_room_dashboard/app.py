# control_room_dashboard/app.py

import sys
import os

# Ensure project root is on path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.database import fetch_all, execute_query

st.set_page_config(page_title="Control Room Dashboard", layout="wide")
st.title("🏢 ResQRoute — Control Room Dashboard")

# 1. Show all pending emergencies
st.header("Pending Emergency Requests")
emergencies = fetch_all("SELECT * FROM emergencies WHERE status = 'Pending'")
if emergencies:
    for e in emergencies:
        st.write(f"- ID: {e['id']} | Type: {e['emergency_type']} | Location: ({e['location_lat']}, {e['location_lon']})")
else:
    st.write("No pending emergencies.")

st.markdown("---")

# 2. Override Traffic Signal
st.header("Signal Override Control")
# Load signals
signals = fetch_all("SELECT id, signal_code, current_state FROM signals")
signal_map = {f"{s['signal_code']} (#{s['id']})": s['id'] for s in signals}
choice = st.selectbox("Select Signal to Override", list(signal_map.keys()))
new_state = st.selectbox("New State", ["GREEN", "YELLOW", "RED"])

if st.button("Override Signal"):
    sig_id = signal_map[choice]
    execute_query("UPDATE signals SET current_state = %s, last_override = NOW() WHERE id = %s", (new_state, sig_id))
    execute_query("""
        INSERT INTO signal_logs (signal_id, new_state, overridden_by) 
        VALUES (%s, %s, %s)
    """, (sig_id, new_state, "ControlRoomUser"))
    st.success(f"Signal {choice} overridden to {new_state}.")

st.markdown("---")

# 👇 Live Map Section
st.markdown("---")
st.subheader("🗺️ Live Emergency Signal Map")

from shared_components.live_map import show_live_map
show_live_map()


# 3. Manually assign an emergency (optional)
st.header("Manual Emergency Assignment")
em_id2 = st.text_input("Emergency ID:", "")
if st.button("Assign Now"):
    if em_id2.isdigit():
        from backend.emergency_logic import assign_vehicle_to_emergency
        msg = assign_vehicle_to_emergency(int(em_id2))
        st.write(msg)
    else:
        st.error("Enter a valid Emergency ID.")
