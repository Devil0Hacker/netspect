import os
from core.utils import pause

def ip_menu():
    os.system("clear")
    print("""
[1] My IP
[2] IP Details
[0] Back
""")
    c = input("Choose: ")

    if c == "1":
        os.system("curl ifconfig.me")
    elif c == "2":
        ip = input("Enter IP: ")
        os.system(f"whois {ip}")
    pause()
