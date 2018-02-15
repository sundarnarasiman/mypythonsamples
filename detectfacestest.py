import boto3

BUCKET = 'youtbucket'
KEY = 'testimage.jpg'

def detect_faces(bucket, key, attributes=['ALL'], region="us-east-1"):    
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_faces(
	    Image={

			"S3Object": {

				"Bucket": bucket,

				"Name": key,

			}
		},
	    Attributes=attributes,
	)

	return response['FaceDetails']

for face in detect_faces(BUCKET, KEY):
 print ("Face ({Confidence}%)".format(**face))
 for emotion in face['Emotions']:
     print ("  {Type} : {Confidence}%".format(**emotion))
