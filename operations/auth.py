from connection import db_session
from functions.Generate_Hash import hash_function
from models.sql_model import UserTable
from functions.Generate_Hash import verify_hash
from decoders.user import decode_user
import json


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
def auth_register(doc: dict) -> dict:
    try:
        doc = doc
        email = doc["email"]
        password = doc["password"]

        # check is user already exist
        result = db_session.query(UserTable).filter(UserTable.email == email).one_or_none()

        if str(result) == "None":
            # hash password
            hash_password = hash_function(password)
            doc["password"] = hash_password

            username = doc["username"]
            company = doc["company"]

            # req
            req = UserTable(
                username,
                email,
                hash_password,
                company
            )

            # add and commit changes
            db_session.add(req)
            db_session.commit()

            # login after creating an account
            return auth_login(email, password)
        else:
            return {
                'status': 'error',
                'message': f'user already exist with email: {email}'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


# updating profile
def auth_update_profile(doc: dict) -> dict:
    uuid = doc['uuid']
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



# print(update_handle({'uuid': 2, 'handle': 'codewithfuntechs'}))
# print(auth_login("demo@example.com", "demo_password"))

# update = {
#     'uuid': 1,
#     'category': 'Programming',
#     'handle': 'createwithfuntechs'
# }
#
# auth_update_profile(update)


# user = {
#     "username": "Funtechs",
#     "email": "funtechs45@gmail.com",
#     "password": "admin",
#     "company": "Create With Funtechs",
# }
# print(auth_register(user))
