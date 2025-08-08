
import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load('acc_rf.pkl')

st.title("🚦 Ghana Road Accident Severity Predictor")

st.markdown("Select the conditions below to predict the likely accident severity.")

regions = [
    "Greater Accra", "Ashanti", "Central", "Western", "Eastern", "Volta",
    "Upper East", "Upper West", "Northern", "North East", "Savannah",
    "Bono", "Bono East", "Ahafo", "Western North", "Oti"
]

# Form fields using exact column names from your dataset
Region = st.selectbox("Region", regions)
DayOfWeek = st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
TimeOfDay = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
Weather = st.selectbox("Weather Conditions", ["Clear", "Rainy", "Fog", "Cloudy", "Windy"])
RoadType = st.selectbox("Road Type", ["Highway", "Urban", "Rural", "Gravel", "Bridge"])
VehicleType = st.selectbox("Vehicle Type", ["Private", "Commercial", "Truck", "Motorcycle", "Bus", "Taxi"])

# Predict button
if st.button("Predict Severity"):
    input_data = pd.DataFrame([{
        "Region": Region,
        "DayOfWeek": DayOfWeek,
        "TimeOfDay": TimeOfDay,
        "Weather conditions": Weather,
        "Road type": RoadType,
        "VehicleType": VehicleType
    }])

    prediction = model.predict(input_data)[0]

    severity_map = {0: "Minor", 1: "Serious", 2: "Fatal"}
    result = severity_map.get(prediction, "Unknown")

    st.success(f"🔮 Predicted Severity: **{result}**")