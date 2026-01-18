# 📝 Emotion Diary (감정일기 프로젝트)

## 📌 프로젝트 소개

**Emotion Diary**는 사용자가 하루에 한 번 자신의 감정을 기록하고, 누적된 일기를 기반으로 **감정의 흐름을 시각화**하는 개인 감정 관리 서비스입니다.

본 프로젝트는 **백엔드 구조와 데이터 흐름에 대한 이해**를 목표로 하며, **FastAPI + PostgreSQL** 기반의 REST API 서버로 설계되었습니다.

---

## 🎯 프로젝트 목표

- 서버(API)의 역할과 동작 방식 이해
- 데이터베이스 설계 및 **SQL 직접 작성 경험**
- 프론트엔드와 백엔드의 **역할 분리 구조 학습**
- AI API 연동을 통한 기능 확장 경험

---

## 🛠 기술 스택

### Backend

- **Python**
- **FastAPI**
- **PostgreSQL**
- **psycopg2** (Python ↔ PostgreSQL을 연결해주는 라이브러리)
- **Uvicorn** (FastAPI 서버를 실제로 실행시켜주는 웹 서버)

### Frontend

- **Vue 3**
- **Vite**
- **Ionic**
- **Axios**

---

## 📂 프로젝트 구성 (예정)

```text
emotion-diary/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routers/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── database.py
│   └── requirements.txt
└── frontend/
