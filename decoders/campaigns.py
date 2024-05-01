from functions.TimeStamp import generate_analytics
from operations.smtp_server import get_smtp


def decode_campaign(doc: {}) -> dict:
    return {
        'subject': doc.subject,
        'server': get_smtp(doc.smtp_id)['doc']['server_name'],
        'number_of_subscribers_reach': doc.number_of_subscribers_reach,
        'success': doc.success,
        'errors': doc.errors,
        'analytics': generate_analytics(doc.timestamp, False)
    }


def decode_campaigns(docs: list) -> list:
    return [
        decode_campaign(doc) for doc in docs
    ]
