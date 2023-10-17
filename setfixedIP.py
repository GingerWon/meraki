import meraki
import requests
import os
from dotenv import load_dotenv
load_dotenv()

import meraki

# Create a Meraki Dashboard API client session
API_KEY = os.environ.get("API_KEY")
dashboard = meraki.DashboardAPI(API_KEY)

# Define the network ID where you want to create or update the DHCP assignment
network_id = os.environ.get('NET_ID')

# Define the client's MAC address and desired fixed IP address
client_mac = '00:11:22:33:44:55'
fixed_ip = '192.168.1.36'

# Get the list of all clients in the network
try:
    # Get the list of devices in the network
    devices = dashboard.networks.getNetworkDevices(network_id)

    # Search for the device by MAC address
    target_device = next((device for device in devices if device['mac'] == client_mac), None)

    if target_device:
        # Update the device's DHCP assignment
        target_device['dhcpReservations'] = [{
            'mac': client_mac,
            'ip': fixed_ip
        }]

        # Update the network configuration to apply the changes
        dashboard.networks.updateNetwork(network_id, dhcpReservations=target_device['dhcpReservations'])
        print(f"Fixed IP assignment updated successfully for {client_mac}.")
    else:
        print(f"Device with MAC address {client_mac} not found in the network.")
except meraki.APIError as e:
    print(f"Meraki API error: {e}")