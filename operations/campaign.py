from connection import db_session
from models.sql_model import CampaignTable
from operations.subscriptions import all_subscribers_emails
from functions.send_email import send_emails
from operations.smtp_server import get_smtp
from decoders.campaigns import decode_campaigns


# new campaign
def create_campaign(doc: dict) -> dict:
    try:
        uuid = doc['uuid']
        subject = doc['subject']
        body = doc['body']
        server = doc['server_id']

        # get the smtp
        smtp = get_smtp(server)
        smtp = smtp['doc']
        smtp_server = smtp['smtp_server']
        smtp_email = smtp['server_email']
        smtp_password = smtp['smtp_password']

        # get all email list for the user
        subscribers = all_subscribers_emails(uuid)
        subscribers = subscribers['docs']
        number_of_subscribers_reach = len(subscribers)

        res = send_emails(subscribers, smtp_server, smtp_email, smtp_password, subject, body)

        if res['status'] == 'ok':
            req = CampaignTable(
                uuid,
                subject,
                body,
                server,
                number_of_subscribers_reach,
                res['success'],
                res['errors'])
            db_session.add(req)
            db_session.commit()
            return res
        else:
            return res

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


# get users campaigns
def user_campaigns(uuid: int) -> dict:
    res = db_session.query(CampaignTable).filter(CampaignTable.uuid == uuid).all()
    if len(res) > 0:
        docs = decode_campaigns(res)
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


print(create_campaign({
    'uuid': 1,
    'server_id': 1,
    'subject': 'Devin is changing everything',
    'body': '<h1>Hi Devin Here </h1> This is a simple demo email sent.'
})
)

# print(user_campaigns(1))
