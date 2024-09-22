import streamlit as st
st.header("hello practise")
name=st.text_input("Enter your name")
btn=st.button("start")
if btn:
  st.write(f"hello {name}")
  
st.header('Calculate area')
choose=st.selectbox('choose the shape',['Circle','rectangle'])
if choose=='Circle':
  r=st.number_input('Enter the radius',min_value=1,max_value=50)
  area=r*r*3.14
elif choose=='rectangle':
  h=st.number_input('Enter the length',min_value=1,max_value=50)
  w=st.number_input('Enter the width',min_value=1,max_value=50)
  area=h*w
btn=st.button('calculate')
if btn:
  st.write('the area:{area}')
