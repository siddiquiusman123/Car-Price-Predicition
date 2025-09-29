# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Load trained model and encoder
# model = joblib.load("car_price_model.pkl")
# encoder = joblib.load("encoder.pkl")

# st.title("🚗 Car Price Prediction App")

# # Load dataset only to extract options
# dataset = pd.read_csv(r"C:\Users\siddi\Downloads\Car Dataset.csv")

# # User inputs
# car_name = st.selectbox("Car Name", dataset['name'].unique())
# km_driven = st.number_input("Kilometers Driven", min_value=0, value=10000)
# fuel = st.selectbox("Fuel Type", dataset['fuel'].unique())
# seller_type = st.selectbox("Seller Type", dataset['seller_type'].unique())
# transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
# owner = st.selectbox("Number of Previous Owners", dataset['owner'].unique())
# car_age = st.slider("Car Age (in years)", 0, 30, 5)

# # Encode the categorical values using loaded encoder
# categorical_input = [[car_name, fuel, seller_type, transmission, owner]]
# encoded_input = encoder.transform(categorical_input)[0]

# # Combine with numerical inputs
# input_data = np.array([[encoded_input[0],  # car_name
#                         km_driven,
#                         encoded_input[1],  # fuel
#                         encoded_input[2],  # seller_type
#                         encoded_input[3],  # transmission
#                         encoded_input[4],  # owner
#                         car_age]])

# # Predict button
# if st.button("Predict Price"):
#     prediction = model.predict(input_data)
#     st.success(f"Estimated Price: ₹ {round(prediction[0], 2)} lakh")


for i in range(100,1000,100):
    print(i)