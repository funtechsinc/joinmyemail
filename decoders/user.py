def decode_user(doc) -> dict:
    return {
        'uuid': doc.uuid,
        'username': doc.username,
        'welcome_message': doc.welcome_message,
        'smtp_for_welcome_message': doc.smtp_for_welcome_message,
        'welcome_message_subject': doc.welcome_message_subject,
        'call_to_action': doc.call_to_action,
        'email': doc.email,
        'handle': doc.handle,
        'company': doc.company,
        'photo_url': doc.photo_url,
        'title': doc.title,
        'sub_title': doc.sub_title,
        'category': doc.category,
        'youtube': doc.youtube,
        'instagram': doc.instagram,
        'x': doc.x,
    }
