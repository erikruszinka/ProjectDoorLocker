import RPi.GPIO as GPIO
import time
import os
pinShutdown = 26
pinTestButton = 21
pin = 16
pin2 = 19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.output(pin2,GPIO.HIGH)
GPIO.setup(pinShutdown,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinTestButton,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    input_state_shutdown = GPIO.input(pinShutdown)
    input_state_testPin = GPIO.input(pinTestButton)
    if input_state_shutdown == False:
        print('pressed Shutdown')
        os.system("shutdown -h now")
    elif input_state_testPin == False:
        print('pressed Test')
        GPIO.output(pin2,GPIO.LOW)
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)
    else:
        time.sleep(1)
