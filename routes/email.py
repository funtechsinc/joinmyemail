from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer

import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

email_route = APIRouter()

# Define the redirection URI
REDIRECT_URI = "http://127.0.0.1:8000/email/callback"

# Define the OAuth2 authorization scope
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# Define the OAuth2 authorization flow
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES, redirect_uri=REDIRECT_URI)

# Define the send_email route
@email_route.get('/mail')
async def send_email(request: Request):
    authorization_url, _ = flow.authorization_url(access_type='offline', prompt='consent')

    # Redirect to Google OAuth2 consent screen
    return RedirectResponse(url=authorization_url)


# Define the OAuth2 callback route
@email_route.get("/email/callback")
async def oauth2_callback(request: Request, code: str = None):
    if code:
        flow.fetch_token(code=code)

        # Get the credentials
        creds = flow.credentials

        # Build the Gmail service
        service = build('gmail', 'v1', credentials=creds)

        # Compose the email message
        message = MIMEText('This is the body of the email')
        message['to'] = 'abdulwahabiddris08@gmail.com'
        message['subject'] = 'Email Subject'
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            # Send the email
            message = service.users().messages().send(userId="me", body=create_message).execute()
            print(F'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(F'An error occurred: {error}')
    else:
        print("Authorization code is missing or invalid.")

    # Redirect to a success page or return some response indicating success
    return {"message": "Email sent successfully!"}
