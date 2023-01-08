import streamlit as st
# import pandas as pd
# import numpy as np
import scanner as sc
import url_phishing 
from PIL import Image
from pathlib import Path

from requests.exceptions import MissingSchema

# image = Image.open('images/among-us-sus.gif')

st.title('GPT-Injector ')

user_input = st.text_input(
        "Enter URL:",
        key="placeholder",
        placeholder="This is placeholder",
    )
try:
    result = sc.xss_checker(user_input)
    if not result:
        # st.write('Hello, *World!* ')
        st.write("XSS vulneribility discovered!")
        # print("Attack payload:"+payload)
    else:
        st.write("Secure :sunglasses:")

    res = url_phishing.analyze_url(user_input)

    st.write(res)
    # st.image(image, caption='Sunrise by the mountains')
    # st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
except:
    st.write("PLEASE ENTER A URL : 😀 ")

