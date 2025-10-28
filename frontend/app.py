'''
frontend/app.py
Streamlit 웹 UI
'''
import streamlit as st
import requests
import to_LaTeX

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="OCR + Text Summarizer", page_icon="🧠")

st.title("이미지 텍스트 요약기")
st.write("이미지를 업로드하면, 텍스트를 읽고 요약해줍니다!")

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 일단 먼저 업로드한 이미지를 띄움
    st.image(uploaded_file, caption="업로드한 이미지", use_container_width=True)

    # OCR 요청
    with st.spinner("텍스트를 추출 중입니다..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{BACKEND_URL}/ocr", files={"file": uploaded_file})
        ocr_result = response.json().get("text", "")
        st.subheader("📜 인식된 텍스트")
        st.text_area("추출 결과", ocr_result, height=200)

    # LaTeX 변환기
        latex_result = to_LaTeX.to_LaTeX(uploaded_file)
        st.subheader("🔢 LaTeX 문법에 맞게 변환된 수식")
        st.text_area("변환 결과", latex_result, height=200)

    # 요약 기능
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("요약하기"):
        with st.spinner("요약 중입니다..."):
            res = requests.post(f"{BACKEND_URL}/summary", json={"text": ocr_result})
            summary = res.json().get("summary", "")
            st.subheader("🪄 요약 결과")
            st.write(summary)