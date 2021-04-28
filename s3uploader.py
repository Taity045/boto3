from aws_keys import access_key , secret_access_key

import boto3
import os


#Interact with client
client = boto3.client('s3',
                       aws_access_key_id = access_key,
                       aws_secret_access_key = secret_access_key)

for file in os.listdir():
    if '.pdf' in file:
        upload_file_bucket = 'uploads3files'
        upload_file_key = 'pdffiles/' + str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)


for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'uploads3files'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)

print('Upload Successful')       