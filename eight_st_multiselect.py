"""
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY11
st.multiselect
st.multiselect displays a multiselect widget.
"""

import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What are your favoriate colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('Your selected: ', options)
