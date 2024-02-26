
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
    params = st.experimental_get_query_params()
    dict_param = {
        k: v[0] if isinstance(v, list) else v for k, v in params.items()
    }
    return dict_param

def set_query_params_to_url(params: dict[str, str]) -> None:
    params = {k: v for k, v in params.items() if v}
    st.experimental_set_query_params(**params)