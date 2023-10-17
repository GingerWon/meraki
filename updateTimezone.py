import os
import meraki
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ.get('API_KEY')
dashboard = meraki.DashboardAPI(API_KEY)
orgID = os.environ.get("ORG_ID")
networks = dashboard.organizations.getOrganizationNetworks(orgID)
MountainStr = "vmx"
AZStr = "CCNP"
EasternStr = "CCNA"


def filterid(target):
    filtered = [x for x in networks if target in x['name']]
    for f in filtered:
        print(f['id'])

print("Eastern Jobs")
filterid(EasternStr)
print("--------------")
print("Mountain Jobs")
filterid(MountainStr)
print("--------------")
print("AZ Jobs")
filterid(AZStr)
    
# For a list of allowed timezones, please see the 'TZ' column in the table in this article.
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# Mountain = "America/Denver"
# AZ = "America/Phoenix"
# Eastern = "America/New_York"
# Central = "America/Chicago"
# Pacific = "America/Los_Angeles"

# MountainStr = ["W-CO", "W-ID", "W-WY"]
# AZStr = "W-AZ"
# EasternStr = []
# CentralStr = ["MW-KS", "MW-OK", "MW-NE", "SC-TX", "SC-OK"]
# PacificStr = ["W-CA", "W-OR", "W-NV"]

# response = dashboard.networks.updateNetwork(
#     NETWORKID,
#     timeZone='UTC -7',
# )
#
# print(response)
