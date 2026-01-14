import os
import time

def banner():
    print("""
███╗   ██╗███████╗████████╗███████╗██████╗ ███████╗ ██████╗████████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝
██╔██╗ ██║█████╗     ██║   ███████╗██████╔╝█████╗  ██║        ██║   
██║╚██╗██║██╔══╝     ██║   ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   
██║ ╚████║███████╗   ██║   ███████║██║     ███████╗╚██████╗   ██║   
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   

NetSpect – Termux Network & OSINT Toolkit
Educational Use Only
""")

def menu():
    print("""
[1] Network Scanning
[2] IP Intelligence
[3] Email OSINT
[4] Device Status
[0] Exit
""")

def pause():
    input("\nPress Enter to continue...")
