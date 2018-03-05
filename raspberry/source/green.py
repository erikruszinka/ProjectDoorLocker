import RPi.GPIO as GPIO
import time
pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
print "LED GREEN"
GPIO.output(pin,GPIO.HIGH)
