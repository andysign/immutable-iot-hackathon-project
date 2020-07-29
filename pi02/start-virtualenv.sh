num=$(hostname|tr "raspberrypi" "\n"|tail -1)
cd ~/pi${num}
[ -d "bin/" ] && echo "" || virtualenv --python=/usr/bin/python3.7 ~/pi${num}
source /home/pi/pi${num}/bin/activate
