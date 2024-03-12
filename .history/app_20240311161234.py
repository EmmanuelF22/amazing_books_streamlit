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
modele = st.text_input("Model to be used:", "")
comment = st.text_input("Enter your comment:", "")

with st.form(key='params_for_api'):

    passenger_count = st.text_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

    st.form_submit_button('Make prediction')





################################# CALL THE API ######################################
params=dict(comment=comment)
url = 'https://amazing-ympfzdipeq-ew.a.run.app/predict?'


st.write(f"comment: {comment}")

response = requests.get(url, params=params)

st.write(f"response: {response}")

prediction = response.json()

st.write(f"prediction: {prediction}")


pred = prediction['prediction']

st.header(f'prediction: ${round(pred, 2)}')
