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

    pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_datetime = f'{pickup_date} {pickup_time}'
    pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
    pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
    dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
    dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
    passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

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
