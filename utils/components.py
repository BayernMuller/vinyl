from dataclasses import dataclass
from models.record import Record
import streamlit as st

class RecordGroup:
    def __init__(self):
        self.__html = '<div>'
        self.__length = 0

    def add_record(self, record: Record):
        self.__html += self.__create_record(record)
        self.__length += 1

    def __len__(self):
        return self.__length

    def generate(self, placeholder=None):
        self.__html += '</div>'
        if placeholder is None:
            placeholder = st.empty()
        placeholder.markdown(self.__html, unsafe_allow_html=True)
        self.__html = '<div>'

    def __create_record(self, record: Record) -> str:
        html = f"""
<div style="display: inline-block; width: 150px; height: 260; margin: 0px 10px 10px 0px; vertical-align: top;">
    <img width="150" height="150" src="{record.cover}" style="border-radius: 7px;"/>
    <div class="vynil-info">
        <b>{record.title}</b>
        <div style="color: gray; font-size: 12px;">
            <text>{record.artist}</text>
            <span>•</span>
            <text>{record.year}</text>
            <span>•</span>
            <text>{record.format}</text>
        </div>
    </div>
</div>
    """
        return html