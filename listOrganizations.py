import os
import meraki
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
dashboard = meraki.DashboardAPI(API_KEY)
orgs = dashboard.organizations.getOrganizations()

# To see a list of all organizations and their ID's-
# for org in orgs:
#     print(org['name'], org['id'], sep=" : ")

# To see a specific orgs ID -
target = "DevNet"
for org in orgs:
    if target in org['name']:
        print(org['name'], ":", org['id'])
