from fastapi import APIRouter, HTTPException
from models.pydantic_model import AuthLogin, AuthRegister, User, UserHandle, WelcomeMessage
import all_routes
import operations.auth as Auth

auth_route = APIRouter()


# create account
@auth_route.post(all_routes.auth_register)
def register(doc: AuthRegister):
    doc = dict(doc)
    res = Auth.auth_create_account(doc)
    return res


# login account
@auth_route.post(all_routes.auth_login)
def login(doc: AuthLogin):
    doc = dict(doc)
    email = doc['email']
    password = doc['password']
    res = Auth.auth_login(email, password)
    return res


# user handle
@auth_route.patch(all_routes.auth_create_user_handle)
def create_handle(doc: UserHandle, uuid: int):
    doc = dict(doc)
    res = Auth.update_handle(doc, uuid)
    return res


# update user
@auth_route.patch(all_routes.auth_update)
def update_user(doc: User, uuid: int):
    doc = dict(doc.model_dump(exclude_unset=True))
    res = Auth.auth_update_profile(doc, uuid)
    return res


# welcome message
@auth_route.patch(all_routes.auth_update)
def welcome_message(doc: WelcomeMessage, uuid: int):
    doc = dict(doc)
    res = Auth.auth_set_welcome_message(doc, uuid)
    return res


# Get user
@auth_route.get(all_routes.auth_get_user)
def get_user(uuid: int):
    res = Auth.auth_get_user(uuid)
    return res


# Get user with handle
@auth_route.get(all_routes.auth_get_user_with_handle)
def get_user_with_handle(handle: str):
    res = Auth.auth_get_user_with_handle(handle)
    return res
