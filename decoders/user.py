def decode_user(doc) -> dict:
    return {
        'uuid': str(doc.uuid),
        'username': doc.username,
        'email': doc.email,
        'handle': doc.handle,
        'company': doc.company,
        'youtube': doc.youtube,
        'instagram': doc.instagram,
        'x': doc.x
    }