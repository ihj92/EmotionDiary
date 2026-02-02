from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func, text
from datetime import datetime, date
from .database import engine, get_db, Base
from .models import Diary

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"message": "감정일기 서버가 작동중입니다!"}

# 일기 작성
@app.post("/api/diary")
def create_diary(content: str, emotion: str, db: Session = Depends(get_db)):
  new_diary = Diary(content=content, emotion=emotion)
  db.add(new_diary)
  db.commit()
  db.refresh(new_diary)
  return {
    "status": "success",
    "data": {
      "id": new_diary.id,
      "content": new_diary.content,
      "emotion": new_diary.emotion,
      "created_at": str(new_diary.created_at)
    }
  }

# 전체 일기 조회 (ORM 방식)
# @app.get("/api/diary")
# def get_diaries(db: Session = Depends(get_db)):
#     diaries = db.query(Diary).order_by(Diary.created_at.desc()).all()
#     return {"status": "success", "data": diaries}

# 전체 일기 조회 (Raw SQL 방식)
@app.get("/api/diary")
def get_diaries(db: Session = Depends(get_db)):
  sql = text("""
    SELECT 
      id,
      content,
      emotion,
      created_at
    FROM diaries
    ORDER BY created_at DESC
  """)
  
  result = db.execute(sql)
  rows = result.fetchall()
  data = [dict(row._mapping) for row in rows]
  
  return {"status": "success", "data": data}

# 특정 날짜 일기 조회
@app.get("/api/diary/date/{date}")
def get_diary_by_date(date: str, db: Session = Depends(get_db)):
  try:
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    
    diaries = db.query(Diary).filter(
      func.date(Diary.created_at) == target_date
    ).all()
    
    return {
      "status": "success",
      "date": date,
      "count": len(diaries),
      "data": diaries
    }
  except ValueError:
    return {
      "status": "error",
      "message": "날짜 형식이 잘못되었습니다. YYYY-MM-DD 형식으로 입력해주세요."
    }

# 기간별 일기 조회
@app.get("/api/diary/range")
def get_diary_by_range(
  start_date: str,
  end_date: str,
  db: Session = Depends(get_db)
):
  try:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    end = end.replace(hour=23, minute=59, second=59)
    
    diaries = db.query(Diary).filter(
      Diary.created_at >= start,
      Diary.created_at <= end
    ).order_by(Diary.created_at.desc()).all()
    
    return {
      "status": "success",
      "start_date": start_date,
      "end_date": end_date,
      "count": len(diaries),
      "data": diaries
    }
  except ValueError:
    return {
      "status": "error",
      "message": "날짜 형식이 잘못되었습니다."
    }