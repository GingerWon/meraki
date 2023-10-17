import re
import os
import meraki
from dotenv import load_dotenv
load_dotenv()


def connecttodashboard():
    api_key = os.environ.get("API_KEY")
    dashboard = meraki.DashboardAPI(api_key)
    orgid = os.environ.get("ORG_ID")
