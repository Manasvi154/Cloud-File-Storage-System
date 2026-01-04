from flask import Flask, render_template, request, redirect, url_for, send_file
import boto3
from werkzeug.utils import secure_filename
import io

app = Flask(__name__)

# S3 configuration
S3_BUCKET = "cloud-file-storage-manasvi"   
S3_REGION = "ap-south-1"

s3 = boto3.client("s3", region_name=S3_REGION)

@app.route('/')
def index():
    response = s3.list_objects_v2(Bucket=S3_BUCKET)

    files = []

    if 'Contents' in response:
        for obj in response['Contents']:
            size_kb = obj['Size'] / 1024
            if size_kb < 1024:
                size = f"{size_kb:.1f} KB"
            else:
                size = f"{size_kb/1024:.1f} MB"

            files.append({
                "name": obj['Key'],
                "type": obj['Key'].split('.')[-1].upper(),
                "size": size
            })

    return render_template(
        'index.html',
        files=files,
        total_files=len(files)
    )


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)

    s3.upload_fileobj(file, S3_BUCKET, filename)

    return redirect(url_for('index'))


@app.route('/download/<filename>')
def download_file(filename):
    file_obj = io.BytesIO()

    s3.download_fileobj(S3_BUCKET, filename, file_obj)
    file_obj.seek(0)

    return send_file(
        file_obj,
        as_attachment=True,
        download_name=filename
    )


@app.route('/delete/<filename>')
def delete_file(filename):
    s3.delete_object(Bucket=S3_BUCKET, Key=filename)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
