sudo systemctl stop gethnode.service
cd ~/pi$(hostname|tr "raspberrypi" "\n"|tail -1)/
./reset-and-init.sh
sudo systemctl start gethnode.service
