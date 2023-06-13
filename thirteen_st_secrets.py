"""
@Author: Neel Shah
    
DOING STREAMLIT 30 DAYS CHALLENGE

@DAY17
st.secrets
st.secrets allows you to store confidential information such as API keys, database passwords or other credentials.
"""

import streamlit as st

st.title('`st.secrets`')

st.write(st.secrets['message'])

"""

    It should be noted that, secrets can be stored in Streamlit Community Cloud by going in to the https://streamlit.io/cloud?ref=blog.streamlit.io, And than on the deployed app there would be an option of the secret key, FOR MORE DETAILS ABOUT IT CHECK https://blog.streamlit.io/secrets-in-sharing-apps/ OR https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management

    If working locally, they can be stored in .streamlit/secrets.toml, but make sure to avoid uploading this to a GitHub repo when deploying the app.

    """
""""
TEMPLATE FORMAT FOR THE secrets.toml file

# Everything in this section will be available as an environment variable 
db_username = "Jane"
db_password = "12345qwerty"

# You can also add other sections if you like.
# The contents of sections as shown below will not become environment variables,
# but they'll be easily accessible from within Streamlit anyway as we show
# later in this doc.
[my_cool_secrets]
things_i_like = ["Streamlit", "Python"]

"""

"""
    Use secrets in your Streamlit app
    To use secrets in your app, you'll want to access your secrets as environment variables or by querying the st.secrets dict. For example, if you enter the secrets from the section above, the code below shows you how you can access them within your Streamlit app.


import streamlit as st

# Everything is accessible via the st.secrets dict:

    st.write("DB username:", st.secrets["db_username"])
    st.write("DB password:", st.secrets["db_password"])
    st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

    # And the root-level secrets are also accessible as environment variables:

    import os
    st.write(
        "Has environment variables been set:",
        os.environ["db_username"] == st.secrets["db_username"])
    """
