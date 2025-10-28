'''
backend/main.py
FastAPI 서버 : OCR과 요약 기능 처리
'''

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.ocr_service import extract_text
from services.summary_service import summarize_text
from io import BytesIO
from PIL import Image

app = FastAPI()

# Streamlit과 연결을 위해 CORS 허용
# CORS 허용은 서버에서 특정 출처(origin)의 요청을 받아들이도록 설정하는 것인데
# 개발 단계라 전체를 허용하도록 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"])

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    """이미지 파일을 받아 OCR 처리"""
    image = Image.open(BytesIO(await file.read()))
    text = extract_text(image)
    return {"text": text}

@app.post("/summary")
async def summary_endpoint(data: dict):
    text = data.get("text", "")
    summary = summarize_text(text)
    return {"summary": summary}
