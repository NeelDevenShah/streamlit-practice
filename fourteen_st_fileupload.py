"""
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY18
st.file_uploader
st.file_uploader displays a file uploader widget https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader

By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config option. For more info on how to set config options, see https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options

For advance settings of port and other things https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options
"""

import streamlit as st
import pandas as pd

st.title('st.file_upload')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Desciptive Statistics')
    st.write(df.describe())
else:
    st.info('Upload a CSV file')
