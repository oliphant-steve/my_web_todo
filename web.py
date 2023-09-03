import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo =st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.save_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productiity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)  # remove to checked todo
        functions.save_todos(todos)  # save the new todo list
        del st.session_state[todo]  # remove the checked todo from the session state
        st._rerun()  # rerun the code to get the new todo list


st.text_input(label="label", label_visibility="hidden", placeholder="enter a new todo", on_change=add_todo, key="new_todo")