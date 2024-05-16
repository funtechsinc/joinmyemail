import smtplib
from email.mime.text import MIMEText
import json


def send_emails(emails: list, server: str, sender: str, access_password: str, subject: str, body: str) -> dict:
    try:
        smtp_server = server
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        gmail_user = sender
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

        html_body = body

        for to_email in receivers:
            msg = MIMEText(html_body.replace('{{email}}', to_email), "html")
            msg["From"] = from_email
            msg["To"] = to_email
            msg["Subject"] = subject
            server.sendmail(from_email, to_email, msg.as_string())

        # Close the connection
        server.quit()

        return {
            "status": 'ok',
            'message': f'👏 Email sent successfully to all recipients',
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
