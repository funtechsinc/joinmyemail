from functions.TimeStamp import generate_analytics


def decode_sub(doc: {}) -> dict:
    return {
        'subscription_id': doc.subscription_id,
        'display_name': doc.display_name,
        'email': doc.email,
        'analytics': generate_analytics(doc.timestamp)
    }


def decode_subs(docs: []) -> []:
    return [decode_sub(doc) for doc in docs]

