import RPi.GPIO as GPIO
import time
pin = 16
pin2 = 19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.output(pin,GPIO.HIGH)
time.sleep(1)
GPIO.output(pin,GPIO.LOW)
GPIO.output(pin2,GPIO.HIGH)
time.sleep(1)
GPIO.output(pin2,GPIO.LOW)
