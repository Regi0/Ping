2 Things for this project:

1. Create a ping request from your device to an IP address
-> Ping a device
-> Write away the end result


2. Create a ping request from a switch to an IP address
-> Log into the switch/router
-> Send a ping
-> Write away the end result



Extra features:
For client:
- Use hostnames, give IP address as well, with nslookup
- Give the option to ping for multiple multiple ping requests
- Give it a file so it can go trough the list
- Get the output into a specific file, maybe a csv/excel file?
    - Colour coding for succesful attempts:
        OK, latency lower than 50ms -> green
        OK, latency between 50ms and 400ms -> orange
        No response or latency above 400ms -> red

For switch/router:
- Lookup MAC addresses of the hostnames, show to the user
- Give the option to ping for multiple multiple ping requests
    - Do a lookup for the first half, to see who is the vendor, what kind of device is connected
- Give it a file so it can go trough the list
- Get the output into a specific file, maybe a csv/excel file?
    - Colour coding for succesful attempts:
        OK, latency lower than 50ms -> green
        OK, latency between 50ms and 400ms -> orange
        No response or latency above 400ms -> red