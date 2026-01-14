import os
from core.utils import pause

def network_menu():
    os.system("clear")
    print("""
[1] Quick Scan
[2] Full Scan
[3] Local Network Devices
[0] Back
""")
    c = input("Choose: ")

    if c == "1":
        t = input("Target IP/Domain: ")
        os.system(f"nmap {t}")
    elif c == "2":
        t = input("Target IP/Domain: ")
        os.system(f"nmap -p- {t}")
    elif c == "3":
        os.system("nmap -sn 192.168.1.0/24")
    pause()
