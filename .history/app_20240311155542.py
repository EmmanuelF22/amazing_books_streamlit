import streamlit as st


'''
# Amazing books
'''

st.markdown('''
Tell us what you thought of the book... we'll tell you if you like it!
''')

# Get location input from user
location_input = st.text_input("Enter Location:", "")
