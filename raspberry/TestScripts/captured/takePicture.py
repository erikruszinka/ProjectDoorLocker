import os
import time
import datetime
from picamera import PiCamera
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
os.system("mkdir /home/pi/DoorLockerCaptured/"+st)
camera = picamera.PiCamera()
camera.capture("/home/pi/DoorLockerCaptured/"+st+"/image.jpg")
