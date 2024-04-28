from sqlalchemy import Column, String, Integer, ForeignKey
from functions.TimeStamp import Get_Time_Stamp
from sqlalchemy.orm import declarative_base

SQLBASE = declarative_base()


# create user
class UserTable(SQLBASE):
    __tablename__: str = 'users'
    uuid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    handle = Column(String)
    company = Column(String)
    timestamp = Column(String, default=Get_Time_Stamp())

    def __init__(self, username, email, password, company):
        self.username = username
        self.email = email
        self.password = password
        self.company = company
