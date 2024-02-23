from dataclasses import dataclass
from models.record import Record
from babel.numbers import format_currency
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
    <div class="vinyl-info">
        <b>{record.title}</b>
        <div style="color: gray; font-size: 12px;">
            <text>{record.artist}</text>
            <span>•</span>
            <text>{record.year}</text>
            <span>•</span>
            <text>{record.format}</text>
        </div>
        {self.__create_purchase_info(record)}
    </div>
</div>
    """
        return html

    def __create_purchase_info(self, record: Record) -> str:
        if not record.purchase or self.__group_name != 'purchase_date':
            return '<div></div>'

        price_html = f"""<div style="color: gray; font-size: 12px;">
            <text>💵 {format_currency(record.purchase_price[1], record.purchase_price[0])}</text>
        </div>""" if record.purchase_price else '<div></div>'


        others = [
            f'<text>{value}</text>' for value in [
                record.purchase_location if record.purchase_location else None,
                record.purchase_date if record.purchase_date else None,
            ] if value
        ]
        others_html = f"""<div style="color: gray; font-size: 12px;">
            <text>🛒 </text>
            {"<span>•</span>".join(others)}
        </div>""" if others else '<div></div>'

        return f"{price_html}{others_html}"
