from sqlalchemy import Column, String, Integer, ForeignKey
from functions.TimeStamp import Get_Time_Stamp
from sqlalchemy.orm import declarative_base

SQLBASE = declarative_base()


#  users
class UserTable(SQLBASE):
    __tablename__: str = 'users'
    uuid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    handle = Column(String, unique=True)
    company = Column(String)
    title = Column(String)
    sub_title = Column(String)
    category = Column(String)
    timestamp = Column(String, default=Get_Time_Stamp())

    def __init__(self, username, email, password, company, handle):
        self.username = username
        self.email = email
        self.password = password
        self.company = company
        self.handle = handle


#  smtp server
class SmtpTable(SQLBASE):
    __tablename__ = 'smtp'
    smtp_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    uuid = Column(Integer, ForeignKey('users.uuid'))
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
    subscription_id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(Integer, ForeignKey('users.uuid'))
    display_name = Column(String)
    email = Column(String, unique=True)
    subscription_hash = Column(String, unique=True)
    timestamp = Column(String, default=Get_Time_Stamp())

    def __init__(self,  uuid, display_name, email, subscription_hash):
        self.uuid = uuid
        self.display_name = display_name
        self.email = email
        self.subscription_hash = subscription_hash








