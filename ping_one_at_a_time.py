import socket
from ping3 import ping, verbose_ping

def resolve_hostname(hostname, output_file):
    """
    Resolve the hostname or FQDN to an IP address and log to file.
    """
    try:
        ip_address = socket.gethostbyname(hostname)
        message = f"Resolved {hostname} to {ip_address}.\n"
        print(message, end="")
        with open(output_file, "a") as file:
            file.write(message)
        return ip_address
    except socket.gaierror as e:
        message = f"Error resolving {hostname}: {e}\n"
        print(message, end="")
        with open(output_file, "a") as file:
            file.write(message)
        return None

def ping_target(ip_address, count, output_file):
    """
    Ping the target IP address with the specified count and log to file.
    """
    with open(output_file, "a") as file:
        if count == 1:
            # Single ping
            response_time = ping(ip_address)
            if response_time:
                message = f"Ping to {ip_address} successful! Response time: {response_time:.4f} seconds.\n"
            else:
                message = f"Ping to {ip_address} failed.\n"
            print(message, end="")
            file.write(message)
        else:
            # Multiple pings
            message = f"Pinging {ip_address} with {count} requests...\n"
            print(message, end="")
            file.write(message)
            for _ in range(count):
                response_time = ping(ip_address)
                if response_time:
                    line = f"Reply from {ip_address}: time={response_time:.4f} seconds.\n"
                else:
                    line = f"Request to {ip_address} failed.\n"
                print(line, end="")
                file.write(line)

def main():
    # Step 1: Get target and output file name from user
    target = input("Enter an IP address or hostname/FQDN to ping: ").strip()
    output_file = input("Enter the name of the output file (e.g., results.txt): ").strip()

    # Step 2: Resolve hostname/FQDN if necessary
    if not target.replace('.', '').isdigit():  # Check if input is not an IP address
        ip_address = resolve_hostname(target, output_file)
        if not ip_address:
            print("Exiting due to unresolved hostname.")
            return
    else:
        ip_address = target

    # Step 3: Ask if user wants to send multiple pings
    multiple = input("Do you want to send multiple pings? (yes/no): ").strip().lower()
    if multiple in ['yes', 'y']:
        try:
            count = int(input("Enter the number of ping requests to send: ").strip())
            if count < 1:
                raise ValueError("The number of ping requests must be at least 1.")
        except ValueError as e:
            message = f"Invalid input: {e}\n"
            print(message, end="")
            with open(output_file, "a") as file:
                file.write(message)
            return
    else:
        count = 4  # Default count

    # Step 4: Perform the ping
    ping_target(ip_address, count, output_file)

if __name__ == "__main__":
    main()