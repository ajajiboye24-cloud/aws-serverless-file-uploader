import json
import boto3
import os

s3 = boto3.client('s3')
BUCKET = os.environ['UPLOAD_BUCKET']

def lambda_handler(event, context):
    try:
        body = {}
        if event.get("body"):
            body = json.loads(event["body"])

        filename = body.get("filename", "default.txt")

        presigned_url = s3.generate_presigned_url(
            'put_object',
            Params={"Bucket": BUCKET, "Key": filename},
            ExpiresIn=3600
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "uploadURL": presigned_url,
                "key": filename
            })
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
