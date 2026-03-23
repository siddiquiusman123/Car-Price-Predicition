import pandas as pd
import joblib
import streamlit as st

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

st.title("🚗 Car Price Prediction App")

# Load Cleaned Data

@st.cache_data
def load_data():
    return pd.read_csv('Cleaned_data.csv')

dataset = load_data()

# Laod Pipeline

@st.cache_resource
def load_model():
    return joblib.load('car_price_pipeline.joblib')

model = load_model()

# User Input

st.subheader("Enter Car Details")

brand = st.selectbox("Brand", sorted(dataset["brand"].unique()))
filtered_models = dataset[dataset["brand"] == brand]["model"].unique()
car_model = st.selectbox("Model", sorted(filtered_models))
vehicle_age = st.number_input("Vehicle Age", min_value=0, max_value=40)
km_driven = st.number_input("KM Driven", min_value=100, max_value=1000000, step=100)
seller_type = st.selectbox("Seller Type", dataset["seller_type"].unique())
fuel_type = st.selectbox("Fuel Type", dataset["fuel_type"].unique())
transmission_type = st.selectbox("Transmission Type", dataset["transmission_type"].unique())
mileage = st.number_input("Mileage", min_value=0.0, max_value=50.0, step=0.1)
engine = st.number_input("Engine (CC)", min_value=300, max_value=10000, step=10)
max_power = st.number_input("Max Power (bhp)", min_value=10, max_value=500)
seats = st.number_input("Seats", min_value=1, max_value=10)

# Create Imput DataFrame

input_df = pd.DataFrame([{
    'brand': brand,
    'model': car_model,
    'vehicle_age': vehicle_age,
    'km_driven': km_driven,
    'seller_type': seller_type,
    'fuel_type': fuel_type,
    'transmission_type': transmission_type,
    'mileage': mileage,
    'engine': engine,
    'max_power': max_power,
    'seats': seats
}])

# Prediction

if st.button("Predict Price"):

    try:
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Price: ₹ {round(prediction, 2):,}")
    
    except Exception as e:
        st.error("⚠️ Error in prediction. Please check inputs.")
        st.text(str(e))