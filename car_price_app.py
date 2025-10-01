import pandas as pd
import numpy as np
import joblib
import streamlit as st

st.title("🚗 Car Price Prediction App")

# Load The Dataset , Model and Scalar

dataset = pd.read_csv('cardekho_dataset.csv')
model = joblib.load('car_price_model.pkl')
encoder = joblib.load('car_price_prd_encoder.pkl')
scaler = joblib.load('car_price_prd_scaler.pkl')

# User Input

st.markdown("<h3><b>Brand</b></h3>", unsafe_allow_html=True)
brand = st.selectbox("Brand",dataset["brand"].unique(),label_visibility="collapsed")

st.markdown("<h3><b>Model</b></h3>", unsafe_allow_html=True)
car_model = st.selectbox("Model", dataset["model"].unique(),label_visibility="collapsed")

st.markdown("<h3><b>Vehicle Age</b></h3>", unsafe_allow_html=True)
vehicle_age = st.number_input("Vehicle Age",min_value=0 , max_value=40,label_visibility="collapsed")

st.markdown("<h3><b>KM Driven</b></h3>", unsafe_allow_html=True)
km_driven = st.number_input("KM Driven",min_value=100 , max_value=4000000 , step=100 , label_visibility="collapsed")

st.markdown("<h3><b>Seller Type</b></h3>", unsafe_allow_html=True)
seller_type	= st.radio("Seller Type",dataset["seller_type"].unique(),label_visibility="collapsed")

st.markdown("<h3><b>Fuel Type</b></h3>", unsafe_allow_html=True)
fuel_type = st.radio("Fuel Type",dataset["fuel_type"].unique(),label_visibility="collapsed")

st.markdown("<h3><b>Transmission Type</b></h3>", unsafe_allow_html=True)
transmission_type = st.radio("Transmission Type",dataset['transmission_type'].unique(), label_visibility="collapsed")

st.markdown("<h3><b>Mileage</b></h3>", unsafe_allow_html=True)
mileage = st.number_input("Mileage",min_value=0.0 , max_value=50.0 , step=0.1, label_visibility="collapsed")

st.markdown("<h3><b>Engine(CC)</b></h3>", unsafe_allow_html=True)
engine = st.number_input("Engine",min_value=500 , max_value=10000 , step=10 , label_visibility="collapsed")

st.markdown("<h3><b>Maximum Power (bhp)</b></h3>", unsafe_allow_html=True)
max_power = st.number_input("Maximum Power (bhp)",min_value=10 , max_value=500 , label_visibility="collapsed")

st.markdown("<h3><b>Seats</b></h3>", unsafe_allow_html=True)
seats = st.number_input("Seats",min_value=0 , max_value=10 , label_visibility="collapsed")

user_input = [[brand , car_model , vehicle_age , km_driven, seller_type , 
                fuel_type , transmission_type , mileage , engine , max_power , seats]]

columnss = ['brand', 'model', 'vehicle_age', 'km_driven', 'seller_type',
       'fuel_type', 'transmission_type', 'mileage', 'engine', 'max_power',
       'seats']

input_df = pd.DataFrame(user_input , columns=columnss)

cat_col = input_df.select_dtypes(include=['object']).columns
num_col = input_df.select_dtypes(include=['int64','float64']).columns

# Encoding

enc = encoder.transform(input_df[cat_col])
enc_df = pd.DataFrame(enc , columns=cat_col , index=input_df.index)

final_input = pd.concat([input_df.drop(columns=cat_col , axis=1),enc_df],axis=1)

# Scaling

final_input[num_col] = scaler.transform(final_input[num_col])

if st.button("Predict price"):
    prediction = model.predict(final_input)
    st.success(f"Estimated Price {prediction[0]:.3f}₹")





