"""

@Author: Neel Shah

DOING STREAMLIT 30 DAYS CHALLENGE

@DAY8
st.slider
st.slider allows the display of a slider input widget.

The following data types are supported: int, float, date, time, and datetime.

What we're building?
A simple app that shows the various ways on how to accept user input by adjusting the slider widget.

Flow of the app:

User selects value by adjusting the slider widget
App prints out the selected value
"""

import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range Slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3
st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for: ", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")

st.write("Start time: ", start_time)
