from connection import db_session
from models.sql_model import SmtpTable
from decoders.smtp import  decode_smtps

# create a smtp service
def create_smtp_server(doc: dict) -> dict:
    uuid = doc['uuid']
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
                'len':0
            }

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


# update smtp
def update_smtp(doc: dict) -> dict:
    try:
        smtp_id = doc['smtp_id']
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
        return {
            'status': 'error',
            'message': str(e)
        }



# print(update_smtp({'smtp_id': 1, 'name': 'This is the new name'}))

# print(get_all_smtp(1))

# new_smtp= {
#     'uuid': 1,
#     'server': 'smtp.example.com',
#     'name': 'John Doe',
#     'smtp_email': 'johndoee@example.com',
#     'smtp_password': 'secretpassword'
# }
#
# print(create_smtp_server(new_smtp))
