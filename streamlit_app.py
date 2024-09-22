import streamlit as st
import time
import pandas as pd
st.header("Upload file")
uploaded_file=st.file_uploader('Choose a file',type=['csv'])
if uploaded_file is not None:
  df=pd.read_csv(uploaded_file)
st.write(df)  
    
