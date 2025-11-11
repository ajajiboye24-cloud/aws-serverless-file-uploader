# AWS Serverless File Uploader

This project demonstrates a fully serverless file upload pipeline built with **AWS Lambda**, **API Gateway**, and **S3**.

## 🚀 Features
- Generate pre-signed URLs for secure S3 uploads  
- Automatically processes uploaded files via Lambda triggers  
- Logs events in CloudWatch  
- Uses IAM roles for least-privilege security  

## 🧠 AWS Services Used
- Lambda (Python 3.11)
- S3 (Uploads + Processed Buckets)
- API Gateway
- IAM
- CloudWatch

## 🧪 How It Works
1. Frontend or script requests a pre-signed URL from API Gateway (→ Lambda 1).
2. File is uploaded directly to S3.
3. Upload triggers another Lambda (→ Lambda 2) to process or move the file.
4. Logs confirm success in CloudWatch.

## 🧰 Future Enhancements
- Add SNS notifications on success  
- Send user confirmation emails  
- Add DynamoDB tracking table
