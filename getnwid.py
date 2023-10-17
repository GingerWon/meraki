import os
import meraki
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
dashboard = meraki.DashboardAPI(API_KEY)

orgID = os.environ.get("ORG_ID")
networks = dashboard.organizations.getOrganizationNetworks(orgID)


def getnwid(target):
    for net in networks:
        if target in net['name']:
            print(net['name'], ":", net['id'])


getnwid("CCNA")
