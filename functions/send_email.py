from fastapi import APIRouter
import smtplib
from email.mime.text import MIMEText
import json


def send_emails(emails: list, user: str, password, smtp_server: str, subject: str, body) -> dict:
    try:
        smtp_server = smtp_server
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        gmail_password = password
        receivers = emails

        # Compose the email message
        server.login(user, gmail_password)

        def send_mail(sent_to_email: str):
            msg = MIMEText(body, "html")
            msg["From"] = user
            msg["To"] = sent_to_email
            msg["Subject"] = subject
            server.sendmail(user, sent_to_email, msg.as_string())
            return True

        success = 0
        errors = 0

        for to_email in receivers:
            try:
                res = send_mail(to_email)
                if res:
                    success += 1
            except Exception as e:
                errors += 1
                continue

        # Close the connection
        server.quit()
        return {
                    "status": 'ok',
                    'message':  f'👏 Email sent successfully to {success} mails',
                    'success': success,
                    'errors': errors
            }

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
