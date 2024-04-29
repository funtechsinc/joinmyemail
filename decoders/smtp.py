def decode_smtp(doc: dict) -> dict:
    return {
        'server_name': doc.name,
        'server_email': doc.smtp_email,
        'smtp_server': doc.server
    }


def decode_smtps(docs: list) -> list:
    return [ decode_smtp(doc) for doc in docs ]