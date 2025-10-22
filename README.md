# WebApp_ocr
PDF/이미지 속 글을 읽고 요약하는 웹앱 개발
# OCR Starter Kit

FastAPI + pytesseract + Hugging Face + Streamlit 기반의 챗봇 프로젝트입니다.  
이 템플릿을 기반으로 자신만의 주제를 자유롭게 확장해보세요.

---
## 폴더 구조
project/<br>
│<br>
├── backend/<br>
│   ├── main.py                    # FastAPI 서버<br>
│   └── services/<br>
│ &nbsp;&nbsp;      ├── ocr_service.py         # pytesseract 이용한 OCR 기능<br>
│ &nbsp;&nbsp;      └── summary_service.py     # HuggingFace 모델 로딩<br>
│   <br>
│<br>
├── frontend/<br>
│   └── app.py                      # Streamlit 앱<br>
│<br>
├── requirements.txt<br>
└── README.md<br>

## 🚀 Starter Program 실행 방법

### 1️⃣ 가상환경 만들기 (선택)
```bash
python -m venv venv
source venv/bin/activate     # (Windows는 venv\Scripts\activate)
```

### 2️⃣ 패키지 설치
```bash
pip install -r requirements.txt
```

### 3️⃣ 백엔드(FastAPI) 실행
```bash
cd backend
uvicorn main:app --reload
```

### 4️⃣ 프론트엔드(Streamlit) 실행(다른 터미널을 새로 열어시 실행)
```bash
cd frontend
streamlit run app.py
```

### 5️⃣ 브라우저에서 확인
