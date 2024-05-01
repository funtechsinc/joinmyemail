from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_model import SQLBASE

uri = 'postgresql://postgres:admin@localhost:5432/SubscribeToMyEmailList'
engine = create_engine(uri)

# bind to create all tables
SQLBASE.metadata.create_all(bind=engine)

# create session
session = sessionmaker(bind=engine, autoflush=True)
db_session = session()
