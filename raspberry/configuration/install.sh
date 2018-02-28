echo -n "IMPORTANT! Project need to be cloned directly in to:"
echo -n "/home/pi/"
echo -n "Executed script path is /home/pi/ProjectDoorLocker/install.sh"
sudo cat /home/pi/.bashrc > bashBackup
sudo cat bashConfig > /home/pi/.bashrc
sudo apt update
echo -n "Please change your password!"
echo -n "Current password for user 'pi' is 'raspberry'"
sudo passwd
echo -n""
echo -n "It is necessary to allow using camera. Option 6"
echo -n "I recommend you to expand your file system. Option 1"
echo -n "Press [ENTER] for continue..."
read var_continue
sudo raspi-config
sudo reboot
