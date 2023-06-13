"""
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY15
st.latex
st.latex display mathematical expressions formatted as LaTeX.

What we're building?
A simple app that displays a mathematical equation using LaTeX syntax via the st.latex command.
"""

import streamlit as st

st.header('st.latex')

st.latex(r'''
         a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
         ''')
