import os
from core.utils import pause

def email_menu():
    os.system("clear")
    print("""
[1] Email Enumeration (Holehe)
[0] Back
""")
    c = input("Choose: ")

    if c == "1":
        email = input("Enter email: ")
        os.system(f"holehe {email}")
    pause()
