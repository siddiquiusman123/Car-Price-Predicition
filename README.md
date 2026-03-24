# 🚗 Car Price Prediction | End-to-End Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Deployed-Streamlit-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

> 💡 Predict the **resale price of used cars** using a production-ready Machine Learning pipeline with real-time deployment.

---

## 🚀 Live Demo

👉 **Try the app here:**  
🔗 https://car-price-predicition-spmjq8bptwqufza7xfy2wc.streamlit.app/

---

## 🧠 Project Overview

This project demonstrates a **complete end-to-end Machine Learning workflow**, from raw data preprocessing to deployment.

It simulates a **real-world ML system**, where users can input car details and get **instant price predictions** through a clean and interactive web interface.

---

## ✨ Key Highlights

- 🔥 **End-to-End ML Pipeline (Production Style)**
- ⚙️ Integrated **Data Preprocessing + Model Training**
- 🧩 Used **ColumnTransformer + Pipeline**
- 📊 Compared Multiple Models (Linear Regression, Random Forest, XGBoost)
- 🎯 Optimized for better prediction accuracy
- 🌐 **Deployed using Streamlit Cloud**
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
