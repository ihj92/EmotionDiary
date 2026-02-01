from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
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

# 일기 작성 API
@app.post("/api/diary")
def create_diary(content: str, emotion: str, db: Session = Depends(get_db)):
    new_diary = Diary(content=content, emotion=emotion)
    db.add(new_diary)
    db.commit()
    db.refresh(new_diary)
    return {"status": "success", "data": {
        "id": new_diary.id,
        "content": new_diary.content,
        "emotion": new_diary.emotion,
        "created_at": str(new_diary.created_at)
    }}

# 일기 목록 가져오기 API
@app.get("/api/diary")
def get_diaries(db: Session = Depends(get_db)):
    diaries = db.query(Diary).all()
    return {"status": "success", "data": diaries}