# admin_dashboard/app.py

import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.database import fetch_all
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("📊 ResQRoute – Admin Analytics Dashboard")

# 🔢 Total Emergencies
emergencies = fetch_all("SELECT * FROM emergencies")
st.subheader("🧯 Total Emergency Requests: " + str(len(emergencies)))

# 📊 Emergency Type Distribution
type_count = {}
for e in emergencies:
    t = e['emergency_type']
    type_count[t] = type_count.get(t, 0) + 1

type_df = pd.DataFrame({"Type": list(type_count.keys()), "Count": list(type_count.values())})
st.markdown("### 🚨 Emergency Type Breakdown")
st.dataframe(type_df)

fig = px.pie(type_df, names='Type', values='Count', title='Emergency Type Distribution')
st.plotly_chart(fig)

# 🚘 Vehicles Summary
vehicles = fetch_all("SELECT * FROM vehicles")
total_vehicles = len(vehicles)
on_duty = sum(1 for v in vehicles if v['status'] == 'On duty')
available = sum(1 for v in vehicles if v['status'] == 'Available')

st.markdown("### 🚘 Vehicle Status Summary")
st.metric("Total Vehicles", total_vehicles)
st.metric("On Duty", on_duty)
st.metric("Available", available)

# ⏱️ (Optional) Average ETA
tasks = fetch_all("""
    SELECT assigned_at 
    FROM tasks
    WHERE assigned_at IS NOT NULL
""")


if tasks:
    import datetime
    total_time = 0
    count = 0
    for t in tasks:
        start = t['assigned_at']
        end = t.get('completed_at')
        if isinstance(start, datetime.datetime) and isinstance(end, datetime.datetime):
            diff = (end - start).total_seconds() / 60  # minutes
            total_time += diff
            count += 1
    avg_eta = round(total_time / count, 2) if count else "N/A"
    st.metric("⏱️ Avg. Response Time (ETA)", f"{avg_eta} min")
else:
    st.write("No completed tasks yet to calculate ETA.")

# 🗺️ Optional: Show live map here too
st.markdown("---")
st.subheader("🗺️ Live Emergency Signal Map")
from shared_components.live_map import show_live_map
show_live_map()
