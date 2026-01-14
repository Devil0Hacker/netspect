#!/data/data/com.termux/files/usr/bin/bash

clear
echo "=============================="
echo " NetSpect Installer (Termux) "
echo "=============================="

pkg update -y
pkg install -y python git nmap whois curl

pip install --upgrade pip
pip install holehe requests colorama rich

chmod +x netspect.py

ln -sf $HOME/netspect/netspect.py $PREFIX/bin/netspect

echo ""
echo "Installation completed!"
echo "Run tool using: netspect"
