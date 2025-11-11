import json
import boto3
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Event:", json.dumps(event))

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        # Just log the upload instead of copying
        print(f"✅ File uploaded successfully: {source_key} in {source_bucket}")

        return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully!')
        }

    except Exception as e:
        print(f"❌ Error processing file: {str(e)}")
        raise e
