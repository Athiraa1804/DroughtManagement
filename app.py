# climate_guard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="🌍 ClimateGuard", layout="wide")

# -------------------------------
# Custom Background Theme
# -------------------------------
page_bg = """
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {
    background-color:#5E8BFF;  /* powder blue background */
    color: white;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #191970;  /* Darker navy */
    color: white;
}

/* Header */
[data-testid="stHeader"] {
    background-color: #1E90FF;  /* Slightly lighter header */
}

/* Widgets styling */
[data-testid="stMarkdown"] {
    color: white;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -------------------------------
# App Title
# -------------------------------
st.title("🌍 ClimateGuard: AI-Powered Climate Risk Management")
st.markdown("A simple web app for **monitoring climate risks, predicting temperature, and drought risk alerting**.")

# -------------------------------
# Sidebar Navigation
# -------------------------------
menu = st.sidebar.radio("📌 Navigate", ["Dashboard", "Risk Prediction", "About"])

# -------------------------------
# Dashboard
# -------------------------------
if menu == "Dashboard":
    st.header("📊 Climate Dashboard")

    # Dummy dataset (with Drought Index instead of Rainfall)
    data = {
        "Region": ["Kerala", "Rajasthan", "Delhi", "Tamil Nadu", "Punjab"],
        "Temperature (°C)": [29, 40, 37, 33, 28],
        "Humidity (%)": [80, 30, 45, 60, 50],
        "Drought Index": [10, 85, 65, 50, 30],   # 🌵 Higher = more drought stress
        "Risk Level": ["Low", "High", "Medium", "Medium", "Low"]
    }
    df = pd.DataFrame(data)

    st.subheader("🌍 Regional Climate Data")
    st.dataframe(df)

    # Visualization
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌡️ Temperature by Region")
        fig, ax = plt.subplots()
        ax.bar(df["Region"], df["Temperature (°C)"], color="orange")
        ax.set_ylabel("Temperature (°C)")
        st.pyplot(fig)

    with col2:
        st.subheader("🌵 Drought Index by Region")
        fig, ax = plt.subplots()
        ax.plot(df["Region"], df["Drought Index"], marker="o", color="brown")
        ax.set_ylabel("Drought Index (0 = Safe, 100 = Extreme)")
        st.pyplot(fig)

# -------------------------------
# Risk Prediction Tab
# -------------------------------
elif menu == "Risk Prediction":
    st.header("🌡️ Climate Risk Prediction")

    # User Inputs
    location = st.text_input("Enter Location")
    temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, step=0.5)
    humidity = st.slider("Humidity (%)", 0, 100, 50)
    drought_index = st.slider("Drought Index (0 = Safe, 100 = Extreme)", 0, 100, 30)

    if st.button("🔍 Predict Risk"):
        # Simple rule-based risk prediction
        if temp > 38 and humidity < 35 and drought_index > 70:
            risk = "🔥 High Risk (Severe Heatwave/Drought)"
        elif drought_index > 50 or temp > 32:
            risk = "⚠️ Medium Risk"
        else:
            risk = "✅ Low Risk"

        st.success(f"📍 Location: {location if location else 'N/A'}")
        st.warning(f"🌍 Predicted Climate Risk: **{risk}**")

# -------------------------------
# About Tab
# -------------------------------
elif menu == "About":
    st.header("ℹ️ About ClimateGuard")
    st.markdown("""
    ClimateGuard is a simple AI-powered system for **climate risk monitoring**.  
    Features:  
    - 📊 Dashboard for climate data visualization  
    - 🌡️ Enter details to predict **heat & drought risk levels**  
    - 🚨 Risk alerts (Low / Medium / High)  
    - 🛰️ Potential integration with satellite & historical climate datasets  
    """)

    st.info("Developed as part of the **ClimateGuard Project** 🌍")
