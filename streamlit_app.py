import streamlit as st
import time
st.sidebar.title('Sidebar')
st.header("Calculate Area")

with st.sidebar:
  choose=st.selectbox("Enter the shape",['Circle','rectangle'])
  if choose=='Circle':
    r=st.number_input("Enter the raduis",min_value=1,max_value=50)
    area=r*r*3.14
  elif choose=='rectangle':
    h=st.number_input("Enter the length",min_value=1,max_value=50)
    w=st.number_input("Enter the width",min_value=1,max_value=50)
    area=h*w
  btn=st.button("Calculate")
  if btn:
     with st.spinner('Calculating...'):
      time.sleep(2)
    st.write(f"the area {area}")    
    
