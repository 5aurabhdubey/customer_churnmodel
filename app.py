from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is running!"}

@app.post("/predict")
def predict(data: dict):
    # Convert input to DataFrame
    df = pd.DataFrame([data])

    # One-hot encode same as training
    df = pd.get_dummies(df)
    
    # Align columns with training data (fill missing)
    expected_cols = model.n_features_in_
    df = df.reindex(columns=range(expected_cols), fill_value=0)

    # Scale data
    df_scaled = scaler.transform(df)

    # Predict
    prediction = model.predict(df_scaled)[0]
    probability = model.predict_proba(df_scaled)[0][1]

    return {"churn": int(prediction), "churn_probability": float(probability)}
