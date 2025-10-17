import streamlit as st
import requests

API_URL = 'http://127.0.0.1:8000/todos/'

st.title('To-Do App')

task = st.text_input('Enter a new task')
if st.button('Add Task'):
    response = requests.post(API_URL, json={'id': len(st.session_state.todos) + 1, 'task': task})
    st.session_state.todos.append(response.json())

if 'todos' not in st.session_state:
    st.session_state.todos = []

if st.session_state.todos:
    for todo in st.session_state.todos:
        st.write(f"{todo['task']} - {'Completed' if todo['completed'] else 'Pending'}")
