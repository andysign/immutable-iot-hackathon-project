# ln -s /home/pi/pi$(hostname|tr "raspberrypi" "\n"|tail -1)/Desktop/ /home/pi/
pinum=$(hostname|tr "raspberrypi" "\n"|tail -1)
/bin/bash -c "cd /home/pi/${pinum}; source bin/activate; python gui.py"
