import streamlit as st

name=st.text_input("Enter your name")
btn=st.button('show')

if btn:
    st.write(f'Welcome {name}')

#app 1
st.sidebar.title('Sidebar')
st.header("calculate Area")
choose =st.selectbox('Choose the shape',['circle','rectangle'])
if choose=='circle':
  r=st.number_input('enter the  radius',min_value=1,max_value=100)
  area=r*r*3.14
elif choose=='rectangle':
     w=st.number_input('enter the  width',min_value=1,max_value=100)
     h=st.number_input('enter the  height',min_value=1,max_value=100)
     area=w*h
btn=st.button('calculate')   
if btn:  
  st.write(f'Area is {area}')
