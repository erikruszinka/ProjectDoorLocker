import os
import time
import datetime
import pprint
from pymongo import MongoClient
from picamera import PiCamera

isValid = False
# POROVNANIE CARD ID S DB
# AK SPRAVNE isValid = True
# INAK isValid = False
if isValid == True:
	print("KARTA ROZOZNANA")
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
	os.system("mkdir /home/pi/DoorLockerCaptured/"+st)
	camera = picamera.PiCamera()
	camera.capture("/home/pi/DoorLockerCaptured/"+st+"/image.jpg")
	# ZAPNUt KAMERU
	# UROBIT FOTO
	isRecognized = False
	print("NIECO")
	# VOLAT AWS A UROBIT POROVNANIE FOTO
	# AK ROZOZNANIE USPESNE isRecognized = True
	if isRecognized == True:
		print("ZAPIS DO DB USPESNE")
		# ZAPIS DO DB OVERENIE USPESNE
	else:
		print("ZAPIS DO DB NEUSPESNE")
		# ZAPIS DO DB NEUSPESNE
else:
print("ZAPIS DO DB NEUSPESNE ZLA KARTA")
# ZAPIS DO DB NEUSPESNE ZLA KARTA
