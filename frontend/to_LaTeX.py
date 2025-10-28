
from pix2tex.cli import LatexOCR
from PIL import Image
import io

model = LatexOCR()

def to_LaTeX(uploaded_file) -> str:
    try:
        # Streamlit의 UploadedFile은 BytesIO 형태이므로 Image로 변환
        image = Image.open(io.BytesIO(uploaded_file.getvalue()))

        # 결과를 $$로 감싸서 수식 블록 형태로 반환
        return f"$$ {model(image)} $$"

    except Exception as e:
        return f"Error in OCR: {str(e)}"


# def to_LaTeX(text: str) -> str:
#     # ^, *, / 등을 간단히 변환
#     text = re.sub(r"([A-Za-z0-9])\^([A-Za-z0-9])", r"\1^{\2}", text)
#     text = text.replace("*", r"\times ")
#     text = text.replace("/", r"\frac{a}{b}")  # 단순 예시
#
#     # 결과를 LaTeX 문법으로 감싸기
#     return f"$$ {text} $$"