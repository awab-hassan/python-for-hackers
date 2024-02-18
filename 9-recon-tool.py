# This is a basic recon tool, you can use this tool inside your kali linux machine.
import os 

def recon(ip):
    print("Starting the recon process . . .")
    os.system(f"nmap {ip} -v")
    os.system(f"dirb http://{ip}")
    # Keep adding more recon commands, for example ffuf

ip_address = input("Enter the IP Address: ")
recon(ip_address)