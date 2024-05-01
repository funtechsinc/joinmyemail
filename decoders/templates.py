from functions.TimeStamp import generate_analytics


def decode_template(doc: {}) -> dict:
    return {
        'template_id': doc.template_id,
        'template_name': doc.template_name,
        'body': doc.body,
        'analytics': generate_analytics(doc.timestamp, False)
    }


def decode_templates(docs: list) -> list:
    return [
        decode_template(doc) for doc in docs
    ]
