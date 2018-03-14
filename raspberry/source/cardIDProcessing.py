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
import RPi.GPIO as GPIO

pin = 20
pin2 = 26
pinRed = 19
pinGreen = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pinRed,GPIO.OUT)
GPIO.setup(pinGreen,GPIO.OUT)
GPIO.output(pin,GPIO.HIGH)

cardID = str(sys.argv[1])

client = MongoClient('mongodb://Admin1:akademiasovy@ds229388.mlab.com:29388/recog')
db=client['recog']

isvalid=db.employees.find_one({"cardId":cardID})
print(isvalid)
#cardID = "19221252164"

print(cardID)
     

if isvalid == None:
    print('Invalid Card or User')
    db.acceshistories.insert_one(
        {"Access_time": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")],
         "First_Name": 'Unknown',
         "Last_Name": 'Unknown',
         "profilephoto": 'public/uploads/default.png',
         "success": "Invalid card"
        }
    )
    GPIO.output(pin,GPIO.LOW)
    exit()
else:
    print('Valid card')
GPIO.output(pin,GPIO.LOW)
time.sleep(2)
GPIO.output(pin,GPIO.HIGH)
print("SMILE!")
time.sleep(1)
camera = PiCamera()
camera.capture("/home/pi/captured/"+cardID+".jpg")
GPIO.output(pin,GPIO.LOW)
# Create an S3 client
s3 = boto3.client('s3')

filename = str("/home/pi/captured/"+cardID+".jpg")
bucket_name = 'sovyrekognition2'
filename2 = cardID+".jpg"

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename2)

print("COMPARE")

client = boto3.client('rekognition')
response = client.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': 'sovyrekognition2',
            'Name': 'employee_'+cardID+'.jpg'
            }
        },
    TargetImage={
        'S3Object': {
            'Bucket': 'sovyrekognition2',
            'Name': cardID+'.jpg'
            }
        },
        SimilarityThreshold=0
    )

#print(response)
respo=json.dumps(response)
load=json.loads(respo)

employee=isvalid
name=(employee['First_Name'])
last=(employee['Last_Name'])
foto=(employee['profilephoto'])
card=(employee['cardId'])
print(name)
print(last)
#print(foto)


    
if load['FaceMatches'] == []:
    print('face not recognized')
    db.acceshistories.insert_one(
        {"Access_time": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")],
         "First_Name": card,
         "Last_Name": 'Unknown',
         "profilephoto": 'public/uploads/default.png',
         "success": "Face not recognized"
        }
    )
    
    exit()

if load['FaceMatches'][0]['Similarity'] > 80:
    GPIO.output(pinRed,GPIO.LOW)
    GPIO.output(pinGreen,GPIO.HIGH)
    similarity = load['FaceMatches'][0]['Similarity']
    print(similarity)
    
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
    db.acceshistories.insert_one(
        {"Access_time": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")],
         "First_Name": name,
         "Last_Name": last,
         "profilephoto": foto,
         "success": 'Good ('+str(similarity)+'%)'
        }
    )
    time.sleep(2.5)
    GPIO.output(pinGreen,GPIO.LOW)
    GPIO.output(pinRed,GPIO.HIGH)
    
    
else:
    print('face not recognized')
    db.acceshistories.insert_one(
        {"Access_time": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")],
         "First_Name": card,
         "Last_Name": 'Unknown',
         "profilephoto": 'public/uploads/default.png',
         "success": "Face not recognized"
        }
    )
    


'''
#cardID = sys.argv[1]
#print(cardID)


SimilarityThreshold=80


client = boto3.client('rekognition')
response = client.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': 'sovyrekognition2',
            'Name': 'empo.jpg'
            }
        },
    TargetImage={
        'S3Object': {
            'Bucket': 'sovyrekognition2',
            'Name': '19221252164.jpg'
            }
        },
    SimilarityThreshold=80
    )

'''
    
