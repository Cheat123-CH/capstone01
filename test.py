import streamlit as st
st.set_page_config(
    page_title="AI security",
    page_icon=" :tada",
    layout="wide"
)

with st.container():
    st.subheader("hi I am UX/IU fake designer")
    st.title("A  data analyst from germany")
    st.write("I am possionate about finding ways to use python")

with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I  do")
        st.write("testcode")