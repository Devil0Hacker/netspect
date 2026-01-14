#!/usr/bin/env python3
import os
import sys
import time
import subprocess

from core.utils import banner, menu, pause
from core.network import network_menu
from core.ipinfo import ip_menu
from core.email import email_menu
from core.system import system_menu

def main():
    while True:
        os.system("clear")
        banner()
        menu()
        choice = input("\nSelect option: ").strip()

        if choice == "1":
            network_menu()
        elif choice == "2":
            ip_menu()
        elif choice == "3":
            email_menu()
        elif choice == "4":
            system_menu()
        elif choice == "0":
            print("\nGoodbye 👋")
            sys.exit()
        else:
            print("Invalid option!")
            pause()

if __name__ == "__main__":
    main()
