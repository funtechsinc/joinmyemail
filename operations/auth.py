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
            handle = doc["handle"]

            # req
            req = UserTable(
                username,
                email,
                hash_password,
                company,
                handle
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


# print(auth_login("demo@example.com", "demo_password"))

# update = {
#     'uuid': 1,
#     'category': 'Marketing',
# }
#
# auth_update_profile(update)


user = {
    "username": "demo_users",
    "email": "demo@gmail.com",
    "password": "demo_password",
    "company": "demo_company",
    "handle": "funtechss"
}
print(auth_register(user))
