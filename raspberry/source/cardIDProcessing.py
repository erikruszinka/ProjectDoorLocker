import os
import time
import datetime
import pprint
import sys
import pymongo
import boto3
from pymongo import MongoClient
from picamera import PiCamera

BUCKET = "sovyrekognition"
KEY_SOURCE = "Rihana2.jpg"
KEY_TARGET = "Rihana1.jpg"

def compare_faces(bucket, key, bucket_target, key_target, threshold=80, region="eu-west-1"):
    rekognition = boto3.client("rekognition",region)
    response = rekognition.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': bucket,
            'Name': key,
            }
        },
    TargetImage={
        'S3Object': {
            'Bucket': bucket_target,
            'Name': key_target,
            }
        },
    SimilarityThreshold=threshold,
    )
    return response['SourceImageFace'], response['FaceMatches']

source_face, matches = compare_faces(BUCKET, KEY_SOURCE, BUCKET, KEY_TARGET)









'''
cardID = sys.argv[1]
#print(cardID)


client = MongoClient('mongodb://Admin1:akademiasovy@ds229388.mlab.com:29388/recog')
db = client['recog']
   db.employees.update(
    
    {"cardId":cardID},
    {
        "$push": {
            "Logs": {
                "$each": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")],
                "$position": 0
            }
        }
    }
)


isvalid = db.employees.find_one({"cardId":cardID})

if isvalid == None:
    print('Invalid Card or User')
else:
    print('Valid card')
    
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
'''