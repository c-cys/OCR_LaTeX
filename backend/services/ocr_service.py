'''
backend/services/ocr_services.py
pytesseract를 이용한 OCR 기능
'''
import pytesseract
from PIL import Image # Python Imaging Library(Pillow) 이미지 처리를 위한 라이브러리

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image: Image.Image) -> str:
    """
    이미지 입력받아 pytesseract로 텍스트 추출
    """
    try:
        # img = Image.open(image)
        text = pytesseract.image_to_string(image, lang="eng+kor")
        return text.strip()
    except Exception as e:
        return f"Error in OCR: {str(e)}"