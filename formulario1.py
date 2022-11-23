import streamlit  as st

st.write('<h1><center>Prueba de Fromularios</center></h1>', unsafe_allow_html=True) 


#Form 1
form=st.form('Formulario 1')
form.text_input('Nombre: ')
form.text_input('Apellido: ')
form.form_submit_button('Aceptar')

#Form 2
with st.form('Formulario 2'):
    col1,col2,col3=st.columns(2)
    col1.text_input('Nombre: ')
    col2.text_input('Apellido: ')
    st.form_submit_button('Aceptar')