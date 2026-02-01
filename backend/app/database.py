from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# .env 파일 읽기
load_dotenv()

# 데이터베이스 주소
DATABASE_URL = os.getenv("DATABASE_URL")

# 데이터베이스 연결
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델의 기본 클래스
Base = declarative_base()

# 데이터베이스 사용할 때마다 이 함수 호출
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()