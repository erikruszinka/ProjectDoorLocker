import os
import time
import datetime
from picamera import PiCamera
camera = PiCamera()
camera.capture("/home/pi/captured/boo.jpg")
