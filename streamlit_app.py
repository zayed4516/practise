import streamlit as st
import pandas as pd
import plotly.express as px

st.header('file upload app 2')
file = st.file_uploader('upload dataset',type=['csv'])
if file is not None:
  df = pd.read_csv(file)
  st.write(df)

num_row = st.slider('choose num rows',min_value=1,max_value=len(df),step=1)
names_column = st.multiselect('choose names of columns',df.columns.to_list())
st.write(df[:num_row][names_column])

if names_column:
  st.write(df[:num_row][names_column])
else:
  st.write(df[:num_row])

num_col = df.select_dtypes(include='number').columns.to_list()

col1,col2,col3 = st.columns(3)
with col1:
 x_col = st.selectbox('choose x column',num_col)
with col2:
  y_col = st.selectbox('choose y column',num_col)
with col3:
  color = st.selectbox('choose color',df.columns.to_list())


fig = px.scatter(df,x=x_col,y=y_col,color=color)
st.plotly_chart(fig)

