"""
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY12
st.multiselect
st.multiselect displays a multiselect widget.
"""

import streamlit as st

st.header('st.checkbox')

st.write('What would you like to order?')

icecream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some more ice cream")

if coffee:
    st.write("Okay, here's some coffee")

if cola:
    st.write("Here you go")
