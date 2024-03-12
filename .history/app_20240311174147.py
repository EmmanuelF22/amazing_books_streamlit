import streamlit as st
import requests


st.set_page_config(
            page_title="Amazing books", # => Quick reference - Streamlit
            page_icon="📚",   #📓📖📘
            layout="wide", # centered
            initial_sidebar_state="auto") # collapsed



'''
# Amazing books
'''


############################### GET USER INPUT ####################################

col1, col2 = st.columns(2)

# Add a cool picture to the landing page
with col1:
    cool_image_url = 'https://www.architecturalrecord.com/ext/resources/Issues/2017/interiors/1701-Perspective-Interiors-X-Living-01.jpg'
    st.image(cool_image_url, use_column_width=True)



with col2:
    st.title(f'Tell us what you thought of the book... we'll tell you if you like it!"")
    ''')
    # st.markdown('''
    # Tell us what you thought of the book... we'll tell you if you like it!
    # ''')
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

    bad_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrljoYufSv3dqt2Z08kMHZnKNR9ZvtxYSUU_ssg15i8z4XxkG_WNe7V1JQx4CKjx-tQcY&usqp=CAU'
    good_url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Thumb_up_icon.svg/1200px-Thumb_up_icon.svg.png'


    if comment != "":
        if pred == 1:
            st.image(good_url, use_column_width=True)    #add caption=positive
            st.header('That was a good book, right?')
        else:
            st.image(bad_url, use_column_width=True)
            st.header("You didn't like it? Me neither...")
