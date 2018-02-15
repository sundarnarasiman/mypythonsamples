import boto3

BUCKET = "yourbucket"
KEY = "airpollution.jpg"

s3client = boto3.resource('s3')
data = open('airpollution.jpg', 'rb')

s3client.Bucket(BUCKET).put_object(Key='airpollution.jpg', Body=data)

print('upload succcessful')
