import streamlit as st
from pdf2image import convert_from_path
from strikedtext import striked_remove_text
from pathlib import Path
import os
import warnings
warnings.filterwarnings('ignore')

st.title('Cargo Exclusion')













hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)