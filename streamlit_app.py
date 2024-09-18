import streamlit as st

import pandas as pd
st.header('file upload')
file=st.file_uploader('upload dataset',type=['csv'])
if file is not None:
  df=pd.read_csv(file)
  st.write(df)
    if btn:  
     st.write(f'Area is {area}')
if btn:  
  st.write(f'Area is {area}')
