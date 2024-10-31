from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = 'localhost'
DB_NAME = 'fast_api_db'
DB_USER = 'postgres'
DB_PASSWORD ='``cin100)Out'
DB_PORT = '5432'

def get_db():
    #db 연결
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    session_local = sessionmaker(bind=engine)
    db = session_local()
    
    #객체를 session으로 전달
    try:
        yield db
    finally:
        db.close()