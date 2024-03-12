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

bad_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrljoYufSv3dqt2Z08kMHZnKNR9ZvtxYSUU_ssg15i8z4XxkG_WNe7V1JQx4CKjx-tQcY&usqp=CAU'
good_url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Thumb_up_icon.svg/1200px-Thumb_up_icon.svg.png'


if comment != "":
    if pred == 1:
        st.image(good_url, use_column_width=True)
        st.header('That was a good book, right?')
    else:
        st.image(bad_url, use_column_width=True)
        st.header("You didn't like it? Me neither...")
