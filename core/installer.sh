#!/data/data/com.termux/files/usr/bin/bash
clear
pkg update -y
pkg install -y python git nmap whois curl
pip install holehe
chmod +x netspect.py
ln -sf $PWD/netspect.py $PREFIX/bin/netspect
echo "Installed! Run using: netspect"
