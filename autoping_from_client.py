from ping3 import verbose_ping

def ping_ip(ip_address, count):
    try:
        print(f"Pinging {ip_address} with {count} requests...")
        verbose_ping(ip_address, count=count)
    except Exception as e:
        print(f"Error pinging {ip_address}: {e}")

# Get user input
ip = input("Enter an IP address to ping: ")
try:
    count = int(input("Enter the number of ping requests to send: "))
    if count < 1:
        raise ValueError("The number of ping requests must be at least 1.")
    ping_ip(ip, count)
except ValueError as e:
    print(f"Invalid input: {e}")
