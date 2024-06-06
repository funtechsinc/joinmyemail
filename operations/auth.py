from connection import db_session
from functions.Generate_Hash import hash_function
from models.sql_model import UserTable
from functions.Generate_Hash import verify_hash
from decoders.user import decode_user
import json
import time


# get user
def auth_get_user(uuid: int):
    criteria = {'uuid': uuid}
    res = db_session.query(UserTable).filter_by(**criteria).one_or_none()
    if res is not None:
        return {
            'status': 'ok',
            'user': decode_user(res)
        }
    else:
        return {
            'status': 'error',
            'message': f'wrong uuid for : {uuid}'
        }


# get user with handle
def auth_get_user_with_handle(handle: str):
    criteria = {'handle': handle}
    res = db_session.query(UserTable).filter_by(**criteria).one_or_none()
    if res is not None:
        return {
            'status': 'ok',
            'user': decode_user(res)
        }
    else:
        return {
            'status': 'error',
            'message': f'wrong uuid for : {handle}'
        }


# login account
def auth_login(email: str, password: str) -> dict:
    result = db_session.query(UserTable).filter(UserTable.email == email).one_or_none()
    if str(result) != "None":
        verified = verify_hash(password, result.password)

        if verified:
            return {
                'status': 'ok',
                'message': 'user verified',
                'user': decode_user(result)
            }
        else:
            return {
                'status': 'error',
                'message': 'Invalid credentials'
            }

    else:
        return {
            'status': 'error',
            'message': 'Invalid credentials'
        }


# create a user
def auth_create_account(doc: dict) -> dict:
    doc = doc
    email = doc["email"]
    password = doc['password']

    # check is user already exist
    result = db_session.query(UserTable).filter(UserTable.email == email).one_or_none()

    if str(result) == "None":
        # hash password
        hash_password = hash_function(password)
        doc["password"] = hash_password
        username = doc["username"]

        # req
        req = UserTable(
            username,
            email,
            hash_password
        )

        # add and commit changes
        db_session.add(req)
        db_session.commit()

        res = auth_login(email, password)
        return res

    else:
        return {
            'status': 'error',
            'message': f'user already exist with email: {email}'
        }


# updating profile
def auth_update_profile(doc: dict, uuid) -> dict:
    uuid = uuid
    result = db_session.query(UserTable).filter(UserTable.uuid == uuid).one_or_none()
    if str(result) != "None":
        if 'username' in doc:
            result.username = doc["username"]
        if 'company' in doc:
            result.company = doc["company"]
        if 'title' in doc:
            result.title = doc["title"]
        if 'sub_title' in doc:
            result.sub_title = doc["sub_title"]
        if 'photo_url' in doc:
            result.photo_url = doc["photo_url"]
        if 'category' in doc:
            result.category = doc["category"]
        if 'welcome_message' in doc:
            result.welcome_message = doc["welcome_message"]
        if 'welcome_message_subject' in doc:
            result.welcome_message_subject = doc["welcome_message_subject"]
        if 'call_to_action' in doc:
            result.call_to_action = doc["call_to_action"]
        if 'youtube' in doc:
            result.youtube = doc["youtube"]
        if 'instagram' in doc:
            result.instagram = doc["instagram"]
        if 'x' in doc:
            result.x = doc["x"]
        if 'about' in doc:
            result.about = doc["about"]
        if 'buy_me_a_coffe' in doc:
            result.buy_me_a_coffe = doc["buy_me_a_coffe"]

        db_session.commit()
        return {
            'status': 'ok',
            'message': 'profile updated',
        }


# update handle
def update_handle(doc: dict, uuid: int) -> dict:
    handle = doc['handle']
    result = db_session.query(UserTable).filter(UserTable.handle == handle).one_or_none()
    if result is not None:
        return {
            'status': 'error',
            'message':  'handle already Exist: Try creating a unique handle' if result.uuid != uuid else '👏 Handle updated successfully',
        }
    else:
        result = db_session.query(UserTable).filter(UserTable.uuid == uuid).one_or_none()
        if result is not None:
            result.handle = doc["handle"]
            db_session.commit()
            return {
                'status': 'ok',
                'message': '👏 Handle updated successfully',
            }
        else:
            return {
                'status': 'error',
                'message': F'No record for Id {uuid}'
            }


def auth_set_welcome_message(doc: dict, uuid) -> dict:
    uuid = uuid
    message = doc['message']
    welcome_message_subject = doc['welcome_message_subject']
    server = doc['server_id']

    result = db_session.query(UserTable).filter(UserTable.uuid == uuid).one_or_none()
    if str(result) != "None":
        result.welcome_message = message
        result.welcome_message_subject = welcome_message_subject
        result.smtp_for_welcome_message = server
        db_session.commit()
        return {
            'status': 'ok',
            'message': '''Voila! 🎉 You've just crafted a heartfelt welcome email for new subscribers. ✨''',
        }
