import streamlit as st


'''
# Amazing books
'''


############################### GET USER INPUT ####################################

st.markdown('''
Tell us what you thought of the book... we'll tell you if you like it!
''')

# Get user's comment
location_input = st.text_input("Enter your comment:", "")






################################# CALL THE API ######################################
url = 'https://amazing-ympfzdipeq-ew.a.run.app/predict'
