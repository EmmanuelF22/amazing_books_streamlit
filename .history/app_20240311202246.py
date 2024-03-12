import streamlit as st
import requests

# 0) Main title
st.title("Streamlit Skeleton")

# 1) Left ribbon with title and random picture
# st.sidebar.title("Left Ribbon Title")

# Fetch a random image URL from Unsplash
image_url = requests.get("https://source.unsplash.com/random/400x800").url  # Adjusted for portrait mode
st.sidebar.image(image_url, width=450)

# 2) Rest of the page
# a) Three option buttons
option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

# b) Enter text
user_text = st.text_input("Enter text here:")

# Button to trigger the action
if st.button("Generate Result"):
    # Placeholder for result display
    st.success("Result: Placeholder result for {} with text '{}'".format(option, user_text))
