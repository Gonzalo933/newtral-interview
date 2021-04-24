import boto3
import botocore

BUCKET_NAME = "ml-coding-test"
KEY = "claims.bson"
s3 = boto3.resource("s3")

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, "./data/raw/claims.bson")
except:
    print("Error while downloading new data version.")
