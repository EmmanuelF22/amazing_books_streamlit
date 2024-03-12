import streamlit as st
import requests


st.set_page_config(
            page_title="Amazing books", # => Quick reference - Streamlit
            page_icon="📚",   #📓📖📘
            layout="wide", # centered
            # backgroundColor="#3498db",  # Adjusted background color to blue
            initial_sidebar_state="auto") # collapsed


CSS = """
h1 {
    color: red;
}
.stApp {
    background-image: url(https://avatars1.githubusercontent.com/u/9978111?v=4);
    background-size: cover;
}
"""

# build a left ribbon
image_url = requests.get("https://m.media-amazon.com/images/I/71q3D33qowL.jpg").url
st.sidebar.title(f"""""")
st.sidebar.image(image_url, width=500)



# build the main page
st.title("How was your book?")


# a) Three option buttons
model = st.radio("Choose an algorithm:", ["Naive Bayes", "LSTM", "Conv1D"])

# b) Enter text
comment = st.text_input("Enter a comment:")

# Button to trigger the action
if st.button("Generate prediction"):

    params=dict(
    modele=model,
    comment=comment
    )

    ################################# CALL THE API ######################################

    url = 'https://amazing-ympfzdipeq-ew.a.run.app/predict'

    response = requests.get(url, params=params)

    prediction = response.json()

    pred = prediction['prediction']

    bad_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrljoYufSv3dqt2Z08kMHZnKNR9ZvtxYSUU_ssg15i8z4XxkG_WNe7V1JQx4CKjx-tQcY&usqp=CAU'
    good_url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Thumb_up_icon.svg/1200px-Thumb_up_icon.svg.png'


    st.title("")
    st.title("")

    if comment != "":
        if pred == 1:
            # Use columns to display image and header on the same line
            col1, col2 = st.columns([1, 3])
            col1.image(good_url, width=100)  # Adjusted width for smaller image
            col2.header('That was a good book, right?')
        else:
            # Use columns to display image and header on the same line
            col1, col2 = st.columns([1, 3])
            col1.image(bad_url, width=100)  # Adjusted width for smaller image
            col2.header("You didn't like it? Me neither...")
