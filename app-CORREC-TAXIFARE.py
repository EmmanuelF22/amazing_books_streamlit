import streamlit as st
import requests
import datetime
import folium
from geopy.geocoders import Nominatim

'''
# TaxiFare
'''

st.markdown('''
Welcome on taxifare
''')

'''
## Please enter the following info:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

st.title("Location Entry App")

# Get location input from user
location_input = st.text_input("Enter Location:", "")

if st.button("Check Location"):
    # Validate and process the location
    validated_location = process_location(location_input)

    # Display the results
    display_results(validated_location)

def process_location(location_input):
    geolocator = Nominatim(user_agent="location_app")

    try:
        location = geolocator.geocode(location_input)
        return location
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def display_results(validated_location):
    if validated_location:
        st.success("Location validated successfully!")
        st.write(f"Location: {validated_location.address}")
        st.write(f"Latitude: {validated_location.latitude}")
        st.write(f"Longitude: {validated_location.longitude}")
    else:
        st.warning("Unable to validate the location. Please enter a valid location.")




date = st.date_input("When do you want to travel")
pickup_adress= st.text_input('Pick-up location:', 'Type here')
# datetime.date(2019, 7, 6)

st.title("Address Entry App")

# Get address from user
address = st.text_input("Enter Address:", "")



'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
