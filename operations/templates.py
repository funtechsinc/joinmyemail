from models.sql_model import TemplatesTable
from decoders.templates import decode_template, decode_templates
from connection import db_session


# new template
def create_template(doc: dict) -> dict:
    try:
        uuid = doc['uuid']
        template_name = doc['template_name']
        body = doc['body']

        req = TemplatesTable(uuid, template_name, body)
        db_session.add(req)
        db_session.commit()

        return {
            'status': 'ok',
            'message': '👏 Template added successfully'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


def edit_template(doc) -> dict:
    try:
        template_id = doc['template_id']

        res = db_session.query(TemplatesTable).filter(TemplatesTable.template_id == template_id).one_or_none()
        if res is not None:
            if 'template_name' in doc:
                res.template_name = doc['template_name']
            if 'body' in doc:
                res.body = doc['body']

            db_session.commit()
            return {
                'status': 'ok',
                'message': '✅ Template Updated'
            }
        else:
            return {
                'status': 'error',
                'message': f'{template_id}: Template not found'
            }

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


def delete_template(template_id) -> dict:
    try:
        template_id = template_id

        res = db_session.query(TemplatesTable).filter(TemplatesTable.template_id == template_id).one_or_none()
        if res is not None:
            db_session.delete(res)
            db_session.commit()
            return {
                'status': 'ok',
                'message': 'Template Deleted'
            }
        else:
            return {
                'status': 'error',
                'message': f'{template_id}: Template not found'
            }

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


def one_template(template_id) -> dict:

    try:
        res = db_session.query(TemplatesTable).filter(TemplatesTable.template_id == template_id).one_or_none()

        if res is not None:
            docs = decode_template(res)
            return {
                'status': 'ok',
                'message': f'templates gotten for {template_id}',
                'doc': docs
            }
        else:
            return {
                'status': 'ok',
                'message': 'no record!',
            }

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }


# all templates
def all_templates(uuid) -> dict:
    try:

        res = db_session.query(TemplatesTable).filter(TemplatesTable.uuid == uuid).all()

        if len(res) > 0:
            docs = decode_templates(res)
            return {
                'status': 'ok',
                'message': f'templates gotten for {uuid}',
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

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

# print(
#     create_template({'uuid': 1, 'template_name': 'Assignments', 'body': '<h1> Hello </h1>'})
# )

# print(edit_template({'template_id': 2,  'body': 'Welcome Template'}))

# print(delete_template(3))

# print(all_templates(1))
print(one_template(2))