import streamlit as st
# import pandas as pd
# import numpy as np

st.title('GPT-Injector ')

user_input = st.text_input(
        "Enter URL:",
        key="placeholder",
        placeholder="This is placeholder",
    )
