import streamlit as st

# 초기 LaTeX 코드
initial_latex = st.session_state.get("latex_result")
# initial_latex = "$$ {x^{2}+y^{2}=1} $$"
initial_latex = initial_latex.replace("$$","").strip()

# 텍스트 에어리어로 편집 가능
edited_latex = st.text_area("LaTeX 편집기", initial_latex, height=200)

# 실시간 렌더링
st.subheader("미리보기")
st.write("Ctrl+Enter 눌러서 미리보기 Apply")
st.latex(edited_latex)

if st.button("Main 페이지로 이동"):
    st.switch_page("app.py")