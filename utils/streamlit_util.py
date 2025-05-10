
import streamlit as st
from streamlit.components.v1 import html

def remove_streamlit_style():
    st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def get_query_params_from_url():
    return st.query_params

def set_query_params_to_url(params: dict[str, str]) -> None:
    print(params)
    for k, v in params.items():
        st.query_params.items[k] = v