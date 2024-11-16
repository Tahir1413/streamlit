import streamlit as st



st.title("My Simple Streamlit App")



name = st.text_input("Enter your name:")



if name:

    st.write("Hello, ", name, "!") 

