# Network Scanning Tools

## Project Description
This project contains simple Python programs to perform basic network scanning tasks.  
It includes three tools:

1. Ping Scanner  
2. ARP Scanner  
3. Nmap Scanner  

These tools use Python and system commands to scan and analyze network information.



## Requirements

Before running the programs, make sure the following are installed:

- Python 3
- Nmap




## Installing Nmap

Download and install Nmap from the official website:

https://nmap.org/download.html

After installing, verifying  the installation:

nmap --version





### Run Ping Scanner

Command:

py ping_scanner.py

Example Output:
Enter hostname or IP: google.com
Host is reachable
Average Time: 9ms

---

### Run ARP Scanner

Command:

py arp_scanner.py

Example Output:

=== ARP Scanner ===
IP Address      MAC Address
-----------------------------------
192.168.2.1     08-7b-87-9b-89-f4
192.168.2.2     94-18-65-4f-7a-ab
192.168.2.10    28-00-af-d4-ba-13
192.168.2.18    10-98-19-bc-4e-9f
192.168.2.222   28-00-af-d4-b9-ff
192.168.2.247   78-46-5c-5e-2b-4d
192.168.2.255   ff-ff-ff-ff-ff-ff
224.0.0.22      01-00-5e-00-00-16
224.0.0.251     01-00-5e-00-00-fb
224.0.0.252     01-00-5e-00-00-fc
239.255.255.250 01-00-5e-7f-ff-fa
255.255.255.255 ff-ff-ff-ff-ff-ff
192.168.56.255  ff-ff-ff-ff-ff-ff
224.0.0.22      01-00-5e-00-00-16
224.0.0.251     01-00-5e-00-00-fb
224.0.0.252     01-00-5e-00-00-fc
239.255.255.250 01-00-5e-7f-ff-fa

Total entries: 17




### Run Nmap Scanner

Command:

py nmap_scanner.py

Example:

=== Nmap Scanner ===
Enter target IP: nmap -F scanme.nmap.org
Starting Nmap 7.98 ( https://nmap.org ) at 2026-03-16 18:30 +0530
Nmap scan report for nmap -F scanme.nmap.org (50.116.1.184)
Host is up (0.26s latency).
Other addresses for nmap -F scanme.nmap.org (not scanned): 2600:3c01:e000:3e6::6d4e:7061
rDNS record for 50.116.1.184: ack.nmap.org
Not shown: 993 filtered tcp ports (no-response), 1 filtered tcp ports (admin-prohibited)

PORT      STATE  SERVICE
22/tcp    open   ssh
70/tcp    closed gopher
80/tcp    open   http
113/tcp   closed ident
443/tcp   open   https
31337/tcp closed Elite



## Screenshots

Screenshots of the program outputs are stored in the screenshots folder.


screenshots/ping_output.png  
screenshots/arp_output.png  
screenshots/nmap_output.png  



