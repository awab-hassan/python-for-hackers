# Demo of how you would use nmap (scanner).

ip_address = (input("Enter IP Address: "))

def nmap(ip):
    scan = (f"nmap -A -p- {ip} -v")
    print(f"Running nmap scan against: {ip} || " + f"CMD: {scan}")

nmap(ip_address)

