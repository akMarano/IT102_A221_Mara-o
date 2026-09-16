import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List")

new_task = st.text_input("New task")
if st.button("Add"):
    st.session_state.tasks.append({"name": new_task, "done": False})

for i, task in enumerate(st.session_state.tasks):
    task["done"] = st.checkbox(task["name"], value=task["done"], key=f"task_{i}")