# AWS Serverless File Uploader
<img width="1550" height="516" alt="diagram-export-11-11-2025-2_29_48-PM" src="https://github.com/user-attachments/assets/91ff4148-dfcf-4603-b19e-594bea725a2a" />

<img width="1710" height="944" alt="Screenshot 2025-11-11 at 8 05 05 PM" src="https://github.com/user-attachments/assets/8b5f9c98-c1f7-4692-b9fb-af0ff2f3c0fa" />

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
