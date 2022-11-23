import streamlit as st

def checkChange():
    print('el valor del check es ' + str(st.session_state.check1))

st.checkbox('Checkbox',value=True,key='check1',on_change=checkChange)

def radioChange():
    print('el valor del check es ' + str(st.session_state.radio1))

st.radio('Radio',options=('opcion1','opción2','Opcion3'),key='radio1',on_change=radioChange)

st.date_input('día',)
