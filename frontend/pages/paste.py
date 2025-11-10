import streamlit as st
from st_img_pastebutton import paste
from io import BytesIO
import base64
from PIL import Image

st.title("📤 이미지 붙여넣기(Ctrl+V) 페이지")

image_data = paste(label="📋 이미지 붙여넣기", key="image_clipboard")

if image_data is not None:
    header, encoded = image_data.split(",", 1)
    binary_data = base64.b64decode(encoded)
    st.image(binary_data, caption="붙여넣은 이미지", use_container_width=True)
    st.session_state["uploaded_file"] = binary_data  # PIL 없이 바로 저장

    # img_bytes = BytesIO(binary_data)
    # uploaded_file = Image.open(img_bytes)
    # st.image(uploaded_file, caption="붙여넣은 이미지", use_container_width=True)
    # st.session_state["uploaded_file"] = uploaded_file

    st.success("이미지가 저장되었습니다! 이제 Main 페이지로 이동하세요.")

    if st.button("Main 페이지로 이동"):
        st.switch_page("app.py")