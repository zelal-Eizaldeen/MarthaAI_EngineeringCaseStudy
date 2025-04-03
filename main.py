
import random
import pickle
import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

model = 'ad_performance_model.pkl'
#Initialize FastAPI app
app = FastAPI()
app


# API Request Model
class AdPerformanceRequest(BaseModel):
    spend: float
    impressions: int
    ctr: float

@app.post("/predict")
def predict_conversion(ad: AdPerformanceRequest):
    features = np.array([[ad.spend, ad.impressions, ad.ctr]])
    predicted_conversions = model.predict(features)[0]
    return {"predicted_conversions": predicted_conversions}

@app.get("/health")
def health_check():
    return {"status": "API is running"}

"""#Testing FastAPI"""

