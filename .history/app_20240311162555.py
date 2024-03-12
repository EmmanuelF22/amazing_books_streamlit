import streamlit as st
import requests


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


if address!=""
if pred==1:
    st.header(f'that was a good book, right?')
else:
    st.header(f"You didn't like it? me neither...")
