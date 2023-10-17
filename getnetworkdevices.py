import os
import meraki
from dotenv import load_dotenv
load_dotenv()
from getnwid import getnwid

API_KEY = os.environ.get('API_KEY')
dashboard = meraki.DashboardAPI(API_KEY)
network_id = getnwid()
devices = dashboard.networks.getNetworkDevices(network_id)
networks = dashboard.organizations.getOrganizationNetworks(orgID)

def getnwdev(target):
    for device in devices:
        print(device['name'], device['serial'], device['model'], sep=':')
