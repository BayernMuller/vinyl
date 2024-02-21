from dataclasses import dataclass
import streamlit as st

@dataclass
class RecordData:
    cover: str
    artist: str
    title: str
    year: int
    genre: str
    format: str

    def __init__(self, source: dict=dict()):
        self.cover = source.get('cover')
        self.artist = source.get('artist')
        self.title = source.get('title')
        self.year = source.get('year')
        self.genre = source.get('genre')
        self.format = source.get('format')

    def __str__(self):
        return f'{self.artist} {self.title} {self.year} {self.genre} {self.format}'

class Record:
    def __init__(self):
        self.__html = '<div>'
        self.__length = 0

    def add_record(self, vynil: RecordData):
        self.__html += self.__create_vynil(vynil)
        self.__length += 1

    def __len__(self):
        return self.__length

    def generate(self, placeholder=None):
        self.__html += '</div>'
        if placeholder is None:
            placeholder = st.empty()
        placeholder.markdown(self.__html, unsafe_allow_html=True)
        self.__html = '<div>'

    def __create_vynil(self, vynil: RecordData) -> str:
        # div align to top
        html = f"""
<div style="display: inline-block; width: 150px; height: 260; margin: 0px 10px 10px 0px; vertical-align: top;">
    <img width="150" height="150" src="{vynil.cover}" style="border-radius: 7px;"/>
    <div class="vynil-info">
        <b>{vynil.title}</b>
        <div style="color: gray; font-size: 12px;">
            <text>{vynil.artist}</text>
            <span>•</span>
            <text>{vynil.year}</text>
            <span>•</span>
            <text>{vynil.format}</text>
        </div>
    </div>
</div>
    """
        return html