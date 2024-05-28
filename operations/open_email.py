from models.sql_model import OpenCampaigns
from connection import db_session
from decoders.opens import decode_opens

# opening an email
def email_open(email: str, campaign_id: int):
    try:
        criteria = {'email': email, 'campaign_id': campaign_id}
        res = db_session.query(OpenCampaigns).filter_by(**criteria).one_or_none()
        if res is None:
            req = OpenCampaigns(email, campaign_id)
            db_session.add(req)
            db_session.commit()
    except Exception as e:
        db_session.rollback()
        return {
            'status': 'error',
            'message': str(e)
        }


def get_campaign_opens(campaign_id: int):
    try:
        criteria = {'campaign_id': campaign_id}
        res = db_session.query(OpenCampaigns).filter_by(**criteria).all()
        if res is not None:
            return {
                'status': 'ok',
                'opens': len(res),
                'docs': decode_opens(res)
            }
        else:
            return {
                'status': 'ok',
                'opens': 0
            }
    except Exception as e:
        db_session.rollback()
        return {
            'status': 'error',
            'message': str(e)
        }
