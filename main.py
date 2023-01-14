from utils.components import Vinyl, VynilData
from utils.streamlit_util import remove_streamlit_style, set_page_wide
import streamlit as st

set_page_wide()
remove_streamlit_style()

st.title("My Vinyl Collection")

vinyl_list = eval(open('list.json', 'r').read())

vinyl = Vinyl()
for vynil in vinyl_list:
    vinyl.add_vynil(VynilData(vynil))
vinyl.generate()