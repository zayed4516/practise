import streamlit as st
import time
import pandas as pd
import plotly.express as px
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
fig=px.scatter(df,x='OrderID',y='OrderDetailID')
st.plotly_chart(fig)

num_col=df.select_dtypes(include='number').columns.to_list()
col1,col2,col3=st.columns(3)
with col1:
  x_column=st.selectbox('select the x-axis columns',num_col)
with col2:
  y_column=st.selectbox('select the y-axis columns',num_col)
with col3:
  color=st.selectbox('select color',df.columns.to_list())

fig1=px.scatter(df,x=x_column,y=y_column,color=color)
st.plotly_chart(fig1)

tab1,tab2=st.tabs(['name1','name2'])

with tab1:
  st.write('hello Mohamed')
with tab2:
  st.write('hello zayed')

st.header("session state")
lists=[]
user_name=st.text_input("Enter the list")

if st.button("Enter"):
  lists.append(user_name)
st.write(lists)  
