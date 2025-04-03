import random
import pickle
import pandas as pd
import numpy as np
from pydantic import BaseModel
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Simulated Ad Data Generator
def generate_sample_data(n=1000):
    data = {
        "ad_id": [f"ad_{i}" for i in range(n)],
        "spend": np.random.uniform(10, 1000, n),  # Ad spend ($)
        "impressions": np.random.randint(1000, 100000, n),
        "ctr": np.random.uniform(0.01, 0.2, n),  # Click-through rate
        "conversions": np.random.randint(0, 50, n),  # Conversions
    }
    return pd.DataFrame(data)
# Load data (replace with REAL Meta Ads API pull if available)
ad_data = generate_sample_data()
print(ad_data)