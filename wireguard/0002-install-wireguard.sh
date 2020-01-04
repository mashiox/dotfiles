#!/bin/bash

# System Install
#add-apt-repository ppa:wireguard/wireguard
#apt install wireguard

# Firewall
#ufw allow 51820/udp
#ufw status verbose

# Configuration
mkdir -p /etc/wireguard
cp -r wg0.conf /etc/wireguard/wg0.conf

