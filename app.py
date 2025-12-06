import streamlit as st

st.title("My First Interactive App")

# Ask for user's name
name = st.text_input("What's your name?")

# Display personalized greeting if name is entered
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")
else:
    st.write("Hello, World! Please enter your name above.")
