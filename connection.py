from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_model import SQLBASE

# uri = 'postgresql://postgres:admin@localhost:5432/SubscribeToMyEmailList'
postgres_uri = ('postgresql://avnadmin:AVNS_WPiF4GWj6QcBT2kabID@subscribe-to-my-email-list-funtechs-inc.h.aivencloud'
                '.com:12550/defaultdb?sslmode=require')
# uri = 'sqlite:///SubscribeToMyEmail.db'
engine = create_engine(postgres_uri, pool_size=10, max_overflow=20)

# bind to create all tables
SQLBASE.metadata.create_all(bind=engine)

# create session
session = sessionmaker(bind=engine, autoflush=True)
db_session = session()
