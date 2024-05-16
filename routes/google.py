from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from google.oauth2 import credentials
from google.auth.transport import requests
import requests
from operations.auth import auth_continue_with_google
import all_routes
from fastapi.responses import RedirectResponse


google_route = APIRouter()

CLIENT_ID = '915514989018-l7vqvr9dism79papm9jgres9gapshfbc.apps.googleusercontent.com'
CLIENT_SECRET = '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'

REDIRECT_URI = 'http://127.0.0.1:8000/auth/callback'


def get_authorization_uri():
    authorization_uri = (
        'https://accounts.google.com/o/oauth2/v2/auth?'
        'client_id={}&response_type=code&redirect_uri={}&scope=email%20profile&'
        'access_type=offline'.format(CLIENT_ID, REDIRECT_URI)
    )
    return authorization_uri


def exchange_code_for_token(authorization_code: str) -> str:
    token_request_data = {
        'code': authorization_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    token_endpoint = "https://oauth2.googleapis.com/token"
    response = requests.post(token_endpoint, data=token_request_data)
    if response.status_code == 200:
        token_response = response.json()
        access_token = token_response.get('access_token')
        return access_token
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


@google_route.get(all_routes.auth_login)
async def login(request: Request):
    authorization_uri = get_authorization_uri()
    return {
        'status': 'ok',
        'login_url': str(authorization_uri)
    }


GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"


@google_route.get("/auth/callback")
async def auth_callback(request: Request, code: str):
    access_token = exchange_code_for_token(code)
    access_token = str(access_token)

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(GOOGLE_USERINFO_URL, headers=headers)
    if response.status_code == 200:
        user_details = response.json()
        user_details = dict(user_details)
        user_details['access_token'] = access_token
        user_details['verified_email'] = True if str(user_details['verified_email']) is True else False
        res = auth_continue_with_google(user_details)
        return res
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


