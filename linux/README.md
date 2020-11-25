# Linux

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
parted -s /dev/sda -- mkpart primary ext4 1 -1s

## Format
mkfs.ext4 /dev/sda1

## Find the UUID of the new partition
lsblk -o UUID /dev/sda1

## Add the partition to fstab for auto-mount on boot
UUID=$(lsblk -o UUID /dev/sda1 | tail -n 1)
echo "UUID=$UUID       /mnt/data/somewhere     ext4    defaults,nofail" \
	| tee -a /etc/fstab

```
