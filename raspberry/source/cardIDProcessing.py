import os
import time
import datetime
import pprint
import sys
import pymongo
import boto3
import json
from pymongo import MongoClient
from picamera import PiCamera

cardID = sys.argv[1]

print(cardID)

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
    return
else:
    print('Valid card')

time.sleep(2)
print("SMILE!")
time.sleep(1)
#ts = time.time()
#st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
camera = PiCamera()
camera.capture(str("/home/pi/captured/"+cardID+".jpg"))

# Create an S3 client
s3 = boto3.client('s3')

filename = str("/home/pi/captured/"+cardID+".jpg")
bucket_name = 'sovyrekognition2'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename,bucket_name, str(cardID+".jpg"))

client = boto3.client('rekognition')
response = client.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': 'sovyrekognition2',
            'Name': str(cardID+".jpg"),
            }
        },
    TargetImage={
        'S3Object': {
            'Bucket': 'sovyrekognition2',
            'Name': str("employe_"+cardID+".jpg"),
            }
        },
        SimilarityThreshold=80
    )
respo=json.dumps(response)
load=json.loads(respo)
print(load['FaceMatches'][0]['Similarity'])



'''
cardID = sys.argv[1]
#print(cardID)



    
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