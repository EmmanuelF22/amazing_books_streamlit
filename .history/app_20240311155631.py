import streamlit as st


'''
# Amazing books
'''


################################# CALL THE API ######################################

st.markdown('''
Tell us what you thought of the book... we'll tell you if you like it!
''')

# Get user's comment
location_input = st.text_input("Enter your comment:", "")


################################# CALL THE API ######################################
