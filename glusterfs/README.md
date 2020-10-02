# Gluster Filesystem

## How to deploy a glusterfs server

Requirements:

- Linux server, with a kernel version better than 5.6
  - This guide will use Debian 10
- A client server, like another linux server, or a PC
  - This guide will assume Debian 10
- VPN running on server and host
  - Wireguard is assumed here, but tools like sstunnel work, too

The server is assumed to be the machine interfacing with the original physical drive.

### Installation

```bash
## Server will need both
apt install glusterfs-server glusterfs-client

## Client
apt install glusterfs-client
```

### Server volume setup

```bash
#
# $volume_name the common label name of the drive
# $stripe_count, use 1.
#	a parameter to store chunks of the file across different paritions of a hard drive.
# $server_address the VPN interface
# $share_directory the directory to share over the network
#
gluster volume create $volume_name $stripe_count $server_address:$share_directory force

gluster volume start $volume_name

gluster volume status $volume_name

#
##
gluster volume create dropbox 1 10.8.0.1:/mnt/sda1 force

gluster volume start dropbox

gluster volume status dropbox

```

### Client volume setup

```bash

mount -t glusterfs $server_address:$volume_name $share_directory

mount -t glusterfs 10.8.0.1:dropbox /Volumes/my-dropbox

```

### Need Help?

Contact me at code@mashio.net
