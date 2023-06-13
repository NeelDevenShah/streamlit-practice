"""
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY14
Streamlit Components
Components are third-party Python modules that extend what's possible with Streamlit [1].

What Streamlit components are available?
There are several dozens of Streamlit components featured on Streamlit's website [2].

Fanilo (a Streamlit Creator) curated an amazing list of Streamlit components on a wiki post [3] that lists about 85 Streamlit components as of April 2022.

How to use?
Streamlit components are just a pip-install away.

In this tutorial, let's get you started in using the streamlit_pandas_profiling component [4].
"""
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv(
    'https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)
