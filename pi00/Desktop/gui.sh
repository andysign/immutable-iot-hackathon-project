pinum=$(hostname|tr "raspberrypi" "\n"|tail -1)
/bin/bash -c "source /home/pi/pi00/bin/activate; python /home/pi/pi00/gui.py"
