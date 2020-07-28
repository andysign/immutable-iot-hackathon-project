# Immutable IoT Demo

Simple Internal Raspberry Pi Ethereum Blockchain.

---

# OS Setup Manually

The next section will help describe the steps needed to setup the ssh, the wifi and etherenet connections and everything that makes the every Pi in this network unique.

## Setting Up The OS And SSH

Download [Raspberry Pi OS 32-bit with desktop image](https://www.raspberrypi.org/downloads/raspberry-pi-os/) then Use Balena Etcher to burn it on your SD card (here I am using a 32GB SD card).

**Note**: You can backup the SD card with [SD Clone](https://twocanoes.com/products/mac/sd-clone/) or manually with DiskUtil as described in the [Clone Pi TutsPlus Tutorial](https://computers.tutsplus.com/articles/how-to-clone-raspberry-pi-sd-cards-using-the-command-line-in-os-x--mac-59911).

After that connect your raspberry to your favorite switch, like in my case the little 5 port switch from [Tenda](https://tendacn.com/en/product/SG105.html).

Connect for a your screen and activate ssh to be able to the resto of the work in headless more and type `sudo systemctl enable ssh
; sudo systemctl start ssh` or go trough the _sudo raspi-config_ as described in the [official website article](https://www.raspberrypi.org/documentation/remote-access/ssh/).

After that ssh with:

```sh
ssh pi@raspberrypi.local
```

## Setting Up The Hostname

Change the hostname from _raspberrypi_ to _raspberrypi**XX**_ trough where XX is the node number starting from _00_ and here you have two options, either manually or trough _sudo raspi-config_ by going to _2 Network Options_ then selecting _N1_.

## Setting Up The Wifi And Etherenet

Connect to your wireless network by walking trough all the steps from the [official configuration article](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md).

```bash
# /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=GB
network={
    ssid="AndroidGal7"
    psk=27e5be1ec90d7ec8b3ef13b8de8c2189cc940c0e5ce1a9ed51cc15718d62a0f8
}
```

Then finally setup the Raspberry Pi Wifi and Ethernet static ip as described in the [electrondust article](https://electrondust.com/2017/11/25/setting-raspberry-pi-wifi-static-ip-raspbian-stretch-lite/) as in edit the _dhcp_ config file.

In my case the file looks like this:


```sh
# /etc/dhcpcd.conf
hostname
clientid
persistent
option rapid_commit
option domain_name_servers, domain_name, domain_search, host_name
option classless_static_routes
option interface_mtu
require dhcp_server_identifier
slaac private
# Custom
interface eth0
#static ip_address=169.254.68.100
static ip6_address=fe80::a2:c34f:caa:ee00/64 # Change
static routers=169.254.68.1
static domain_name_servers=192.168.43.1
interface wlan0
static ip_address=192.168.43.100 # Change
static routers=192.168.43.1
static domain_name_servers=8.8.8.8 192.168.43.1
```

```sh
static ip6_address=fe80::a2:c34f:caa:ee01/64 # Second
# [...]
static ip_address=192.168.43.101 # Second
```

```sh
static ip6_address=fe80::a2:c34f:caa:ee02/64 # Thrid
# [...]
static ip_address=192.168.43.102 # Third
```

## Setup TFT Display Hardware Manually

In order to install all the drivers needed for the TFT 3.5 display just clone the official repo and execute the install script like:

```ah
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./MHS35-show
```

As described on the official [Lcd Wiki website](http://www.lcdwiki.com/MHS-3.5inch_RPi_Display).

---
