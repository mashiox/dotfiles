# Systemd

## Suggested Reading

- https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files
- https://www.man7.org/linux/man-pages/man5/resolved.conf.5.html

## Systemd resolved.conf notes

Base configuration file: `/etc/systemd/resolved.conf`

Recommended Override config: 

```
/etc/systemd/resolved.conf -> /dev/null
/etc/systemd/system/resolved.conf
```

```ini
[Resolve]
# space-separated IPv4 or IPv6 to use as system DNS servers
DNS=
# only used if no other DNS server information is known
FallbackDNS=

# Default blank, space-separated list of search domains
# network-specific TLDs resolv can use to find a host that is missing a domain component
Domains=

# Windows DNS -  RFC 4795 ?
# https://en.wikipedia.org/wiki/Link-Local_Multicast_Name_Resolution
LLMNR=true|false|resolve

# Multicast DNS RFC 6762[2]
MulticastDNS=true|false|resolve

# All DNS lookups DNSSEC-validated locally on true (ex. LLMNR and Multicast DNS)
# DNSSEC validation is not possible until new trust anchors are configured locally
# or the resolver software package is updated with the new root trust anchor
DNSSEC=true|false|allow-downgrade

# Requires a DNS server that supports DNS-over-TLS and has a valid certificate
# for the IP when true.
# Use Let's Encypt DNS validation for the cert
DNSOverTLS=true|false|opportunistic

# resolving a domain name which already got queried earlier will return the previous
# result while the result is still valid
# implicitly turned off when on a host-local IP address (127.0.0.1, ::1, etc)
Cache=true|false|no-negative

# @todo
DNSStubListener=

# Read /etc/hosts and try to resolve host or address using file entries
ReadEtcHosts=true|false
```

## Systemd DO Crib Notes

Unit files

Configuration files for services running on a system, including daemons, sockets, mount devices, swap, cronjobs, backups, and other linux components.

Unit files can be found in 3 locations, which have a defined load order.

```
/lib/systemd/system - loaded last, upstream distribution services, perfer not to use this directory
/run/systemd/system - used for session modifications to services, not persisted
/etc/systemd/system - used for user configuration, perfer this directory 
```

Unit files have different dot-extensions prefixes to define what kind of system resource they manage.

```
.service - A unit to manage a program, daemon, or application
.socket - A unit to manage [network socket](https://beej.us/guide/bgnet/), IPC socket, or FIFO buffer.
.device - @todo
.mount - A unit to mange a mount point
.automount - @todo
.swap - A unit to manage system swap space
.target - @todo
.path - @todo 
.time - A unit to manage a scheduled process
.snapshot - A unit to capture Systemd session state
.slice - @todo
.scope - @todo
```

**Unit file rules**

```conf
[SectionName]

# Assignment
DirectiveName=Value

# Un-Assignment
Directive=

# A completely legitimate different section
[sectionname] # names are case sensitive

```

**Generic Systemd Unit File**

```conf

# The standard Unit section definition
[Unit]

# Free text
Description=
Documentation= # location of documention. man pages, urls, etc.

# Space separated list of other units files that this unit depends on
Requires=docker.service networking.service
# Less strict Require directive
Wants=
# Services that will stop this serivce if they are disrupted
BindsTo=

# Start this service before the specificed services
Before=
# Start this service after the specificed services
After=
# Services that can not run at the same time as this service.
# systemd will stop these services if this service starts with them active.
Conflicts=

# @todo
Codition...=
Assert...=

# Unit Type specific directives
# Service Type definitions
[Service]
# Default, if busname and it are empty, and ExecStart is not.
Type=simple

# Services that fork a child process
Type=forking

# @todo
Type=oneshot
RemainAfterExit=

# @todo
Type=dbus
BusName=

# @todo
Type=notify
NotifyAccess=none|main|all

# @todo
Type=idle

# Path of directory pidfile should live in. Type=forking obeys this for child processes 
PIDFile=/run/service

# full path and arguments of the program to start
# if preceded with a '-' character, non-zero status exit will not mark the unit as failed
ExecStart=
# Command(s) to execute before ExecStart is executed
ExecStartPre=
# Command(s) to execute after ExecStart is executed
ExecStartPost=
# Command to execute when the systemd reload command is issued
ExecReload=
# Command to execute when the systemd stop command is issued
ExecStop= 
ExecStopPost=

# If auto-restart enabled, number of seconds to wait before restart
RestartSec=
# Command to execute when the systemd restart command is issues
Restart=
# Time in seconds to wait before force-kill or marking as failed after the systemd stop command is issued.
TimeoutSec=

# @todo Socket Type definitions
[Socket]
ListenStream=
ListenDatagram=
ListenSequentialPacket=
ListenFIFO=

# @todo Mount Type definitions
[Mount]

# @todo
[Automount]
[Swap]
[Path]
[Timer]
[Slice]


# End of "Unit Type specific directives"

# Optional, define behavior when the service is enabled or disabled
[Install]
# Service(s) that should enable this service. uses special symlinked directories to manage relationships
WantedBy=
RequiredBy=
# Enable to disable this service using a different name
Alias=
# Enable or disable these services as a set
Also=
# @todo
DefaultInstance=

```

**Template Unit Files**

Template unit files have an `@` character after their name, but before the service-type extension.

Example: `example@.service`, `corp-cdn@.mount`

Some things I do not know:

- What are unit templates?
- How do I use them?
- What are common use cases for unit templates?
- What are good practices for using unit templates?

Need help? Drop me a line code@mashio.net