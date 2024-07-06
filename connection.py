from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_model import SQLBASE
from dotenv import load_dotenv
from sqlalchemy import text
import os

load_dotenv('.env')
user: str = os.getenv('USER')
password: str = os.getenv('PASSWORD')
db_host: str = os.getenv('DB_HOST')
db_port: str = os.getenv('DB_PORT')
db_name: str = 'defaultdb'

# uri = 'postgresql://postgres:admin@localhost:5432/SubscribeToMyEmailList'
# uri = F'postgresql://{user}:{password}@{db_host}:{db_port}/{db_name}?sslmode=require'
uri = 'sqlite:///SubscribeToMyEmail.db'
# engine = create_engine(uri,
#     pool_size=5,              # Smaller pool size due to limited resources
#     max_overflow=10,          # Allow limited overflow connections
#     pool_timeout=15,          # Reduced wait time for a connection
#     pool_recycle=1800,        # Recycle connections every 30 minutes
#     connect_args={"sslmode": "require"} 
                       
# )
engine = create_engine(
    uri,
    connect_args={"check_same_thread": False}  # Allows multiple threads to use the same connection
)

# bind to create all tables
SQLBASE.metadata.create_all(bind=engine)

# create session
session = sessionmaker(bind=engine, autoflush=True)
db_session = session()
