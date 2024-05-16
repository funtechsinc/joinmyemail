from connection import db_session
from models.sql_model import SmtpTable
from decoders.smtp import decode_smtps, decode_smtp


# create a smtp service
def create_smtp_server(doc: dict, uuid) -> dict:
    server = doc['server']
    name = doc['name']
    smtp_email = doc['smtp_email']
    smtp_password = doc['smtp_password']

    req = SmtpTable(
        uuid,
        server,
        name,
        smtp_email,
        smtp_password
    )

    try:
        # check if smtp service already added by user
        res = db_session.query(SmtpTable).filter(SmtpTable.smtp_email == smtp_email).one_or_none()
        if res is None:
            db_session.add(req)
            db_session.commit()

            return{
                'status': 'ok',
                'message': 'new smtp service added'
            }
        else:
            return{
                'status': 'error',
                'message': 'stmp server with email already exist'
            }

    except Exception as e:
        db_session.rollback()
        return {
            'status': 'error',
            'message': str(e)
        }


# getting all services for a user
def get_all_smtp(uuid: int) -> dict:
    try:
        res = db_session.query(SmtpTable).filter(SmtpTable.uuid == uuid).all()
        if len(res) > 0:
            res = decode_smtps(res)
            return {
                'status': 'ok',
                'message': f'smtp services gotten for {uuid}',
                'docs': res,
                'len': len(res)
            }
        else:
            return{
                'status': 'ok',
                'message': 'no records',
                'docs': [],
                'len': 0
            }

    except Exception as e:
        db_session.rollback()
        return {
            'status': 'error',
            'message': str(e)
        }


# update smtp
def update_smtp(doc: dict, smtp_id: int) -> dict:
    try:
        res = db_session.query(SmtpTable).filter(SmtpTable.smtp_id == smtp_id).one_or_none()

        if res is None:
            return {
                'status': 'error',
                'message': f'{smtp_id}: record with id not found'
            }
        else:
            if 'name' in doc:
                res.name = doc['name']
            if 'server' in doc:
                res.server = doc['server']
            if 'smtp_email' in doc:
                res.smtp_email = doc['smtp_email']
            if 'smtp_password' in doc:
                res.smtp_password = doc['smtp_password']

            db_session.commit()
            return {
                'status': 'ok',
                'message': 'smtp service updated',
            }
    except Exception as e:
        db_session.rollback()
        return {
            'status': 'error',
            'message': str(e)
        }


# delete server
def delete_smtp(smtp_id:int) -> dict:
    try:
        res = db_session.query(SmtpTable).filter(SmtpTable.smtp_id == smtp_id).one_or_none()
        if res is not None:
            db_session.delete(res)
            db_session.commit()
            return {
                'status': 'ok',
                'message': f'{res.name} deleted!'
            }
        else:
            return{
                'status': 'error',
                'message': 'smtp service not found'
            }
    except Exception as e:
        db_session.rollback()
        return {
            'status': 'error',
            'message': str(e)
        }


# get server
def get_smtp(smtp_id: int) -> dict:
    try:
        res = db_session.query(SmtpTable).filter(SmtpTable.smtp_id == smtp_id).one_or_none()
        if res is not None:
            return {
                'status': 'ok',
                'message': f'smtp gotten',
                'doc': decode_smtp(res)
            }
        else:
            return{
                'status': 'error',
                'message': 'smtp service not found'
            }
    except Exception as e:
        db_session.rollback()
        return {
            'status': 'error',
            'message': str(e)
        }


# print(get_all_smtp(8))


# print(update_smtp({'smtp_id': 1, 'name': 'This is the new name'}))

# print(get_smtp(1))

# new_smtp = {
#     'uuid': '107239095561327300729',
#     'server': 'smtp.gmail.com',
#     'name': 'Youtube Gmail Messages',
#     'smtp_email': 'mail.funtechs@gmail.com',
#     'smtp_password': 'socmlttuexphktdt'
# }
#
# print(create_smtp_server(new_smtp))
