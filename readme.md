Main objective of this project:

1. Create a ping request from your device to an IP address
-> Ping a device
-> Write away the end result in a file 

Single ones:

ping_one_at_a_time:
For client:
- Use hostnames, give IP address as well, with nslookup DONE
- Give the option to ping for multiple ping requests DONE
- Give a timestamp of when the ping was completed DONE
DONE

ping_timestamp_from_file:
For client:
- it will use the current date and time for the filename, with the hostname/IP address
DONE


Multiple ones at a time:

ping_multiple_txt:
Create a separate one for multiple IP addresses/clients
- Input a txt file
- It will go through the list and print the result in a txt file.
    - Colour coding for succesful attempts:
        OK, latency lower than 50ms -> nothing will be added
        OK, latency between 50ms and 150ms -> !! will be added in front
        No response or latency above 150ms -> !!! will be added in front
DONE

TO DO:

ping_multiple_libre:
Create a separate one for multiple IP addresses/clients
- Input a txt file
- Get the output into a libreoffice math/excel file:
    - Colour coding for attempts:
        OK, latency lower than 50ms -> give the cell a green font
        OK, latency between 50ms and 150ms -> give the cell an orange font
        No response or latency above 150ms -> give the cell a red font
DONE


ping_multiple_excel:
Create a separate one for multiple IP addresses/clients
- Input a CSV/Excel file
- Get the output into a CSV/Excel file:
    - Colour coding for attempts:
        OK, latency lower than 50ms -> give the cell a green font
        OK, latency between 50ms and 150ms -> give the cell an orange font
        No response or latency above 150ms -> give the cell a red font
DONE