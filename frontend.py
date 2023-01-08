import streamlit as st
# import pandas as pd
# import numpy as np
import scanner as sc
import url_phishing 

from requests.exceptions import MissingSchema


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
except:
    st.write("PLEASE ENTER A URL : 😀 ")

