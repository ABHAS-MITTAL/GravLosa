import streamlit as st
from chatbot import get_gravlosa_reply
from openai import OpenAI

st.set_page_config(page_title="Gravlosa", page_icon="🤖")
st.title(":robot_face: Gravlosa - Your AI Chat Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = get_gravlosa_reply(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Gravlosa", response))

for speaker, text in reversed(st.session_state.history):
    st.markdown(f"**{speaker}:** {text}")
