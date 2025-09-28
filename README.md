# 📊 Customer Churn Prediction Project

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-lightblue?logo=fastapi)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-2.3.2-blue?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Project Overview
This project predicts **customer churn** for a telecom company using machine learning.  
It provides a **FastAPI endpoint** for real-time predictions and a **dashboard** to visualize churn probability.

- Dataset: `WA_Fn-UseC_-Telco-Customer-Churn.csv`
- Machine Learning Model: Random Forest / Logistic Regression
- Features include: customer demographics, account info, services, and billing details.

---

## 🛠️ Features
- ✅ Predict if a customer will churn or not  
- ✅ Calculate **churn probability**  
- ✅ Dashboard to visualize predictions and insights  
- ✅ API endpoint for integration with apps  

---


## 📁 Project Structure
customer_churn_project/
│
├─ .venv/ # Python virtual environment
├─ dashboard.py # Streamlit dashboard
├─ train_model.py # Model training script
├─ churn_model.pkl # Saved ML model
├─ churn_pipeline.pkl # Preprocessing pipeline
├─ scaler.pkl # Standard scaler
├─ app.py # FastAPI application
├─ WA_Fn-UseC_-Telco-Customer-Churn.csv
└─ README.md # Project documentation


---

## ⚡ Installation
1. Clone the repository:
```bash
git clone https://github.com/5aurabhdubey/customer_churnmodel.git
cd customer_churn_project
python -m venv .venv
# Windows PowerShell
& .venv/Scripts/Activate.ps1

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

🧑‍💻 Usage
1. Train Model
python train_model.py

2. Run API
uvicorn app:app --reload


API endpoint: POST /predict

Example JSON body:
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.35,
  "TotalCharges": 845.5
}
3. Run Dashboard
streamlit run dashboard.py

📈 Sample Output

Churn prediction: 0 → Not Churn

Churn probability: 32%

🔧 Technologies Used

Python 🐍

FastAPI ⚡

Scikit-learn 🔹

Pandas 🐼

Streamlit ✨

Joblib 💾

📝 License

This project is licensed under the MIT License.

📫 Contact

GitHub: 5aurabhdubey

Email:sddubey492@gmail.com


