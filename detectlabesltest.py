import boto3

BUCKET = "yourbucket"
key = "testimage.jpg"

def detect_lables(bucket, key, max_labels=10, min_confidence=50, region="us-east-1"):
    rekognition = boto3.client("rekognition",region)
    response = rekognition.detect_labels(
		Image={

			"S3Object": {

				"Bucket": bucket,

				"Name": key,

			}

		},

		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
    return response['Labels']


for label in detect_lables(BUCKET, key):
    print (label)
    
