import streamlit as st
import time
import pandas as pd
st.header('file uploaded')
uploaded_file=st.file_uploader('Choose the file',type=['csv'])
if uploaded_file is not None:
  df=pd.read_csv(uploaded_file)
  n_rows=st.slider('Enter the number of rows',min_value=1,max_value=len(df),step=1,value=1)
  columns_choose=st.multiselect('Choose the columns',df.columns.to_list())
  if columns_choose:
    st.write(df[:n_rows][columns_choose])
  else:
    st.write(df[:n_rows])
