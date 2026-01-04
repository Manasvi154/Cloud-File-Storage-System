# Cloud-Based File Storage System (AWS)

A cloud-based file storage web application built using Flask and AWS services that allows users to upload, view, download, and delete files securely from the cloud.

This project demonstrates real-world cloud concepts including compute, storage, IAM-based security, and deployment on AWS EC2 with a clean dashboard-style UI.

## Features

- Upload files to cloud storage (Amazon S3)
- View stored files with file name, file type, and file size
- Download files from cloud
- Delete files from cloud storage
- Clean and responsive dashboard UI
- Secure access using IAM Role (no hardcoded AWS credentials)

## System Architecture

User → Browser → EC2 (Flask App) → IAM Role → Amazon S3

- Users access the application through a web browser
- The backend is a Flask application hosted on an AWS EC2 instance
- Files are stored in an Amazon S3 bucket
- An IAM Role attached to EC2 securely grants access to S3
- No AWS access keys are stored in the code

## Workflow Overview

1. User performs an action from the web UI (upload, view, download, delete)
2. Request is sent to the Flask application on EC2
3. Flask processes the request and interacts with Amazon S3 using boto3
4. IAM Role authorizes the required S3 operation
5. Amazon S3 returns the response
6. Flask sends the updated response back to the browser

## Tech Stack

- Frontend: HTML, CSS
- Backend: Python, Flask
- Cloud Provider: AWS
- Compute: Amazon EC2
- Storage: Amazon S3
- Security: IAM Role
- SDK: boto3

## Project Structure

cloud-file-storage/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   └── style.css
└── templates/
    └── index.html

## Setup & Run

1. Clone the repository  
git clone https://github.com/Manasvi154/Cloud-File-Storage-System.git  

2. Navigate to project directory  
cd Cloud-File-Storage-System  

3. (Optional) Create virtual environment  
python -m venv venv  

4. Install dependencies  
pip install -r requirements.txt  

5. Run the application  
python app.py  

Application runs on http://localhost:5000

## AWS Configuration

- EC2 instance has an IAM Role attached
- IAM Role permissions include:
  - List objects in S3
  - Upload files
  - Download files
  - Delete files
- This avoids storing AWS credentials in code

## Best Practices Followed

- IAM Role–based authentication
- No AWS secrets in code
- Cloud-native storage using Amazon S3
- Clean separation of frontend and backend
- Cost-aware cloud usage

## Future Enhancements

- User authentication
- File search
- Folder support
- File sharing
- Storage analytics

## Author

Manasvi Pawar  
Cloud & Data Enthusiast
