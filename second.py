import streamlit as st

"""

@Author: Neel Shah

DOING STREAMLIT 30 DAYS CHALLENGE

@DAY3
"""


st.header('st.button')

if st.button('Say Hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
