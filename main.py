from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("synthetic_ad_data.csv")
df["date"] = pd.to_datetime(df["date"])

# FastAPI app setup
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def dashboard(request: Request, ad_id: int = None):
    if ad_id is not None:
        df_filtered = df[df["ad_id"] == ad_id]
    else:
        df_filtered = df  # Show all data if no ad is selected

    # Generate Plotly charts
    spend_fig = px.line(df_filtered, x="date", y="ad_spend", title="📈 Ad Spend Over Time").to_html()
    ctr_fig = px.bar(df_filtered, x="date", y=["ctr", "conversions"], title="📊 CTR & Conversions").to_html()

    # Get summary stats
    total_spend = df_filtered["ad_spend"].sum()
    total_impressions = df_filtered["impressions"].sum()
    avg_ctr = df_filtered["ctr"].mean()
    total_conversions = df_filtered["conversions"].sum()

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "spend_fig": spend_fig,
        "ctr_fig": ctr_fig,
        "total_spend": total_spend,
        "total_impressions": total_impressions,
        "avg_ctr": avg_ctr,
        "total_conversions": total_conversions,
        "ad_ids": df["ad_id"].unique(),
        "selected_ad": ad_id
    })
