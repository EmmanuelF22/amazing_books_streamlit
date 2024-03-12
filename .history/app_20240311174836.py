import streamlit as st
import requests

# Set page configuration to wide layout
st.set_page_config(layout="wide")

# Add a cool picture to the left as a ribbon
cool_image_url = 'URL_OF_YOUR_COOL_PICTURE'
st.image(cool_image_url, caption='Cool Picture', use_column_width=True, width=150)  # Adjust the width as needed

# Center the main title with green color
st.markdown('<h1 style="text-align: center; color: green;">Amazing Books</h1>', unsafe_allow_html=True)

# Set the width of col1 using st.sidebar
col1 = st.sidebar
col1_width = 300  # Adjust the width as needed
col1.markdown(f'<div style="width: {col1_width}px;">', unsafe_allow_html=True)

with st:
    '''
    # Amazing books
    '''

    ############################### GET USER INPUT ####################################

    st.markdown('''
    Tell us what you thought of the book... we'll tell you if you like it!
    ''')

    # Get user's comment
    with st.form(key='params_for_api'):
        model = st.text_input('Model to be used', 'naive')
        comment = st.text_input('Comment', 'excellent book')
        st.form_submit_button('Make prediction')

    params = dict(
        model=model,
        comment=comment
    )

    ################################# CALL THE API ######################################

    url = 'https://amazing-ympfzdipeq-ew.a.run.app/predict'
    response = requests.get(url, params=params)
    prediction = response.json()
    pred = prediction['prediction']

    # Replace the result with other pictures
    if comment != "":
        if pred == 1:
            st.image('URL_OF_GOOD_BOOK_IMAGE', caption='Good Book Image', use_column_width=True)
            st.header('That was a good book, right?')
        else:
            st.image('URL_OF_NOT_LIKED_BOOK_IMAGE', caption='Not Liked Book Image', use_column_width=True)
            st.header("You didn't like it? Me neither...")
