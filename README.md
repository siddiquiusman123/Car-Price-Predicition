# 🚗 Car Price Prediction | End-to-End Machine Learning Project

> 💡 Predict the resale price of used cars using a production-ready Machine Learning pipeline with real-time deployment.

---

## 🚀 Live Demo

👉 Try the app here:  
🔗 https://car-price-predicition-spmjq8bptwqufza7xfy2wc.streamlit.app/

---

## 🧠 Project Overview

This project demonstrates a complete end-to-end Machine Learning workflow, from raw data preprocessing to deployment.

It is designed to simulate a real-world ML system, where users can input car details and receive instant price predictions through an intuitive web interface.

---

## ✨ Key Highlights

- 🔥 End-to-End ML Pipeline (Production Style)  
- ⚙️ Integrated Data Preprocessing + Model Training  
- 🧩 Used ColumnTransformer + Pipeline  
- 📊 Compared Multiple Models (Linear Regression, Random Forest, XGBoost)  
- 🎯 Optimized for better prediction accuracy  
- 🌐 Deployed using Streamlit Cloud  
- ⚡ Real-time predictions via interactive UI  

---

## ⚙️ Machine Learning Pipeline Architecture

```mermaid
flowchart LR
    A[Raw Data] --> B[Data Cleaning]
    B --> C[Feature Engineering]
    C --> D[Encoding + Scaling]
    D --> E[Model Training]
    E --> F[Pipeline Creation]
    F --> G[Model Serialization (Joblib)]
    G --> H[Streamlit Deployment]
