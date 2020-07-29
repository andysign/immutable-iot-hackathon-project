pinum=$(hostname|tr "raspberrypi" "\n"|tail -1)
/bin/bash -c "cd /home/pi/${pinum}; source bin/activate; python gui.py"
