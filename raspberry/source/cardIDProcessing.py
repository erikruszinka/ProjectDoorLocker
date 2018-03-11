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

#cardID = sys.argv[1]
cardID = "19221252164"

print(cardID)
"""
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
"""

time.sleep(2)
print("SMILE!")
time.sleep(1)
#ts = time.time()
#st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
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

'''client = boto3.client('rekognition')
response = client.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': 'sovyrekognition2',
            'Name': 'employee_19221252164.jpg'
            }
        },
    TargetImage={
        'S3Object': {
            'Bucket': 'sovyrekognition2',
            'Name': 'employee_19221252164.jpg'
            }
        },
        SimilarityThreshold=80
    )
'''
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


#print(response)
respo=json.dumps(response)
load=json.loads(respo)
print(load['FaceMatches'][0]['Similarity'])



'''
cardID = sys.argv[1]
#print(cardID)


SimilarityThreshold=80
    
'''