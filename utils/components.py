from dataclasses import dataclass
import streamlit as st

class VynilData:
    cover: str
    artist: str
    title: str
    year: int
    genre: str

    def __init__(self, source: dict):
        self.cover = source.get('cover')
        self.artist = source.get('artist')
        self.title = source.get('title')
        self.year = source.get('year')
        self.genre = source.get('genre')


class Vinyl:
    def __init__(self):
        self.__html = '<div>'

    def add_vynil(self, vynil: VynilData):
        self.__html += self.__create_vynil(vynil)

    def generate(self, placeholder=None):
        self.__html += '</div>'
        if placeholder is None:
            placeholder = st.empty()
        placeholder.markdown(self.__html, unsafe_allow_html=True)
        self.__html = '<div>'

    def __create_vynil(self, vynil: VynilData) -> str:
        html = f"""
<div style="display: inline-block; width: 200px; height: 260px; margin: 10px;"> 
    <img width="180" height="180" src="{vynil.cover}" />
    <div class="vynil-info">
        <b>{vynil.title}</b>
        <div style="color: gray;">
            <a>{vynil.artist}</a>
            <span>•</span>
            <a>{vynil.year}</a>
        </div>
    </div>
</div>
    """
        return html