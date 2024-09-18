import streamlit as st
import pandas as pd
st.header('file upload')
file=st.file_uploader('upload dataset',type=['csv'])
if file is not None:
  df=pd.read_csv(file)
  st.write(df)
num_row=st.slider('choose num rows',min_value=1,max_value=len(df))
names_col=st.multiselect('choose columns',df.columns.to_list())
if names_col:
  st.write(df[:num_row][names_col])
else:
  st.write(df[:num_row]) 
