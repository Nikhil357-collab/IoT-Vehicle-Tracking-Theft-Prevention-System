import streamlit as st
import pandas as pd
import os
from streamlit_autorefresh import st_autorefresh

st_autorefresh(
    interval=5000,   # 5 seconds
    key="vehicle_dashboard"
)
# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Smart Vehicle Tracking System",
    page_icon="🚗",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 1rem;
}

[data-testid="stMetric"] {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #333;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD DATA
# ==========================================

CSV_FILE = "data/vehicle_log.csv"

if not os.path.exists(CSV_FILE):
    st.error("vehicle_log.csv not found")
    st.stop()

df = pd.read_csv(CSV_FILE)

latest = df.iloc[-1]

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🚗 Vehicle Security")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Security Center",
        "Analytics",
        "Vehicle Logs",
        "System Info"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    f"Current Mode: {latest['Mode']}"
)

st.sidebar.info(
    f"Current Alert: {latest['Alert']}"
)

# ==========================================
# DASHBOARD PAGE
# ==========================================

if page == "Dashboard":

    st.title("🚗 IoT Vehicle Tracking & Theft Prevention")

    st.markdown(
        "Real-Time Vehicle Monitoring Dashboard"
    )

    # KPI CARDS

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Status",
        latest["Status"]
    )

    c2.metric(
        "Speed",
        f"{latest['Speed']} km/h"
    )

    c3.metric(
        "Ignition",
        str(latest["Ignition"])
    )

    c4.metric(
        "Alert",
        latest["Alert"]
    )

    c5.metric(
        "Mode",
        latest["Mode"]
    )

    st.divider()

    # LOCATION INFO

    col1, col2, col3 = st.columns(3)

    col1.info(
        f"📍 Latitude: {latest['Latitude']:.6f}"
    )

    col2.info(
        f"📍 Longitude: {latest['Longitude']:.6f}"
    )

    col3.link_button(
        "🌍 Open Google Maps",
        latest["Maps"]
    )

    st.divider()

    # MAP

    st.subheader("🗺 Live Vehicle Route")

    st.map(
        df[["Latitude", "Longitude"]]
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("📈 Speed Trend")

        st.line_chart(
            df["Speed"]
        )

    with right:

        st.subheader("🚨 Alert Distribution")

        st.bar_chart(
            df["Alert"].value_counts()
        )

# ==========================================
# SECURITY CENTER
# ==========================================

elif page == "Security Center":

    st.title("🔒 Vehicle Security Center")

    if latest["Alert"] == "VEHICLE_THEFT":

        st.error(
            "🚨 VEHICLE THEFT DETECTED"
        )

        st.error(
            "🔊 Buzzer Activated"
        )

        st.error(
            "🔒 Engine Lock Activated"
        )

    elif latest["Alert"] == "GEOFENCE_ALERT":

        st.warning(
            "⚠ Vehicle Outside Safe Zone"
        )

    elif latest["Alert"] == "OVERSPEED":

        st.warning(
            "⚠ Overspeed Detected"
        )

    else:

        st.success(
            "✅ Vehicle Secure"
        )

    st.divider()

    st.subheader("Security Recommendations")

    st.write(
        """
        - Enable Engine Lock
        - Verify Vehicle Location
        - Notify Owner
        - Notify Fleet Manager
        - Check Vehicle Route History
        """
    )

# ==========================================
# ANALYTICS
# ==========================================
elif page == "Analytics":

    st.title("📊 Fleet Analytics")

    total_records = len(df)

    theft_count = (
        df["Alert"] == "VEHICLE_THEFT"
    ).sum()

    geofence_count = (
        df["Alert"] == "GEOFENCE_ALERT"
    ).sum()

    overspeed_count = (
        df["Alert"] == "OVERSPEED"
    ).sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Records",
        total_records
    )

    col2.metric(
        "Theft Events",
        theft_count
    )

    col3.metric(
        "Geofence Alerts",
        geofence_count
    )

    col4.metric(
        "Overspeed Events",
        overspeed_count
    )

    st.divider()

    st.subheader("Mode Distribution")

    st.bar_chart(
        df["Mode"].value_counts()
    )

    st.subheader("Alert Distribution")

    st.bar_chart(
        df["Alert"].value_counts()
    )

    st.subheader("Speed Trend")

    st.line_chart(
        df["Speed"]
    )

# ==========================================
# VEHICLE LOGS
# ==========================================


elif page == "Vehicle Logs":

    st.title("📋 Vehicle Logs")

    st.dataframe(
        df.tail(100),
        use_container_width=True
    )

    st.download_button(
        "⬇ Download CSV",
        data=df.to_csv(index=False),
        file_name="vehicle_log.csv",
        mime="text/csv"
    )

    map_df = df.rename(
        columns={
            "Latitude": "latitude",
            "Longitude": "longitude"
        }
    )

    st.map(
        map_df
    )
# ==========================================
# SYSTEM INFO
# ==========================================

elif page == "System Info":

    st.title("⚙ System Information")

    st.write(
        """
        ### Project Name
        IoT Vehicle Tracking & Theft Prevention System

        ### Features

        - GPS Tracking
        - Geofence Monitoring
        - Theft Detection
        - Overspeed Detection
        - Engine Lock Simulation
        - Buzzer Simulation
        - Cloud Ready Architecture
        - Streamlit Dashboard

        ### Future Hardware Integration

        - ESP32
        - NEO-6M GPS
        - Relay Module
        - Buzzer
        - GSM Module
        - MQTT
        - 
        """
    )

    st.success(
        "Industry-Oriented Vehicle Telematics Platform"
    )