"""
    
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY10
st.selectbox
st.selectbox allows the display of a select widget.

What we're building?
A simple app that asks the user what their favorite color is.

Flow of the app:

User selects a color
App prints out the selected color
"""

import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    {'Blue', 'Red', 'Green'})

st.write('Your favorite color is ', option)
