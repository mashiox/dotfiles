# Linux

## References

- https://abarrak.gitbook.io/linux-sysops-handbook/
- https://beej.us/guide/

# Network

Problem:
List all programs listening for a network connection

```bash
$ netstat -tunlp
```

Argument disambiguation:

`-t` or `--tcp` displays TCP network connections

`-u` or `--udp` displays UDP network connections

`-n` or `--numeric` Shows numeric IP addresses instead of attempting to discover host

`-l` or `--listening` Shows active listening sockets

`-p` or `--program` Shows the Process ID (PID) and Program name that the socket belongs to

Problem:
Send packets from a specific network interface
Example using ping

```bash
$ ping -I wg0 -C4 example.com
$ ping -I 10.0.0.1 -C4 example.com
```

Argument disambiguation:

`-I` takes an address or interface name. It works differently depending on if an address or interface is provided.

# Drive Management

## Checking a filesystem for bad blocks

Use `mkfs`

```bash
mkfs -c /dev/sda
mkfs -c /dev/sda1
```

## Partitioning a new disk

### Reading

- https://techtitbits.com/2018/12/using-parteds-resizepart-non-interactively-on-a-busy-partition/
- https://www.gnu.org/software/parted/manual/html_node/mkpart.html
- http://raspberrypiwiki.com/Properly_Mount_USB_Storage_on_Raspberry_Pi
- https://linoxide.com/linux-command/parted-commands-manage-disk-partition/

You can discover more about drives attached to the computer with the following tools.
Drives will always be under `/dev/`.

Drives attached via SCSI or SATA will be labeled `/dev/sd*`
Drives attached via IDE ribbons will be labeled `/dev/hd*`

```bash
lsblk

parted -l

fdisk -l
```

When we partition a disk, we want to prefer `parted` because it can create a Globally Unique Identifiers Partition Table, which help administrators mount drives without needing to use MSDos partition maps in `/etc/fstab`.
If we opt for the older `fdisk`, or `cfdisk`, we will be constrained to using MSDos partition maps.

According to techtitbits.com ,in 2018, there is some difficulty in using the `parted` command in noninteractive mode. Under certain conditions, like using a TTY-less SSH session, noninteractive mode may behave unpredictably, and will require the use of `---pretend-input-tty`.

```bash
# Noninteractive parted

## Create 1 partition of largest size
parted -s /dev/sda mklabel msdos
parted -s /dev/sda mkpart primary ext4 0% 100%

## Format
mkfs.ext4 /dev/sda1

## Find the UUID of the new partition
lsblk -o UUID /dev/sda1

## Add the partition to fstab for auto-mount on boot
UUID=$(lsblk -o UUID /dev/sda1 | tail -n 1)
echo "UUID=$UUID       /mnt/data/somewhere     ext4    defaults,nofail" \
	| tee -a /etc/fstab

```

## Deleting a partition

Reference `$partition_number` from either `parted print all` or the natural partition number `/dev/sdN`

```bash
parted rm $partition_number
```

## Reloading filesystem table /etc/fstab

Reload fstab without re-mounting mountpoints that are already mounted

```bash
mount -av
```

# Management

## Logrotate

Reading:

- https://linuxconfig.org/logrotate
- https://linux.die.net/man/8/logrotate
- https://www.systutorials.com/docs/linux/man/5-logrotate.conf/
- [Examples](https://www.tutorialspoint.com/unix_commands/logrotate.htm)
- https://askubuntu.com/questions/405663/configuring-logrotate-without-root-access-per-user-log-rotation

