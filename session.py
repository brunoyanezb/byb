import streamlit as st

text = "Texto viejo"

if "submit" not in st.session_state:
    st.session_state.submit = False
else:
    if st.session_state.submit == False:
        text = "Texto nuevo"
        st.session_state.submit = True
    else:
        text = "Texto viejo"
        st.session_state.submit = False

st.text_input("Texto actual", value=text)
btn = st.button("Aceptar")
if btn:
    text = "Texto nuevo"

