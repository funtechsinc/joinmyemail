# organization settings
from functions.template_layout import  template_layout

# emails send by subscribe to my email list org
smtp_email = ''
smtp_password = ''
smtp_server = ''


# Template to alert users of new subscribers
def new_subscriber_template(content: str):
    return template_layout()


