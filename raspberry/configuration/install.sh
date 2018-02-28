sudo passwd
sudo apt update
sudo apt upgrade
echo -n""
echo -n "It is necessary to allow using camera. Option 6"
echo -n "I recommend you to expand your file system. Option 1"
echo -n "Press [ENTER] for continue..."
read var_continue
sudo raspi-config
sudo apt-get install python-dev python~rpi.gpio
