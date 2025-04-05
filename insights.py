import pandas as pd
import numpy as np

# Load synthetic ad data
df = pd.read_csv("synthetic_ad_data.csv")

# Ensure 'ad_id' exists
if "ad_id" not in df.columns:
    df["ad_id"] = range(1, len(df) + 1)  # Assign unique IDs
    
df["date"] = pd.to_datetime(df["date"])

# 📉 Identify Poor-Performing Ads
low_ctr_threshold = 0.02  # Below 2% CTR is concerning
low_conversion_threshold = df["conversions"].quantile(0.25)  # Bottom 25% conversions

poor_ads = df[(df["ctr"] < low_ctr_threshold) | (df["conversions"] < low_conversion_threshold)]

# 🔄 Suggest Budget Reallocation
top_ads = df.sort_values(by="conversions", ascending=False).head(5)  # Top 5 high-converting ads
poor_ads_spend = poor_ads["ad_spend"].sum()
if poor_ads_spend > 0:
    avg_conversion_rate = top_ads["conversions"].sum() / top_ads["ad_spend"].sum()
    suggested_budget_shift = round(poor_ads_spend * avg_conversion_rate, 2)
else:
    suggested_budget_shift = 0

# 🧪 A/B Testing Suggestions
ab_testing_needed = df.groupby("ad_id")[["ctr", "conversions"]].std().reset_index()
ab_testing_needed = ab_testing_needed[(ab_testing_needed["ctr"] > 0.01) & (ab_testing_needed["conversions"] > 5)]
ab_testing_suggestions = ab_testing_needed["ad_id"].tolist()

# 📢 Print Insights
print("\n🔍 Automated Insights & Recommendations\n")

if not poor_ads.empty:
    print("🚨 Poor-Performing Ads (Low CTR or Conversions):")
    print(poor_ads[["ad_id", "ctr", "conversions", "ad_spend"]])

if suggested_budget_shift > 0:
    print(f"\n💰 Suggested Budget Shift: Move ${suggested_budget_shift} from low-performing ads to high-converting ones.")

if ab_testing_suggestions:
    print("\n🧪 Suggested A/B Testing for Ads:")
    print(ab_testing_suggestions)
else:
    print("\n✅ No immediate A/B testing needs detected.")
