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
    
    exit()
else:
    print('Valid card')

time.sleep(2)
print("SMILE!")
time.sleep(1)
camera = PiCamera()
camera.capture("/home/pi/captured/"+cardID+".jpg")

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
        #SimilarityThreshold=0
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
print(foto)

if response:
    pprint.pprint(response)
else:
    print('nope')
    
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
         "success": 'Good'
        }
    )
    
    
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
    #similarity = load['FaceMatches'][0]['Similarity']
    #print(similarity)


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
    
