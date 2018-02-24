import RPi.GPIO as GPIO
import time
pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
print "LED on"
GPIO.output(pin,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(pin,GPIO.LOW)
