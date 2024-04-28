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


print(auth_login("demo@example.com", "demo_password"))

# ser = {
#     "username": "demo_user",
#     "email": "demo@example.com",
#     "password": "demo_password",
#     "company": "demo_company"
# }
# print(Auth_Create_User(user))
