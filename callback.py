import streamlit as st

def Saludar(parameter_name, parameter_last_name):
    st.session_state.txtSaludo = "Hola " + parameter_name + " " + parameter_last_name

name = st.text_input("Nombre: ")
last_name = st.text_input("Apellido: ")
btn = st.button("Aceptar")

if btn:
    st.checkbox("¿Quieres que te salude?", on_change=Saludar, args=(name,last_name,))

st.text_area("", key="txtSaludo")