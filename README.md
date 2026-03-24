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
    C --> D[Encoding and Scaling]
    D --> E[Model Training]
    E --> F[Pipeline Creation]
    F --> G[Model Serialization]
    G --> H[Streamlit Deployment]

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- scikit-learn  
- XGBoost  
- Streamlit  
- Matplotlib, Seaborn  
- Joblib  

---

## 📊 Features

- 🚘 Predict resale price instantly  
- 🧹 Cleaned & preprocessed dataset  
- 🔄 Fully automated ML pipeline  
- 📉 Handles numerical & categorical features  
- 🌐 Clean and responsive UI  
- ⚡ Fast and real-time predictions  

---

## 📈 Model Performance

- 🏆 Best results achieved using:
  - Random Forest Regressor  
  - XGBoost Regressor  

- 📌 Key influencing features:
  - Car Brand  
  - Year / Age  
  - Kilometers Driven  
  - Engine Capacity  
  - Power  

---

## ⚠️ Known Limitations

- Predictions may vary for:
  - Rare car models (low data availability)  
  - Outlier cases  

- UI may include categories not present after preprocessing (can be improved)

---

## 🚀 Deployment Details

- Hosted on Streamlit Cloud  
- Model saved using `joblib`  
- Integrated pipeline ensures:
  - No manual preprocessing required  
  - Consistent predictions  

---

## 📂 Project Structure

```bash
├── app.py                      # Streamlit UI
├── car_price_pipeline.joblib   # Trained ML pipeline
├── cleaned_data.csv            # Dataset
├── requirements.txt            # Dependencies
├── runtime.txt                 # Python version (optional)
└── README.md

## 🔮 Future Enhancements

- 🚀 Improve model accuracy with advanced feature engineering  
- 🧠 Add deep learning models  
- 🎯 Dynamic UI (Brand → Model filtering)  
- 📊 Add confidence intervals for predictions  
- 🌍 Deploy on scalable cloud platforms (AWS / GCP / Azure)  

---

## 👨‍💻 Author

**Siddiqui Usman Ahmed Siraj Ahmed**

📧 siddiquiusman915256@gmail.com  

🔗 https://www.linkedin.com/in/usman-siddiqui-948006347  
