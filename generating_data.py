import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 90 days of sample ad data
num_days = 90
dates = pd.date_range(start="2024-01-01", periods=num_days)

# Generate synthetic ad metrics
ad_spend = np.random.uniform(50, 500, num_days)  # Spend between $50 - $500
impressions = np.random.randint(10000, 100000, num_days)  # Impressions between 10K - 100K
clicks = (impressions * np.random.uniform(0.01, 0.10, num_days)).astype(int)  # CTR between 1% - 10%
ctr = clicks / impressions  # Compute CTR
conversions = (clicks * np.random.uniform(0.05, 0.15, num_days)).astype(int)  # Conversion Rate between 5% - 15%

# Create DataFrame
ad_data = pd.DataFrame({
    "ad_id": range(1, num_days + 1),  # ✅ Fixed: unique ad IDs
    "date": dates,
    "ad_spend": ad_spend,
    "impressions": impressions,
    "clicks": clicks,
    "ctr": ctr,
    "conversions": conversions
})

# Save to CSV
ad_data.to_csv("synthetic_ad_data.csv", index=False)

# Display sample data
print(ad_data.head())
