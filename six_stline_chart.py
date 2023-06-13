"""

@Author: Neel Shah

DOING STREAMLIT 30 DAYS CHALLENGE

@DAY9
st.line_chart
st.line_chart displays a line chart.

This is syntax-sugar around st.altair_chart. The main difference is this command uses the data's own column and indices to figure out the chart's spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

If st.line_chart does not guess the data specification correctly, try specifying your desired chart using st.altair_chart.
"""
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line Chart')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

neel = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.write(neel)

st.subheader('Graph')
st.line_chart(chart_data)
