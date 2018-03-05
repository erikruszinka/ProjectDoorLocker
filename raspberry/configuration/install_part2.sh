#!/bin/bash
echo "Project Door Locker instalation"
echo "If you need to abort it now then you need to run manualy: "
echo "sh /home/pi/ProjectDoorLocker/raspberry/configuration/install_part2.sh"
echo "Continue by pressing [ENTER]"
read var_continue
clear
sudo rm /etc/rc.local
sudo cat /home/pi/ProjectDoorLocker/raspberry/configuration/localAutostart > /etc/rc.local
sudo apt-get purge wolfram-engine
sudo apt-get purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
sudo apt-get install python-dev python~rpi.gpio
sudo apt-get install python2.7-dev python3-dev
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo python -m pip install pymongo
python -m pip install --upgrade pymongo
python -m pip install pymongo[gssapi]
sudo apt update
sudo apt upgrade
sudo apt-get install python-picamera
reboot
