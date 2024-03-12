import streamlit as st
import requests


st.set_page_config(
            page_title="Amazing books", # => Quick reference - Streamlit
            page_icon="📚",   #📓📖📘
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed


'''
# Amazing books
'''


############################### GET USER INPUT ####################################

col1, col2 = st.columns(2)

# Add a cool picture to the landing page
with col1:
    cool_image_url = 'https://www.architecturalrecord.com/ext/resources/Issues/2017/interiors/1701-Perspective-Interiors-X-Living-01.jpg'
    st.image(cool_image_url, caption='book store', use_column_width=True)

    st.markdown('''
    Tell us what you thought of the book... we'll tell you if you like it!
    ''')

with col2:

