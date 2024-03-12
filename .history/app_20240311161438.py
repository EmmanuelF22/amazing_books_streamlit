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

    model = st.text_input('Model to be used', 'naive')
    comment = st.text_input('Model to be used', 'excellent book')
    st.form_submit_button('Make prediction')

params=dict(
    model=model,
    comment=comment
    )


################################# CALL THE API ######################################

url = 'https://amazing-ympfzdipeq-ew.a.run.app/predict?'


st.write(f"comment: {comment}")

response = requests.get(url, params=params)

st.write(f"response: {response}")

prediction = response.json()

st.write(f"prediction: {prediction}")


pred = prediction['prediction']

st.header(f'prediction: ${round(pred, 2)}')
