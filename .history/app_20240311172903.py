import streamlit as st
import requests


'''
# Amazing books
'''


############################### GET USER INPUT ####################################

# Add a cool picture to the landing page
cool_image_url = 'https://www.architecturalrecord.com/articles/12100-zhongshuge-bookstore-by-xliving'
st.image(cool_image_url, caption='book store', use_column_width=True)

st.markdown('''
Tell us what you thought of the book... we'll tell you if you like it!
''')

# Get user's comment
with st.form(key='params_for_api'):

    model = st.text_input('Model to be used', 'naive')
    comment = st.text_input('Model to be used', 'excellent book')
    st.form_submit_button('Make prediction')

params=dict(
    modele=model,
    comment=comment
    )


################################# CALL THE API ######################################

url = 'https://amazing-ympfzdipeq-ew.a.run.app/predict'


response = requests.get(url, params=params)

prediction = response.json()

pred = prediction['prediction']


if comment!="":
    if pred==1:
        st.header(f'that was a good book, right?')
    else:
        st.header(f"You didn't like it? me neither...")
if comment != "":
    if pred == 1:
        st.image('URL_OF_GOOD_BOOK_IMAGE', caption='Good Book Image', use_column_width=True)
        st.header('That was a good book, right?')
    else:
        st.image('URL_OF_NOT_LIKED_BOOK_IMAGE', caption='Not Liked Book Image', use_column_width=True)
        st.header("You didn't like it? Me neither...")
