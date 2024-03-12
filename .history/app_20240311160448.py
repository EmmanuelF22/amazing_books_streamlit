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
comment = st.text_input("Enter your comment:", "")






################################# CALL THE API ######################################
params=dict(comment=comment)
url = 'https://amazing-ympfzdipeq-ew.a.run.app/predict'

st.write(f"Location: {comment}")

response = requests.get(url, params=params)

st.write(f"Location: {response}")

prediction = response.json()

st.write(f"Location: {comment}")


pred = prediction['prediction']

st.header(f'prediction: ${round(pred, 2)}')
