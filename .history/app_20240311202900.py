import streamlit as st
import requests


st.set_page_config(
            page_title="Amazing books", # => Quick reference - Streamlit
            page_icon="📚",   #📓📖📘
            layout="wide", # centered
            initial_sidebar_state="auto") # collapsed


# build a left ribbon
image_url = requests.get("https://m.media-amazon.com/images/I/71q3D33qowL.jpg").url
st.sidebar.title(f"""""")
st.sidebar.image(image_url, width=500)



# build the main page
st.title("How was your book?")


# a) Three option buttons
option = st.radio("Choose an algorithm:", ["Naive", "Option 2", "Option 3"])

# b) Enter text
user_text = st.text_input("Enter text here:")

# Button to trigger the action
if st.button("Generate Result"):
    # Placeholder for result display
    st.success("Result: Placeholder result for {} with text '{}'".format(option, user_text))
