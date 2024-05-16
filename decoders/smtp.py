from functions.TimeStamp import generate_analytics


def decode_smtp(doc: {}) -> dict:
    return {
        'server_id': doc.smtp_id,
        'server_name': doc.name,
        'server_email': doc.smtp_email,
        'smtp_server': doc.server,
        'smtp_password': doc.smtp_password,
        'analytics': generate_analytics(doc.timestamp, False)
    }


def decode_smtps(docs: list) -> list:
    return [decode_smtp(doc) for doc in docs]
