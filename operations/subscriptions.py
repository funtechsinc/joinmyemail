from models.sql_model import SubscriptionTable
from connection import db_session
from functions.defaults import is_email_valid
from functions.Generate_Hash import hash_function
from decoders.subscriptions import decode_subs, decode_only_emails
from models.sql_model import UserTable
from operations.smtp_server import get_smtp
from functions.send_email import send_emails


# user subscribe
def new_subscription(doc: dict, handle: str) -> {}:
    try:
        email = doc["email"]
        country = doc['country']
        display_name = doc["display_name"]
        subscription_hash = hash_function(email)

        req_user = db_session.query(UserTable).filter(UserTable.handle == handle).one_or_none()

        if req_user is not None:
            welcome_message = req_user.welcome_message
            welcome_message_subject = req_user.welcome_message_subject

            # get the smtp
            smtp = get_smtp(req_user.smtp_for_welcome_message) if welcome_message is not None else None
            smtp = smtp['doc'] if welcome_message is not None else None
            smtp_server = smtp['smtp_server'] if welcome_message is not None else None
            smtp_email = smtp['server_email'] if welcome_message is not None else None
            smtp_password = smtp['smtp_password'] if welcome_message is not None else None

            req = SubscriptionTable(req_user.uuid, display_name, email, country, subscription_hash)

            if is_email_valid(email):
                res = db_session.query(SubscriptionTable).filter(SubscriptionTable.email == email).one_or_none()
                if res is None:
                    db_session.add(req)
                    db_session.commit()
                    if welcome_message is not None:
                        # send a notification email to user
                        receiver: list = [{'username': display_name, 'email': email}]
                        res_email = send_emails(receiver, smtp_server, smtp_email, req_user.uuid, smtp_password,
                                                welcome_message_subject, welcome_message)
                        resp = {
                            'status': 'ok',
                            'message': f'👏 Thanks: Check your email for a free package {display_name}'
                        } if res_email['status'] is 'ok' else {
                            'status': 'ok',
                            'message': f'👏 Thanks for subscribing {display_name}'
                        }
                    else:
                        resp = {
                            'status': 'ok',
                            'message': f'👏 Thanks for subscribing {display_name}'
                        }
                    return resp
                else:
                    return {
                        'status': 'ok',
                        'message': f'{email}: already subscribed'
                    }
            else:
                return {
                    'status': 'error',
                    'message': 'Invalid Email!'
                }
        else:
            return {
                'status': 'error',
                'message': 'handle do not exist'
            }

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


# unsubscribe user
def unsubscribe(hash_token: str) -> {}:
    res = db_session.query(SubscriptionTable).filter(SubscriptionTable.subscription_hash == hash_token).one_or_none()
    if res is None:
        return {
            'status': 'error',
            'message': 'unAuthorised!'
        }
    else:
        db_session.delete(res)
        db_session.commit()
        return {
            'status': 'ok',
            'message': f'😔 subscription removed for {res.display_name}'
        }


# get all subscribers
def all_subscribers(uuid: int) -> list or dict:
    res = db_session.query(SubscriptionTable).filter(SubscriptionTable.uuid == uuid).all()
    if len(res) > 0:
        docs = decode_subs(res)
        return {
            'status': 'ok',
            'message': f'subscriptions gotten for {uuid}',
            'docs': docs,
            'len': len(docs)
        }
    else:
        return {
            'status': 'ok',
            'message': 'no records',
            'docs': [],
            'len': 0
        }


# get all subscribers emails
def all_subscribers_emails(uuid: int) -> list or dict:
    res = db_session.query(SubscriptionTable).filter(SubscriptionTable.uuid == uuid).all()
    if len(res) > 0:
        docs = decode_only_emails(res)
        return {
            'status': 'ok',
            'message': f'subscriptions gotten for {uuid}',
            'docs': docs,
            'len': len(docs)
        }
    else:
        return {
            'status': 'ok',
            'message': 'no records',
            'docs': [],
            'len': 0
        }

# print(
#     new_subscription(
#         {'uuid': "107239095561327300729", 'email': 'funtechs45@gmail.com', 'display_name': 'Abdul Wahab', 'country': 'USA'}
#      )
# )

# print(all_subscribers(1))
