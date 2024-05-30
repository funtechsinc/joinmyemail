from functions.TimeStamp import generate_analytics
from operations.smtp_server import get_smtp
from operations.templates import one_template


def decode_campaign(doc: {}) -> dict:
    return {
        'campaign_id': doc.campaign_id,
        'subject': doc.subject,
        'body': doc.body,
        'server': get_smtp(doc.smtp_id)['doc']['server_name'],
        'server_id': doc.smtp_id,
        'number_of_subscribers_reach': doc.number_of_subscribers_reach,
        'success': doc.success,
        'errors': doc.errors,
        'deployed': doc.deployed,
        'template_name': one_template(doc.template_id)['doc']['template_name'] if doc.template_id is not None else 'scratch',
        'publish': 'published' if doc.deployed else 'Not Published',
        'analytics': generate_analytics(doc.timestamp, False)
    }


def decode_campaigns(docs: list) -> list:
    return [
        decode_campaign(doc) for doc in docs
    ]
