import streamlit as st

def changeOptions():
    return str(st.session_state.Options)

with st.sidebar:
    st.write("Mi sidebar")
    st.radio("Red social", options=("Facebook","Instagram","Twitter","Tiktok"), on_change=changeOptions, key="Options")

st.markdown("<h2 style='text-align: center;'>Contenido de mi página</h2><hr/>", unsafe_allow_html=True)
st.markdown("El usuario selecciono **" + changeOptions() + "**")
