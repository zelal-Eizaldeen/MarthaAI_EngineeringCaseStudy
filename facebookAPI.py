import os
from dotenv import load_dotenv
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
AD_ACCOUNT_ID = os.getenv("AD_ACCOUNT_ID")

# Initialize Meta Ads API
FacebookAdsApi.init(access_token=ACCESS_TOKEN)

# Fetch ad performance data
FIELDS = ["date_start", "spend", "impressions", "clicks", "ctr", "conversions"]
PARAMS = {
    "time_range": {"since": "2024-03-01", "until": "2024-03-31"},
    "level": "ad",
    "time_increment": 1
}

ad_account = AdAccount(AD_ACCOUNT_ID)
ads_insights = ad_account.get_insights(fields=FIELDS, params=PARAMS)

# Print results
for insight in ads_insights:
    print(insight)
