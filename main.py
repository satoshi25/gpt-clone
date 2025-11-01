import streamlit as st

is_admin = False

st.header("Hello!")

name = st.text_input("What is your name?")

if name:
    st.write(f"Hello {name}")
    is_admin = True

print(is_admin)