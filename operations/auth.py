from connection import db_session
from functions.Generate_Hash import hash_function
from models.sql_model import UserTable
from functions.Generate_Hash import verify_hash
from decoders.user import decode_user
import json


# login account
def auth_get_user(uuid: str) -> dict:
    result = db_session.query(UserTable).filter(UserTable.uuid == uuid).one_or_none()
    if result is None:
       return {
                'status': 'error',
                'message': 'Invalid credentials'
            }
    else:
        return {
            'status': 'ok',
            'message': 'login successfully',
            'user': decode_user(result)
        }


# create a user
def auth_continue_with_google(doc: dict) -> dict:
    try:
        doc = doc
        email = doc["email"]
        uuid = doc["id"]
        verified_email = doc['verified_email']
        username = doc['name']
        photo = doc['picture']
        access_token = doc['access_token']

        # check is user already exist
        result = db_session.query(UserTable).filter(UserTable.email == email).one_or_none()

        if result is None:
            # req
            req = UserTable(
                uuid,
                username,
                email,
                verified_email,
                access_token,
                photo
            )

            # add and commit changes
            db_session.add(req)
            db_session.commit()

            # login after creating an account
            return auth_get_user(uuid)
        else:
            result.gmail_access_token = access_token
            db_session.commit()
            return auth_get_user(uuid)

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
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
        if 'category' in doc:
            result.category = doc["category"]
        if 'welcome_message' in doc:
            result.welcome_message = doc["welcome_message"]
        if 'youtube' in doc:
            result.youtube = doc["youtube"]
        if 'instagram' in doc:
            result.instagram = doc["instagram"]
        if 'x' in doc:
            result.x = doc["x"]

        db_session.commit()
        return {
            'status': 'ok',
            'message': 'profile updated',
        }


# update handle
def update_handle(doc: dict) -> dict:
    uuid = doc['uuid']
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
    server = doc['server']

    result = db_session.query(UserTable).filter(UserTable.uuid == uuid).one_or_none()
    if str(result) != "None":
        result.welcome_message = message
        result.smtp_for_welcome_message = server
        db_session.commit()
        return {
            'status': 'ok',
            'message': '''Voila! 🎉 You've just crafted a heartfelt welcome email for new subscribers. ✨''',
        }


# print(auth_continue_with_google({"id":"107239095561327300729","email":"abdulwahabiddris08@gmail.com","verified_email":True,"name":"Iddris Abdul Wahab","given_name":"Iddris","family_name":"Abdul Wahab","picture":"https://lh3.googleusercontent.com/a/ACg8ocLnsCU9GKOiecIXIgadoGBmDExGcRgbppL-QC7R3eGHvbn-20Zk=s96-c","locale":"en","access_token":"ya29.a0AXooCguqLSWvOSRhg5UaRHvSz643sTHvXUrOz2ePiroSn3ePFBmIENX0zb7iiGke2icrkQ1mVFkCQ81MEMsJtaeS4NWXDhnYZtgVITnvSwNVs_yuAOtUqfx68l_7FiJGklkc8lOAS7uY1Knis7f9JYwY9XIPZtr40WekaCgYKAYgSARISFQHGX2Mi_5-cqW7JWHF9uvGZRqD24A0171"}))
# print(update_handle({'uuid': '107239095561327300729', 'handle': 'codewithfuntechs'}))
# print(auth_set_welcome_message({'message': 'Hello, welcome to my new email list', 'server': 1} , '107239095561327300729'))

# print(auth_login("demo@example.com", "demo_password"))

# update = {
#     'category': 'Programming',
#     'x': 'funtechs',
#     'welcome_message': 'Thanks for joining my email list'
# }
#
# print(auth_update_profile(update, '107239095561327300729'))
#

# user = {
#     "username": "Funtechs",
#     "email": "funtechs45@gmail.com",
#     "password": "admin",
#     "company": "Create With Funtechs",
# }
# print(auth_register(user))
