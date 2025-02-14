# Generated by pykickstart v3.48
#version=DEVEL
# Firewall configuration
firewall --enabled --service=mdns
# Keyboard layouts
keyboard 'de'
# System language
lang en_US.UTF-8
# Network information
network  --bootproto=dhcp --device=link --activate
# Shutdown after installation
shutdown
repo --name="BaseOS" --baseurl=http://dl.rockylinux.org/pub/rocky/9/BaseOS/$basearch/os/ --cost=200
repo --name="AppStream" --baseurl=http://dl.rockylinux.org/pub/rocky/9/AppStream/$basearch/os/ --cost=200
repo --name="CRB" --baseurl=http://dl.rockylinux.org/pub/rocky/9/CRB/$basearch/os/ --cost=200
repo --name="extras" --baseurl=http://dl.rockylinux.org/pub/rocky/9/extras/$basearch/os --cost=200
repo --name="epel" --baseurl=https://dl.fedoraproject.org/pub/epel/9/Everything/$basearch/ --cost=200
repo --name=rt --baseurl=https://dl.rockylinux.org/pub/rocky/9.5/RT/x86_64/os/ --cost=200 --install

# Root password
rootpw --plaintext user
user --name user --plaintext --password user

# SELinux configuration
selinux --enforcing
# System services
services --disabled="sshd" --enabled="NetworkManager,ModemManager"
# System timezone
timezone US/Eastern
eula --agreed
# Use network installation
url --url="http://dl.rockylinux.org/pub/rocky/9/BaseOS/$basearch/os/"
# X Window System configuration information
xconfig  --startxonboot
# System bootloader configuration
bootloader --location=none
# Clear the Master Boot Record
zerombr
# Partition clearing information
clearpart --all
# Disk partitioning information
part / --fstype="ext4" --size=5120
part / --size=8192

%post
systemctl enable livesys.service
systemctl enable livesys-late.service
# Enable tmpfs for /tmp - this is a good idea
systemctl enable tmp.mount

# make it so that we don't do writing to the overlay for things which
# are just tmpdirs/caches
# note https://bugzilla.redhat.com/show_bug.cgi?id=1135475
cat >> /etc/fstab << EOF
vartmp   /var/tmp    tmpfs   defaults   0  0
EOF

# PackageKit likes to play games. Let's fix that.
rm -f /var/lib/rpm/__db*
releasever=$(rpm -q --qf '%{version}\n' --whatprovides system-release)
basearch=$(uname -i)
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-9
echo "Packages within this LiveCD"
rpm -qa
# Note that running rpm recreates the rpm db files which aren't needed or wanted
rm -f /var/lib/rpm/__db*

# go ahead and pre-make the man -k cache (#455968)
/usr/bin/mandb

# make sure there aren't core files lying around
rm -f /core*

# remove random seed, the newly installed instance should make it's own
rm -f /var/lib/systemd/random-seed

# convince readahead not to collect
# FIXME: for systemd

echo 'File created by kickstart. See systemd-update-done.service(8).' \
    | tee /etc/.updated >/var/.updated

# Drop the rescue kernel and initramfs, we don't need them on the live media itself.
# See bug 1317709
rm -f /boot/*-rescue*

# Disable network service here, as doing it in the services line
# fails due to RHBZ #1369794 - the error is expected
systemctl disable network

# Remove machine-id on generated images
rm -f /etc/machine-id
touch /etc/machine-id

# relabel
/usr/sbin/restorecon -RF /

%end

%post --nochroot
# only works on x86_64
if [ "unknown" = "i386" -o "unknown" = "x86_64" ]; then
    # For livecd-creator builds. livemedia-creator is fine.
    if [ ! -d /LiveOS ]; then mkdir -p /LiveOS ; fi
    cp /usr/bin/livecd-iso-to-disk /LiveOS
fi

%end

%post
# mate configuration

sed -i 's/^livesys_session=.*/livesys_session="mate"/' /etc/sysconfig/livesys

# this doesn't come up automatically. not sure why.
systemctl enable --force lightdm.service

# CRB needs to be enabled for EPEL to function.
dnf config-manager --set-enabled crb
dnf install rt-kernel -y
dnf install python3 -y
dnf install podman-compose podman -y
%end

%packages
@anaconda-tools
@base-x
@core
@dial-up
@fonts
@guest-desktop-agents
@hardware-support
@input-methods
@standard
NetworkManager-adsl
NetworkManager-bluetooth
NetworkManager-l2tp-gnome
NetworkManager-libreswan-gnome
NetworkManager-openconnect-gnome
NetworkManager-openvpn-gnome
NetworkManager-ovs
NetworkManager-ppp
NetworkManager-pptp-gnome
NetworkManager-team
NetworkManager-wifi
NetworkManager-wwan
aajohan-comfortaa-fonts
anaconda
anaconda-install-env-deps
anaconda-live
atril
atril-caja
atril-thumbnailer
caja
caja-actions
chkconfig
dconf-editor
dracut-live
efi-filesystem
efibootmgr
efivar-libs
engrampa
eom
epel-release
f36-backgrounds-extras-mate
f36-backgrounds-mate
f37-backgrounds-extras-mate
f37-backgrounds-mate
filezilla
firefox
firewall-applet
firewall-config
gjs
glibc-all-langpacks
gnome-disk-utility
gnome-epub-thumbnailer
gnome-themes-extra
gparted
grub2-common
grub2-efi-*64
grub2-efi-*64-cdboot
grub2-pc-modules
grub2-tools
grub2-tools-efi
grub2-tools-extra
grub2-tools-minimal
grubby
gstreamer1-plugins-ugly-free
gtk2-engines
gucharmap
gvfs-fuse
gvfs-gphoto2
gvfs-mtp
gvfs-smb
hexchat
initial-setup-gui
initscripts
kernel
kernel-rt
kernel-modules
kernel-modules-extra
libmatekbd
libmatemixer
libmateweather
libsecret
lightdm
livesys-scripts
lm_sensors
marco
mate-applets
mate-backgrounds
mate-calc
mate-control-center
mate-desktop
mate-dictionary
mate-disk-usage-analyzer
mate-icon-theme
mate-media
mate-menu
mate-menus
mate-menus-preferences-category-menu
mate-notification-daemon
mate-panel
mate-polkit
mate-power-manager
mate-screensaver
mate-screenshot
mate-search-tool
mate-sensors-applet
mate-session-manager
mate-settings-daemon
mate-system-log
mate-system-monitor
mate-terminal
mate-themes
mate-user-admin
mate-user-guide
mate-utils
memtest86+
mozo
network-manager-applet
nm-connection-editor
orca
p7zip
p7zip-plugins
parole
pavucontrol
pipewire-alsa
pipewire-pulseaudio
pluma
pluma-plugins
podman
podman-compose
python3
rocky-backgrounds
rocky-backgrounds-compat
rocky-release
seahorse
seahorse-caja
setroubleshoot
shim-*64
slick-greeter-mate
syslinux
tigervnc
usermode-gtk
vim-enhanced
wireplumber
xdg-user-dirs-gtk
xmodmap
xrdb
yelp
-@3d-printing
-@admin-tools
-audacious
-brasero
-evolution-help
-fedora-icon-theme
-gnome-icon-theme
-gnome-icon-theme-symbolic
-gnome-logs
-gnome-software
-gnome-user-docs
-hplip
-isdn4k-utils
-mpage
-sane-backends
-shim-unsigned-*64
-systemd-oomd-defaults
-telnet
-xane-gimp
-xsane

%end