from models.sql_model import SubscriptionTable
from connection import db_session
from functions.defaults import  is_email_valid
from functions.Generate_Hash import hash_function
from decoders.subscriptions import decode_subs, decode_only_emails
from models.sql_model import UserTable
from operations.smtp_server import get_smtp
from functions.send_email import send_emails


# user subscribe
def new_subscription(doc: {}) -> {}:
    try:
        uuid = doc['uuid']
        email = doc["email"]
        country = doc['country']
        display_name = doc["display_name"]
        subscription_hash = hash_function(email)

        # get the smtp
        smtp = get_smtp(1)
        smtp = smtp['doc']
        smtp_server = smtp['smtp_server']
        smtp_email = smtp['server_email']
        smtp_password = smtp['smtp_password']

        req_user = db_session.query(UserTable).filter(UserTable.uuid == uuid).one_or_none()
        welcome_message = req_user.welcome_message
        welcome_message = welcome_message if welcome_message is not None else f"""" 
       <p> Dear {display_name}, </p>
      <div>I hope this message finds you well!</div>
      I wanted to take a moment to extend a warm and heartfelt congratulations on subscribing to our email list. 
      🎉 Your decision to join us means a lot, and we're thrilled to welcome you into our exclusive community.
       """
        subject = f' 🎉 Congratulations on Joining the {req_user.company} Community!'


        req = SubscriptionTable(uuid, display_name, email, country, subscription_hash)

        if is_email_valid(email):
            res = db_session.query(SubscriptionTable).filter(SubscriptionTable.email == email).one_or_none()

            if res is None:
                db_session.add(req)
                db_session.commit()
                # send a notification email to user
                send_emails([email], smtp_server, smtp_email, smtp_password, subject, welcome_message)
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


# get all subscribers emails
def all_subscribers_emails(uuid: str) -> list or dict:
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
