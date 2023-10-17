import re
import os
import meraki
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
dashboard = meraki.DashboardAPI(API_KEY)
orgID = os.environ.get("ORG_ID")
networks = dashboard.organizations.getOrganizationNetworks(orgID)

target = "vmx"
filtered = [x for x in networks if target in x['name']]
for f in filtered:
    print(f['id'])
    #print(f['name'], f['id'])
