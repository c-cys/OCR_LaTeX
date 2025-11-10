import streamlit as st

st.title("📤 이미지 업로드 페이지")

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    binary_data = uploaded_file.read()  # 이게 바로 파일의 raw bytes
    st.image(uploaded_file, caption="업로드한 이미지", use_container_width=True)
    st.session_state["uploaded_file"] = binary_data
    st.success("이미지가 저장되었습니다! 이제 Main 페이지로 이동하세요.")

    if st.button("Main 페이지로 이동"):
        st.switch_page("app.py")