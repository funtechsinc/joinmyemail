from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_model import SQLBASE

# uri = 'postgresql://postgres:admin@localhost:5432/SubscribeToMyEmailList'
uri = 'sqlite:///SubscribeToMyEmail.db'
engine = create_engine(uri, pool_size=1000, max_overflow=2000)

# bind to create all tables
SQLBASE.metadata.create_all(bind=engine)

# create session
session = sessionmaker(bind=engine, autoflush=True)
db_session = session()
