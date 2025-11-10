[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/RWKU9dGg)
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
│   └── to_LaTex.py                 # LaTeX 수식 변환기<br>
│   └── pages                       # 하위 페이지<br>
│         └── editor.py             # LaTeX 수식 편집기<br>
│         └── paste.py              # 이미지 업로드 시, Ctrl+V로 붙여넣기<br>
│         └── upload.py             # 이미지 업로드 시, 기기 내장 이미지 업로드<br>
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

## 🚀 초기 실행 시 다운로드해야 하는 것
```
tesseract.exe 다운로드 후
backend/services/ocr_service.py의 8번째 line 변경
```
