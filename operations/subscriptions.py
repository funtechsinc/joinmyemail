from models.sql_model import SubscriptionTable
from connection import db_session
from functions.defaults import  is_email_valid
from functions.Generate_Hash import hash_function
from decoders.subscriptions import decode_subs


# user subscribe
def new_subscription(doc: {}) -> {}:
    try:
        uuid = doc['uuid']
        email = doc["email"]
        display_name = doc["display_name"]
        subscription_hash = hash_function(email)

        req = SubscriptionTable(uuid, display_name, email, subscription_hash)

        if is_email_valid(email):
            res = db_session.query(SubscriptionTable).filter(SubscriptionTable.email == email).one_or_none()

            if res is None:
                db_session.add(req)
                db_session.commit()
                return {
                    'status': 'ok',
                    'message': f'👏 Thanks for subscribing {display_name}'
                }
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
def all_subscribers(uuid: str) -> list or dict:
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





# print(
#     new_subscription({'uuid': 1, 'email': 'abdulwahabiddris08@gmail.com', 'display_name': 'Iddris Abdul Wahab'})
# )


# print(all_subscribers(1))
