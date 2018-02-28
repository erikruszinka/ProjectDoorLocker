import RPi.GPIO as GPIO
import time
import os
pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(pin)
    if input_state==False:
        print('pressed')
        os.system("shutdown -h now")
        time.sleep(1)
    else:
        time.sleep(1)
