import streamlit as st
st.header("hello practise")
name=st.text_input("Enter your name")
btn=st.button("start")
if btn:
  st.write(f"hello{name}")
