from connection import db_session
from functions.Generate_Hash import hash_function
from models.sql_model import UserTable
from functions.Generate_Hash import verify_hash
from decoders.user import decode_user


# create a user
def Auth_Create_User(doc: dict) -> dict:
    doc = doc
    email = doc["email"]

    # check is user already exist
    result = db_session.query(UserTable).filter(UserTable.email == email).one_or_none()

    if str(result) == "None":
        # hash password
        hash_password = hash_function(doc["password"])
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

        return {
            'status': 'success',
            'message': 'User created successfully'
        }
    else:
        return {
            'status': 'error',
            'message': f'user already exist with email: {email}'
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


# user = {
#     "username": "demo_user",
#     "email": "demo@example.com",
#     "password": "demo_password",
#     "company": "demo_company",
#     "handle": "funtechs"
# }
# print(Auth_Create_User(user))
