import firebase_admin
from firebase_admin import credentials, storage
import os

# Initialize Firebase
cred = credentials.Certificate("firebase-key.json")

firebase_admin.initialize_app(cred, {
    "storageBucket": "mlops-assignment-1-64845.appspot.com"
})

bucket = storage.bucket()

def upload(local_path, remote_path):
    blob = bucket.blob(remote_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} -> {remote_path}")

upload("data/versions/v1/diabetes.json", "datasets/diabetes/v1/diabetes.json")
upload("data/versions/v2/diabetes.json", "datasets/diabetes/v2/diabetes.json")
