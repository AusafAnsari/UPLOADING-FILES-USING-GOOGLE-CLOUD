from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import pickle

def upload_file(file_path, mime_type='application/octet-stream'):
    # Load credentials from token.pickle
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': file_path.split('/')[-1]}
    media = MediaFileUpload(file_path, mimetype=mime_type)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File uploaded sucessfully! File ID: {file.get('id')}")

if __name__=="__main__":
    file_path = "C:/Users/adminb/Desktop/voice command by hand gesture/hand_gesture.py" # Change this to files path
    upload_file(file_path)