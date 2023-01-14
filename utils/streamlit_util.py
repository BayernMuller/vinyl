
import streamlit as st

def remove_streamlit_style():
    st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    # remove red border around the app
    
def set_page_wide():
    st.set_page_config(layout="wide")