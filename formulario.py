import streamlit as st

st.markdown("<h1 style='text-align: center;'>Mi formulario</h1><hr/>", unsafe_allow_html=True)

def getMsgError():
    if st.session_state.txtNombre == "":
        return "Inbrese un nombre."
    elif st.session_state.txtApellido == "":
        return "Ingrese un apellido."
    elif st.session_state.txtEmail == "":
        return "Ingrese un correo electrónico."
    elif st.session_state.Contrasenia == "":
        return "Ingrese una Contraseña."
    elif st.session_state.Contrasenia != st.session_state.Contrasenia2:
        return "Las contraseñas no coinciden."
    else: 
        return ""

with st.form("Form 3"):
    col1,col2=st.columns(2)
    col1.text_input("Nombre", key="txtNombre")
    col2.text_input("Apellido", key="txtApellido")

    st.text_input("Correo electrónico", key="txtEmail")
    st.text_input("Contraseña", type="password", key="Contrasenia")
    st.text_input("Confirmar contraseña", type="password", key="Contrasenia2")
    estatus = st.form_submit_button("Guardar")
    
    if estatus:
        msgError = getMsgError()
        if msgError == "":
            st.success("Los datos fueron enviados exitosamente.")
        else:
            st.warning(msgError)