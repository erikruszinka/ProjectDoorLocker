import RPi.GPIO as GPIO
import time
import os
pinShutdown = 26
pinTestButton = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
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
    else:
        time.sleep(1)
