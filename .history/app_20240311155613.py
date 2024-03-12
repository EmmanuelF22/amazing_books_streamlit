import streamlit as st


'''
# Amazing books
'''

st.markdown('''
Tell us what you thought of the book... we'll tell you if you like it!
''')

# Get user's comment
location_input = st.text_input("Enter your comment:", "")


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
