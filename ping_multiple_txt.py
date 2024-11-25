import socket
from ping3 import ping
from datetime import datetime
import os

def resolve_hostname(hostname):
    """
    Resolve the hostname or FQDN to an IP address.
    """
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror as e:
        print(f"!!! Error resolving {hostname}: {e}")
        return None

def log_message(message, output_file):
    """
    Log a message to both the terminal and the specified output file.
    """
    print(message, end="")
    with open(output_file, "a") as file:
        file.write(message)

def ping_target(ip_address, count, output_file):
    """
    Ping the target IP address multiple times and log results with appropriate exclamations.
    """
    for i in range(count):
        response_time = ping(ip_address)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if response_time:
            if response_time > 0.150:  # High latency threshold
                message = f"!!! {timestamp} - Reply from {ip_address}: time={response_time:.4f} seconds.\n"
            elif response_time > 0.050:  # Medium latency threshold
                message = f"!! {timestamp} - Reply from {ip_address}: time={response_time:.4f} seconds.\n"
            else:
                message = f"{timestamp} - Reply from {ip_address}: time={response_time:.4f} seconds.\n"
        else:
            message = f"!!! {timestamp} - Request to {ip_address} failed.\n"
        
        log_message(message, output_file)

def main():
    # Step 1: Get the file with hostnames/IP addresses from the user
    input_file = input("Enter the name of the text file with the list of hostnames/IPs (e.g., hosts.txt): ").strip()
    
    try:
        with open(input_file, "r") as file:
            hosts = file.readlines()
    except FileNotFoundError:
        print(f"!!! Error: File '{input_file}' not found.")
        return

    # Step 2: Get the number of pings to send
    try:
        count = int(input("How many ping requests would you like to send to each host? ").strip())
        if count < 1:
            raise ValueError("The number of ping requests must be at least 1.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Step 3: Extract base filename without extension and create a new output filename with timestamp
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{base_filename}_ping_results_{timestamp}.txt"
    print(f"Results will be saved in: {output_file}")

    # Step 4: Log the start of the test with the timestamp
    log_message(f"\nPing Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", output_file)

    # Step 5: Ping each host/IP multiple times and log results
    for host in hosts:
        host = host.strip()  # Remove any extra whitespace or newline characters
        print(f"Pinging {host}...")

        if not host.replace('.', '').isdigit():  # Check if input is a hostname
            ip_address = resolve_hostname(host)
            if not ip_address:
                log_message(f"!!! Could not resolve {host}\n", output_file)
                continue
        else:
            ip_address = host
        
        # Log the host or IP address and start the ping results
        log_message(f"{host}\n", output_file)
        ping_target(ip_address, count, output_file)
        
        # Add a blank line after the results of each host/IP for readability
        log_message("\n", output_file)

if __name__ == "__main__":
    main()