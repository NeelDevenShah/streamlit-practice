"""
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY16
Customizing the theme of Streamlit apps
We can customize the theme by adjusting parameters in config.toml, which is a configuration file stored in the same folder as the app in the .streamlit folder.

What we're building?
A simple app that shows the result of our theme customization. This is made possible by customizing the HTML HEX code inside the .streamlit/config.toml file.

`The other part of the code of the file is written in the .streamlit/config.toml`

"""

import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit.config.toml` file of this app')

st.code("""
        [theme]
        primaryColor = "#F39C12"
        backgroundColor = "#2E86C1"
        secondaryBakgroundColor = "#AED6F1"
        textColor = "#FFFFFF"
        font = "monospace"
        """)

number = st.sidebar.slider('Select a number: ', 0, 10, 5)
st.write('Selected number from slider widget is: ', number)
