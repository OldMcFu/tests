set -e

sudo dnf install epel-release -y
sudo dnf config-manager --set-enabled crb
sudo dnf makecache

sudo dnf install -y lorax createrepo yum-utils

sudo dnf config-manager --set-enabled rt
sudo dnf install -y kernel-rt kernel-rt-devel
sudo dnf install -y qemu-kvm libvirt virt-install virt-manager bridge-utils

uname -r  # Should display the RT kernel version

sudo dnf clean all