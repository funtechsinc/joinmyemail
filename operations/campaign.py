from connection import db_session
from models.sql_model import CampaignTable
from operations.subscriptions import all_subscribers_emails
from functions.send_email import send_emails
from operations.smtp_server import get_smtp
from decoders.campaigns import decode_campaigns


def launch_campaign(subscribers, smtp_server, smtp_email, uuid, smtp_password, subject, body, campaign_id=None):
    res = send_emails(subscribers, smtp_server, smtp_email, uuid, smtp_password, subject, body, campaign_id)
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

        req = CampaignTable(
            uuid,
            subject,
            body,
            server,
            number_of_subscribers_reach,
            0,
            0,
            is_deployed
        )
        db_session.add(req)
        db_session.commit()
        campaign_id = req.campaign_id

        res = launch_campaign(subscribers, smtp_server, smtp_email, uuid, smtp_password, subject,
                              body,
                              campaign_id=campaign_id) if is_deployed and number_of_subscribers_reach > 0 else not_deployed_state
        res_campaign = db_session.query(CampaignTable).filter(CampaignTable.campaign_id == campaign_id).one_or_none()
        res_campaign.success = res['success']
        res_campaign.errors = res['errors']
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


# delete campaign
def delete_campaign(campaign_id: int):
    res = db_session.query(CampaignTable).filter(CampaignTable.campaign_id == campaign_id).one_or_none()
    try:
        if res is None:
            return {
                'status': 'error',
                'message': f'campaign with ID {campaign_id} do not exist',
            }
        else:
            db_session.delete(res)
            db_session.commit()
            return {
                'status': 'ok',
                'message': 'Campaign Deleted!'
            }
    except Exception as e:
        db_session.rollback()
        return {
            'status': 'error',
            'message': str(e)
        }


def edit_campaign(doc: dict, campaign_id: int) -> dict:
    try:
        criteria: dict = {'campaign_id': campaign_id}
        is_deployed = doc['deployed']
        doc = doc
        res = db_session.query(CampaignTable).filter_by(criteria).one_or_none()

        if is_deployed:
            subject = doc['subject']
            body = doc['body']
            server = doc['smtp_id']
            uuid = res.uuid

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
            campaign_res = launch_campaign(subscribers, smtp_server, smtp_email, uuid, smtp_password, subject,
                                           body, campaign_id=campaign_id)
            if res is not None:
                if 'subject' in doc:
                    res.subject = doc['subject']
                if 'body' in doc:
                    res.body = doc['body']
                if 'smtp_id' in doc:
                    res.server_id = doc['smtp_id']
                res.number_of_subscribers_reach = number_of_subscribers_reach
                res.success = campaign_res['success']
                res.errors = campaign_res['errors']
                res.deployed = True
                db_session.commit()
            return campaign_res
        else:
            if 'subject' in doc:
                res.subject = doc['subject']
            if 'body' in doc:
                res.body = doc['body']
            if 'smtp_id' in doc:
                res.server_id = doc['smtp_id']
            db_session.commit()
            return {
                'status': 'ok',
                'message': 'Campaign saved'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

#
# print(create_campaign({
#     'uuid': 1,
#     'server_id': 1,
#     'subject': 'Devin is changing everything',
#     'body': '<h1>Hi Devin Here </h1> This is a simple demo email sent.'
# })
# )

# print(user_campaigns(1))
