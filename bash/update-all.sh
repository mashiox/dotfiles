#!/usr/bin/env bash

# Check if the script is run as root (EUID 0)
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run with root privileges. Please use sudo."
   exit 1
fi

apt update && apt --yes -qq upgrade

snap refresh

flatpak update --assumeyes

sudo -u "$SUDO_USER" flatpak update --assumeyes

fwupdmgr --assume-yes get-updates

echo "[$SUDO_USER] system packages updated."
