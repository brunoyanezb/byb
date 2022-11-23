import streamlit as st

st.text("función text()")
st.title('función title()')
st.header('función header()')
st.subheader('funcion subheader()')
st.write('función write()')

st.markdown('función markdown()')
st.markdown('---')
st.markdown('este es un texto en **negrita**')
st.markdown('<h1>cabecera de markdown</h1>',unsafe_allow_html=True)

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


json={'campo1':'valor1','campo2':'valor2'}
st.json(json)