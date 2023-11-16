from typing import List
from enum import Enum

import pandas as pd

from fastapi import FastAPI

from data_model import DataModel
from prediction_model import PredictionModel


app = FastAPI()
features = ["gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
        "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
        "MonthlyCharges", "TotalCharges"]

class ModelNumber(int, Enum):
    first = 1
    second = 2

@app.get("/")
def read_root():
    return [{ "message": "Hello world" }]

@app.post("/{model_version}/predict")
def make_predictions(model_version: ModelNumber, X: List[DataModel]):   
    df = pd.DataFrame([x.model_dump() for x in X])
    df = df[features]
    prediction_model = PredictionModel(model_version)
    results = prediction_model.make_predictions(df)
    return results

# You can specify how many variables to retrieve to explain the result by using num_features
@app.post("/{model_version}/explain")
def explain_predictions(model_version: ModelNumber, X: List[DataModel], num_features: int | None = 3):
    df = pd.DataFrame([x.model_dump() for x in X])
    df = df[features]
    prediction_model = PredictionModel(model_version)
    results = prediction_model.explain_prediction(df,num_features)
    return results
