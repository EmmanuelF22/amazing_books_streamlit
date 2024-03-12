import streamlit as st
import requests


st.set_page_config(
            page_title="Amazing books", # => Quick reference - Streamlit
            page_icon="📚",   #📓📖📘
            layout="wide", # centered
            initial_sidebar_state="auto") # collapsed




# 0) Main title
st.title("How was your book?")



# 2) Rest of the page
# a) Three option buttons
option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

# b) Enter text
user_text = st.text_input("Enter text here:")

# Button to trigger the action
if st.button("Generate Result"):
    # Placeholder for result display
    st.success("Result: Placeholder result for {} with text '{}'".format(option, user_text))
