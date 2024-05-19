from connection import db_session
from models.sql_model import CampaignTable
from operations.subscriptions import all_subscribers_emails
from functions.send_email import send_emails
from operations.smtp_server import get_smtp
from decoders.campaigns import decode_campaigns


def launch_campaign(subscribers, smtp_server, smtp_email, uuid, smtp_password, subject, body):
    res = send_emails(subscribers, smtp_server, smtp_email, uuid, smtp_password, subject, body)
    return res


# new campaign
def create_campaign(doc: dict, uuid: int) -> dict:
    try:
        subject = doc['subject']
        body = doc['body']
        server = doc['smtp_id']
        is_deployed = doc['deployed']

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

        not_deployed_state = {
            'status': 'ok',
            'message': 'Saved Successfully.',
            'success': 0,
            'errors': 0
        }
        res = launch_campaign(subscribers, smtp_server, smtp_email, uuid, smtp_password, subject,
                              body) if is_deployed and number_of_subscribers_reach > 0 else not_deployed_state
        req = CampaignTable(
            uuid,
            subject,
            body,
            server,
            number_of_subscribers_reach,
            res['success'],
            res['errors'],
            is_deployed
        )

        db_session.add(req)
        db_session.commit()

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

# def edit_campaign(doc: dict, uuid: int) -> dict:
#     criteria: dict = {'uuid': uuid}
#     doc = doc
#     res = db_session.query(CampaignTable).filter_by(criteria).one_or_none()
#     if res is not None:
#         if 'subject' in doc:
#             res.subject = doc['subject']
#         if 'body' in doc:
#             res.body = doc['body']
#         if 'smtp_id' in doc:
#             res.server_id = doc['smtp_id']


#
# print(create_campaign({
#     'uuid': 1,
#     'server_id': 1,
#     'subject': 'Devin is changing everything',
#     'body': '<h1>Hi Devin Here </h1> This is a simple demo email sent.'
# })
# )

# print(user_campaigns(1))
