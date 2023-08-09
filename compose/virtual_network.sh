


sudo lsmod | grep dummy
sudo modprobe dummy
sudo lsmod | grep dummy

sudo ip link add dummy0 type dummy
sudo ip link add dummy1 type dummy

sudo ip link set name my_eth10 dev dummy0
ip link show my_eth10

sudo ip link delete dummy0 type dummy
sudo rmmod dummy