from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from functions.TimeStamp import Get_Time_Stamp, generate_analytics
from sqlalchemy.orm import declarative_base

SQLBASE = declarative_base()


#  users
class UserTable(SQLBASE):
    __tablename__: str = 'users'
    uuid = Column(String, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    handle = Column(String, unique=True)
    company = Column(String)
    photo_url = Column(String)
    verified_email = Column(Boolean)
    gmail_access_token = Column(String)
    title = Column(String)
    sub_title = Column(String)
    category = Column(String)
    youtube = Column(String)
    instagram = Column(String)
    x = Column(String)
    welcome_message = Column(String)
    smtp_for_welcome_message = Column(Integer)
    timestamp = Column(String, default=Get_Time_Stamp())

    def __init__(self, uuid, username, email, verified_email, gmail_access_token, photo_url):
        self.uuid = uuid
        self.username = username
        self.email = email
        self.verified_email = verified_email
        self.gmail_access_token = gmail_access_token
        self.photo_url = photo_url


#  smtp server
class SmtpTable(SQLBASE):
    __tablename__ = 'smtp'
    smtp_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    uuid = Column(String, ForeignKey('users.uuid'))
    server = Column(String)
    name = Column(String)
    smtp_email = Column(String)
    smtp_password = Column(String)
    timestamp = Column(String, default=Get_Time_Stamp())

    def __init__(self, uuid, server, name, smtp_email, smtp_password):
        self.uuid = uuid
        self.server = server
        self.name = name
        self.smtp_email = smtp_email
        self.smtp_password = smtp_password


# subscriptions
class SubscriptionTable(SQLBASE):
    __tablename__ = 'subscriptions'
    analyst = generate_analytics(Get_Time_Stamp(), True)
    subscription_id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String, ForeignKey('users.uuid'))
    display_name = Column(String)
    email = Column(String, unique=True)
    country = Column(String)
    subscription_hash = Column(String, unique=True)
    timestamp = Column(String, default=analyst['timestamp'])
    year = Column(Integer, default=analyst['year'])
    day = Column(Integer, default=analyst['day'])
    month_number = Column(Integer, default=analyst['month_number'])

    def __init__(self, uuid, display_name, email, country, subscription_hash):
        self.uuid = uuid
        self.display_name = display_name
        self.email = email
        self.country = country
        self.subscription_hash = subscription_hash


# templates
class TemplatesTable(SQLBASE):
    __tablename__ = 'templates'
    template_id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String, ForeignKey('users.uuid'))
    template_name = Column(String)
    body = Column(String)
    timestamp = Column(String, default=Get_Time_Stamp())

    def __init__(self, uuid, template_name, body):
        self.uuid = uuid
        self.template_name = template_name
        self.body = body


# campaign
class CampaignTable(SQLBASE):
    __tablename__ = 'campaigns'

    analyst = generate_analytics(Get_Time_Stamp(), True)

    campaign_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    uuid = Column(String, ForeignKey('users.uuid'))
    smtp_id = Column(Integer, ForeignKey('smtp.smtp_id'))
    subject = Column(String)
    body = Column(String)
    number_of_subscribers_reach = Column(Integer)
    success = Column(Integer)
    errors = Column(Integer)
    timestamp = Column(String, default=analyst['timestamp'])
    year = Column(Integer, default=analyst['year'])
    day = Column(Integer, default=analyst['day'])
    month_number = Column(Integer, default=analyst['month_number'])

    def __init__(self, uuid, subject, body, smtp_id, number_of_subscribers_reach, success, errors):
        self.uuid = uuid
        self.subject = subject
        self.body = body
        self.smtp_id = smtp_id
        self.number_of_subscribers_reach = number_of_subscribers_reach
        self.success = success
        self.errors = errors

