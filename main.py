import streamlit as st
from agents import Agent, Runner, SQLiteSession

if "session" not in st.session_state:
    st.session_state["session"] = SQLiteSession(
        "chat-history", 
        "chat-gpt-clone-memory.db"
    )

session = st.session_state["session"]

