import streamlit as st
import folium

from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import datetime
import requests

import os
my_key = os.environ.get('API_MAPS_KEY')

'''
# TaxiFare
'''
geolocator = Nominatim(user_agent="location_entry_app")


def main():
    warning_shown=False
    st.markdown('''
    Welcome on taxifare
    ''')

    date = st.date_input("When do you want to travel")
    time = st.time_input('when?', datetime.time(8, 45))
    date_time=f'{date}%20{time}'


    # Pick-up
    pickup_address = st.text_input("Enter pick up location:", "Paris", key="location_input1", help="Start typing for suggestions")

    try:
        if pickup_address:
            suggestions = [result.address for result in geolocator.geocode(pickup_address, exactly_one=False)]
            pickup_address=suggestions[0]
    except:
        warning_shown=True
        st.warning("Unable to validate the location. Please enter a valid location.")
    pickup_coordinates = get_coordinates(pickup_address)

    display_results(pickup_address, pickup_coordinates,warning_shown)

    warning_shown=False
    dropoff_address = st.text_input("Enter drop off location:", "Paris", key="location_input2", help="Start typing for suggestions")
    try:
        if dropoff_address:
            suggestions = [result.address for result in geolocator.geocode(dropoff_address, exactly_one=False)]
            dropoff_address=suggestions[0]
    except:
        warning_shown=True
        st.warning("Unable to validate the location. Please enter a valid location.")
    dropoff_coordinates = get_coordinates(dropoff_address)
    display_results(dropoff_address, dropoff_coordinates,warning_shown)

    passenger_count = st.slider('How many passengers?', 1, 6, 1)


    url = 'https://taxifare.lewagon.ai/predict?'
    url += f'pickup_datetime={date_time}'
    url += f'&pickup_longitude={pickup_coordinates[1]}'
    url += f'&pickup_latitude={pickup_coordinates[0]}'
    url += f'&dropoff_longitude={dropoff_coordinates[1]}'
    url += f'&dropoff_latitude={dropoff_coordinates[0]}'
    url += f'&passenger_count={passenger_count}'


   # url = "https://weather.lewagon.com/geo/1.0/direct?q=Barcelona"
    response = round(requests.get(url).json()['fare'],2)

    #works fine!
    #st.title(response)

    dico_api = {
        'pickup_datetime':f"{date} {time}",
        'pickup_longitude':float(pickup_coordinates[1]),
        'pickup_latitude':float(pickup_coordinates[0]),
        'dropoff_longitude':float(dropoff_coordinates[1]),
        'dropoff_latitude':float(dropoff_coordinates[0]),
        'passenger_count':passenger_count
    }

    import urllib.parse

    # BASE_URI = "https://weather.lewagon.com"
    # url = urllib.parse.urljoin(BASE_URI, "/data/2.5/forecast")
    url = 'https://taxifare.lewagon.ai/predict?'
    forecasts = round(requests.get(url, params=dico_api).json()['fare'],2)

    #works fine!
    #st.title(forecasts)

    f"Your fare will be {forecasts}"

    pickup_latitude = pickup_coordinates[0]
    pickup_longitude = pickup_coordinates[1]
    dropoff_latitude = dropoff_coordinates[0]
    dropoff_longitude = dropoff_coordinates[1]

    # Embed Google Maps using an iframe
    map_url = f"https://www.google.com/maps/embed/v1/directions?key={my_key}&origin={pickup_latitude},{pickup_longitude}&destination={dropoff_latitude},{dropoff_longitude}"
    iframe = f'<iframe width="600" height="450" frameborder="0" style="border:0" src="{map_url}" allowfullscreen></iframe>'
    st.components.v1.html(iframe, height=600)


def display_results(address, coordinates, warning_shown):

    if coordinates:
        st.success(f"{address}")
        # st.write(f"Location considered: \n {address}")
        st.write(f"Latitude: {coordinates[0]} | Longitude: {coordinates[1]}")
    else:
        if address!="" and not warning_shown:
            st.warning("Unable to validate the location. Please enter a valid location.")


def get_coordinates(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return [location.latitude, location.longitude]
        else:
            return None
    except:
        pass







if __name__ == "__main__":
    main()
