from functions.TimeStamp import generate_analytics


def decode_open(doc) -> dict:
    return {
        'email': doc.email,
        'analytics': generate_analytics(doc.timestamp, False)
    }


def decode_opens(docs) -> list:
    return [
        decode_open(doc) for doc in docs
    ]
