import smtplib
from email.mime.text import MIMEText
import json
from functions.template_layout import template_layout
from operations.auth import auth_get_user


def send_emails(emails: list, server: str, email: str, sender_uuid: int, access_password: str, subject: str,
                body: str) -> dict:
    try:
        # get the sender first
        user_sender = auth_get_user(sender_uuid)
        user_sender = user_sender['user']

        smtp_server = server
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        gmail_user = email
        gmail_password = access_password
        receivers = emails
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            # If JSON parsing fails, keep the original body value
            body = body
        # Compose the email message
        subject = subject
        server.login(gmail_user, gmail_password)
        from_email = gmail_user

        html_body = template_layout(body, user_sender['photo_url'], user_sender['company'], user_sender['category'],
                                    )

        i = 0
        errors = 0

        while i < len(receivers):
            try:
                to_email = receivers[i]['email']
                to_username = receivers[i]['username']

                msg = MIMEText(html_body.replace('{{email}}', to_email).replace('{{username}}', to_username), "html")
                msg["From"] = from_email
                msg["To"] = to_email
                msg["Subject"] = subject
                server.sendmail(from_email, to_email, msg.as_string())
                i += 1
            except Exception as e:
                errors += 1
                i += 1
        else:
            # Close the connection
            server.quit()
            success = len(receivers) - errors
            return {
                "status": 'ok',
                'message': f'👏 Email sent successfully to recipients',
                'success': success,
                'errors': errors
            }

        #
        # for to_email in receivers:
        #     success = 0
        #
        #     try:
        #         msg = MIMEText(html_body.replace('{{email}}', to_email), "html")
        #         msg["From"] = from_email
        #         msg["To"] = to_email
        #         msg["Subject"] = subject
        #         server.sendmail(from_email, to_email, msg.as_string())
        #
        #


    except smtplib.SMTPException as e:
        return {
            "status": 'error',
            'message': f'Failed to send email: {str(e)}'
        }

    except Exception as e:
        return {
            "status": 'error',
            'message': f'An unexpected error occurred: {str(e)}'
        }
