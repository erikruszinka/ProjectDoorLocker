#!/bin/bash
DATE=`date +%Y_%m_%d_%H_%M_%S`
echo $DATE
mkdir $DATE
cd $DATE
raspistill -o cam.jpg
