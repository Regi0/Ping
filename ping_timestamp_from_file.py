import socket
from ping3 import ping
from datetime import datetime

def resolve_hostname(hostname):
    """
    Resolve the hostname or FQDN to an IP address.
    """
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Resolved {hostname} to {ip_address}.\n")
        return ip_address
    except socket.gaierror as e:
        print(f"!!! Error resolving {hostname}: {e}\n")
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
    Ping the target IP address with the specified count and log results.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message(f"\nPing started at: {timestamp}\n", output_file)
    
    for i in range(count):
        response_time = ping(ip_address)
        if response_time:
            if response_time > 0.150:  # High latency threshold
                message = f"!!! High latency detected: Reply from {ip_address}: time={response_time:.4f} seconds.\n"
            else:
                message = f"Reply from {ip_address}: time={response_time:.4f} seconds.\n"
        else:
            message = f"!!! Request to {ip_address} failed.\n"
        log_message(message, output_file)

def main():
    # Step 1: Get target from user
    target = input("Enter an IP address or hostname/FQDN to ping: ").strip()

    # Step 2: Resolve hostname/FQDN if necessary
    if not target.replace('.', '').isdigit():  # Check if input is not an IP address
        ip_address = resolve_hostname(target)
        if not ip_address:
            print("Exiting due to unresolved hostname.\n")
            return
    else:
        ip_address = target

    # Step 3: Create the output file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # e.g., 20241125_131030
    output_file = f"{target.replace('.', '_')}_{timestamp}.txt"
    print(f"Results will be saved in: {output_file}")

    # Step 4: Ask if user wants to send multiple pings
    multiple = input("Do you want to send multiple pings? (yes/no): ").strip().lower()
    if multiple in ['yes', 'y']:
        try:
            count = int(input("Enter the number of ping requests to send: ").strip())
            if count < 1:
                raise ValueError("The number of ping requests must be at least 1.")
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            return
    else:
        count = 4  # Default count

    # Step 5: Perform the ping
    ping_target(ip_address, count, output_file)

if __name__ == "__main__":
    main()
