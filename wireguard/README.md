# Wireguard

## How to deploy a Wireguard VPN

Requirements:

- Linux server, with a kernel version better than 5.6
  - This guide will use Debian 10
  - this is the server the Peer will connect to, and where VPN traffic will exit
- A computer with an internet connection (like a cell phone)
  - This is the Peer, or Client

### Getting a Server

There are many cheap server providers available, many with non US hosting options

Linode
Digital Ocean
swissnode.ch

### Getting a Wireguard client

https://www.wireguard.com/install/

### Installation on Server

Make note of your Server's IP address.

```bash
apt install wireguard

# Generate your Server's public and private keys
wg genkey | tee server_private.key | wg pubkey > server_public.key
chmod 600 server_private.key

# Generate the Client's public and private keys
wg genkey | tee client_private.key | wg pubkey > client_public.key
chmod 600 client_private.key

```

### Configuration of Server

Replace `@@wg0_server_private_key@@` with the contents of the file `server_private.key`, and replace `@@wg0_client_public_key@@` with the contents of the file `client_public.key`

Save the new configuration to `/etc/wireguard/wg0.conf` on the server.

```conf
# Wireguard interface on the server
[Interface]
Address = 10.1.1.1/24
ListenPort = 42010
PrivateKey = EXAMPLE-Private/Key/=

# Client configuration on the server
[Peer]
PublicKey = EXAMPLE-Public-key//=
AllowedIPs = 10.1.1.2
PersistentKeepalive = 24
```

### Configuration of the Client

Replace `@@wg0_client_private_key@@` with the contents of the file `client_private.key`, and replace `@@wg0_server_public_key@@` with the contents of the file `server_public.key`

This configuration does not need to get saved to the server, but will go on your client device later.

```conf
# Wireguard interface on the client
[Interface]
PrivateKey = EXAMPLE/CLIENT/PRIVATE/KEY=
Address = 10.1.1.2/24
ListenPort = 42020

## Server configuration on the client
[Peer]
PublicKey = EXAMPLE-/SERVER---PUBLIC/KEY
AllowedIPs = 10.1.1.1
Endpoint = @@YOUR_SERVER_IP_ADDRESS@@:42010
PersistentKeepalive = 24
```

### Starting the Server

```bash
# Turn on the Server
wg-quick up wg0

# Check the running configuration
wg show

# Enable Wireguard to turn on after reboot
systemctl enable wg-quick@wg0
```

### Connecting to the Server on the Client

Install a client from https://www.wireguard.com/install/

Mobile:

Import the client config and connect to your server

Desktop: (except windows?)

Use the same commands in the "Starting the Server" section on your client machine, and start the VPN.
