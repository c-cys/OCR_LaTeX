'''
backend/services/summary_service.py
HuggingFace Transformers 이용한 요약 기능
'''
from transformers import pipeline

# 모델 로드
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    """
    텍스트 입력받아 요약 결과 반환
    """
    if len(text.strip()) == 0:
        return "요약할 텍스트가 없습니다."

    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']
