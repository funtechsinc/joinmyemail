from fastapi import APIRouter
from models.pydantic_model import User, UserHandle, WelcomeMessage
import all_routes
from operations.auth import auth_update_profile, update_handle, auth_set_welcome_message

profile_route = APIRouter()


# update profile
@profile_route.patch(all_routes.auth_update)
def update_user_profile(doc: User, uuid:str):
    uuid = uuid
    doc = doc.model_dump(exclude_unset=True)
    doc = dict(doc)
    res = auth_update_profile(doc, uuid)
    return res


# create handle
@profile_route.patch(all_routes.auth_create_user_handle)
def create_handle(doc: UserHandle, uuid: str):
    uuid = uuid
    doc = dict(doc)
    res = update_handle(doc, uuid)
    return res


# welcome message
@profile_route.patch(all_routes.auth_create_welcome_message)
def create_handle(doc: WelcomeMessage, uuid: str):
    uuid = uuid
    doc = dict(doc)
    res = auth_set_welcome_message(doc, uuid)
    return res

