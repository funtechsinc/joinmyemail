from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_model import SQLBASE
from dotenv import load_dotenv
import os

load_dotenv('.env')
user: str = os.getenv('USER')
password: str = os.getenv('PASSWORD')
db_host: str = os.getenv('DB_HOST')
db_port: str = os.getenv('DB_PORT')

# uri = 'postgresql://postgres:admin@localhost:5432/SubscribeToMyEmailList'
# postgres_uri = (F'postgresql://{user}:{password}@{db_host}:{db_port}/defaultdb?sslmode=require')
uri = 'sqlite:///SubscribeToMyEmail.db'
engine = create_engine(uri, pool_size=10, max_overflow=20)

# bind to create all tables
SQLBASE.metadata.create_all(bind=engine)

# create session
session = sessionmaker(bind=engine, autoflush=True)
db_session = session()
