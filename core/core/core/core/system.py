import os
from core.utils import pause

def system_menu():
    os.system("clear")
    print("""
[1] Device IP
[2] RAM Usage
[3] Storage Usage
[0] Back
""")
    c = input("Choose: ")

    if c == "1":
        os.system("ip a")
    elif c == "2":
        os.system("free -h")
    elif c == "3":
        os.system("df -h")
    pause()
