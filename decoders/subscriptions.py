from functions.TimeStamp import generate_analytics


def decode_sub(doc: {}) -> dict:
    return {
        'subscription_id': doc.subscription_id,
        'display_name': doc.display_name,
        'email': doc.email,
        'country': doc.country,
        'analytics': generate_analytics(doc.timestamp, False)
    }


def decode_subs(docs: []) -> []:
    return [decode_sub(doc) for doc in docs]


def decode_only_emails(docs: list) -> list:
    emails = []
    for doc in docs:
        emails.append(doc.email)
    else:
        return emails


