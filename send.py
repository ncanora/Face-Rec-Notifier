import base64
import mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
from face_rec import *
import cv2

SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)


while (True):
    s = input("Press enter to scan for face again: ")
    if (s == ""):
        face, attach = mainCapture()
        cv2.imwrite('./faces/{}.jpg'.format(face), attach)
        message = MIMEText('Face recognized: ' + face)
        message['to'] = 'njc2@williams.edu'
        message['subject'] = 'Face recognized!'
        service = build('gmail', 'v1', credentials=creds)

        with open('./faces/{}.jpg'.format(face), 'rb') as image_file:
            image_data = image_file.read()
            image = MIMEImage(image_data, _subtype=sub_type)
            image.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
            message.attach(image)

        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


        try:
            message = (service.users().messages().send(userId="me", body=create_message).execute())
            print(F'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(F'An error occurred: {error}')
            message = None