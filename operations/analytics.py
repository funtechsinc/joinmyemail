from connection import db_session
from models.sql_model import SubscriptionTable, CampaignTable
from decoders.analytics import decode_yearly
from sqlalchemy import extract


# get year subscriptions
def get_yearly_subs(year: int, uuid) -> dict:
    try:
        criteria = {'uuid': uuid, 'year': year}
        res = db_session.query(SubscriptionTable).filter_by(**criteria).all()
        docs = decode_yearly(res)
        return {
            'status': 'ok',
            'message': 'Yearly subscriptions gotten',
            'docs': docs
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


# get year campaigns
def get_yearly_campaigns(year: int, uuid) -> dict:
    try:
        criteria = {'uuid': uuid, 'year': year}
        res = db_session.query(CampaignTable).filter_by(**criteria).all()
        docs = decode_yearly(res)
        return {
            'status': 'ok',
            'message': 'Yearly subscriptions gotten',
            'docs': docs
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

# print(get_yearly_subs(2024, 1))
print(get_yearly_campaigns(2024, 1))