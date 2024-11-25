import netmiko
import subprocess
import re
import napalm
import nornir
import IPy
import scapy

from netmiko import ConnectHandler

def send_ping_from_switch(host, username, password, ping_targets):
    """
    Connect to a switch and send ping requests to specified targets.
    
    :param host: IP address of the switch
    :param username: Username for SSH login
    :param password: Password for SSH login
    :param enable_password: Enable mode password
    :param ping_targets: List of IP addresses to ping
    :return: Dictionary containing ping results for each target
    """
    switch = {
        'device_type': 'cisco_ios',  # Replace with your device type if different
        'host': host,
        'username': username,
        'password': password,
        'port': 22,
    }
    
    try:
        # Connect to the switch
        connection = ConnectHandler(**switch)
        
        # Send ping commands and collect results
        ping_results = {}
        for target in ping_targets:
            command = f"ping {target}"
            result = connection.send_command(command)
            ping_results[target] = result
        
        # Disconnect from the switch
        connection.disconnect()
        
        return ping_results

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define switch parameters
    host = "devnetsandboxiosxe.cisco.com"
    username = "admin"
    password = "C1sco12345"
    
    # List of devices to ping
    ping_targets = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]
    
    # Send ping requests and get results
    results = send_ping_from_switch(host, username, password, ping_targets)
    
    # Print the results
    if results:
        for target, output in results.items():
            print(f"Ping to {target}:\n{output}\n")
