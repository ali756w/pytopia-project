import streamlit as st
from io import StringIO
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# --- Main Page ---
st.title("Pytopia Dashboard")

# --- banner ---
banner = Image.open('./data/images.jfif')
st.image(banner, use_container_width=True)

# --- login ---
login_option = st.sidebar.radio('Login/SignUp', ('Login', 'SignUp'))

if login_option == 'Login':
    with st.sidebar.form("Login"):
        st.write('Login here')
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass

else:
    with st.sidebar.form("SignUp"):
        st.write('SignUp here')
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        # Every form must have a submit button.
        submitted = st.form_submit_button("SignUp")
        if submitted:
            pass

# --- statistics of members of pytopia's telegram group ---
with st.expander('Statistics'): 
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)

        data = json.loads(string_data)
        st.json(data)

# --- statistic ---
with st.expander('Statistics2'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)

st.metric(label="Pytopia members", value="16000", delta="+100")

# --- User Info ---
with st.expander('User profile'):
    st.write('welcome to your profile')
    col1, col2, = st.columns(2)
    col1.text_input('Enter your name')
    col2.text_input('Enter your location')
    st.camera_input('Take a picture', key='camera_input')