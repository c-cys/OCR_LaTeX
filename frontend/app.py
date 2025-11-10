'''
frontend/app.py
Streamlit 웹 UI
'''
import streamlit as st
import requests
import to_LaTeX
from st_img_pastebutton import paste
import base64

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="OCR + LaTeX Converter", page_icon="🔢")

st.title("LaTeX Converter")
st.write("이미지를 업로드하면, 텍스트를 읽고 요약하거나 수식을 LaTeX로 변환할 수 있습니다!")

if "uploaded_file" in st.session_state:
    uploaded_file = st.session_state.get("uploaded_file") # binary_data 형태임

    # 일단 먼저 업로드한 이미지를 띄움
    st.image(uploaded_file, caption="이전 페이지에서 업로드한 이미지", use_container_width=True)

    # OCR 요청
    with st.spinner("텍스트를 추출 중입니다..."):

        # LaTeX 변환기
        st.subheader("🔢 LaTeX 문법에 맞게 변환된 수식")
        latex_result = to_LaTeX.to_LaTeX(uploaded_file)

        math = paste(label="📋 수식만 crop 하기", key="image_clipboard")
        if math is not None:
            header, encoded = math.split(",", 1)
            binary_data = base64.b64decode(encoded)
            st.image(binary_data, caption="Crop 한 수식:")
            latex_result = to_LaTeX.to_LaTeX(binary_data)

        st.session_state["latex_result"] = latex_result
        st.text_area("변환 결과", latex_result, height=200)

        if st.button("LaTeX 수식 편집하러 가기"):
            st.switch_page("pages/editor.py")

        # 인식된 테스트 띄우기
        files = {"file": uploaded_file}
        response = requests.post(f"{BACKEND_URL}/ocr", files={"file": uploaded_file})
        ocr_result = response.json().get("text", "")
        st.subheader("📜 인식된 텍스트")
        st.text_area("추출 결과", ocr_result, height=200)

    # 요약 기능
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("요약하기"):
        with st.spinner("요약 중입니다..."):
            res = requests.post(f"{BACKEND_URL}/summary", json={"text": ocr_result})
            summary = res.json().get("summary", "")
            st.subheader("🪄 요약 결과")
            st.write(summary)
else:
    if st.button("업로드 페이지로 이동"):
        st.switch_page("pages/upload.py")
    if st.button("붙여넣기 페이지로 이동"):
        st.switch_page("pages/paste.py")
    st.warning("아직 업로드된 이미지가 없습니다. Upload나 Paste 페이지로 이동하세요.")