"""
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY27
Build a draggable and resizable dashboard with Streamlit Elements
Streamlit Elements is a third-party component made by https://github.com/okld that gives you the tools to compose beautiful applications and dashboards with Material UI widgets, Monaco editor (Visual Studio Code), Nivo charts, and more.

What are we building?
The goal of today's challenge is to create a dashboard composed of three Material UI cards:

** You can refer to https://github.com/okld/streamlit-elements#getting-started for an in-depth usage guide.

A first card with a Monaco code editor to input some data ;
A second card to display that data in a Nivo Bump chart ;
A third card to show a YouTube video URL defined with a st.text_input.
You can use data generated from Nivo Bump demo there, in 'data' tab: https://nivo.rocks/bump/.
"""

import json
import streamlit as st
from pathlib import Path

# As for Streamlit Elements, we will need all these objects.
# All available objects and there usage are listed there: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Change page layout to make the dashboard take the whole page

st.set_page_config(layout="wide")

with st.slider:
    st.title("#30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # Define URl for media player.
    media_url = st.text_input(
        "Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")
