from functions.TimeStamp import generate_analytics


def decode_sub(doc: {}) -> dict:
    return {
        'subscription_id': doc.subscription_id,
        'display_name': doc.display_name,
        'email': doc.email,
        'country': doc.country,
        'hash': doc.subscription_hash,
        'analytics': generate_analytics(doc.timestamp, False)
    }


def decode_subs(docs: []) -> []:
    return [decode_sub(doc) for doc in docs]


def decode_only_emails(docs: list) -> list:
    emails = []
    # i am appending the username so that you can use {{username}} to grab the username
    for doc in docs:
        emails.append({'email': doc.email, 'username': doc.display_name, 'hash_token': doc.subscription_hash})
    else:
        return emails


