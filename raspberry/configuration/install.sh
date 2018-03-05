#!/bin/bash
clear
echo "IMPORTANT! Project need to be cloned directly in to: /home/pi/"
echo "Executed script path is /home/pi/ProjectDoorLocker/install.sh"
echo "If is path correct you can continue by [ENTER]"
read var_continue
clear
sudo cat /etc/rc.local > /home/pi/ProjectDoorLocker/raspberry/configuration/localBackup
sudo rm /etc/rc.local
sudo cat bashConfig > /etc/rc.local
sudo apt update
sudo apt upgrade
echo "Please change your password!"
echo "Current password for user 'pi' is 'raspberry'"
sudo passwd
echo ""
echo "It is necessary to allow using camera. Option 6"
echo "I recommend you to expand your file system. Option 1"
echo "Press [ENTER] for continue..."
read var_continue
sudo raspi-config
sudo reboot
