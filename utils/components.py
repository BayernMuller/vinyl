from dataclasses import dataclass
from models.record import Record
from typing import Optional
import streamlit as st
import base64

class RecordGroup:
    def __init__(self, group_name: Optional[str] = None):
        self.__html = '<div>'
        self.__length = 0
        self.__group_name = group_name

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
        # if the cover is a local file, convert it to base64
        if record.cover and not record.cover.startswith('http') and record.cover.endswith('.png'):
            try:
                with open(record.cover, 'rb') as f:
                    record.cover = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
            except FileNotFoundError:
                # if the file is not found, set to default
                record.cover = ''

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
        {f'''<div style="color: gray; font-size: 12px;">
            <text>{record.purchase_date}</text>
        </div>''' if record.purchase_date and self.__group_name == 'purchase_date' else '<div></div>'}
    </div>
</div>
    """
        return html