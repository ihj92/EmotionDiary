from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Emotion Diary API is running"}
