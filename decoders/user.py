def decode_user(doc) -> dict:
    return {
        'uuid': doc.uuid,
        'username': doc.username,
        'email': doc.email,
        'handle': doc.handle,
        'company': doc.company,
        'photo_url': doc.photo_url,
        'verified_email': doc.verified_email,
        'gmail_access_token': doc.gmail_access_token,
        'title': doc.title,
        'sub_title': doc.sub_title,
        'category': doc.category,
        'youtube': doc.youtube,
        'instagram': doc.instagram,
        'x': doc.x,
    }