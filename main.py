from utils.components import Record, RecordData
from utils.streamlit_util import remove_streamlit_style, set_page_wide
import streamlit as st

def sort_func(x, tag_list):
    return ''.join([str(x.get(tag)) for tag in tag_list])

#remove_streamlit_style()
set_page_wide()

record_list = eval(open('list.json', 'r').read())

st.title('')
st.markdown('**My record collection**')
summary = st.empty()

group_by = {
    'artist': {'sort_by': ['year', 'title'], },
    'genre': {'sort_by': ['artist', 'year'], },
    'format': {'sort_by': ['artist', 'year'], },
    'year': {'sort_by': ['artist', 'title'], },
    'none': {'sort_by': ['artist', 'year'], },
}

with st.expander('options'):
    group_name = st.selectbox('group by', list(group_by.keys()))

group_info = group_by[group_name]
sort_by = group_info.get('sort_by')

table = {}
for record in record_list:
    group = record.get(group_name)
    if group not in table:
        table[group] = []
    table[group].append(record)
    table[group] = sorted(table[group], key=lambda x: sort_func(x, sort_by))
    
table = dict(sorted(table.items(), key=lambda x: x[0]))

count = {}
for group, records in table.items():
    st.write('---')
    if group_name != 'none':
        st.subheader(group)

    record_widget = Record()
    for record in records:
        record_obj = RecordData(record)

        record_widget.add_record(record_obj)
        if record_obj.format not in count:
            count[record_obj.format] = 0

        count[record_obj.format] += 1

    record_widget.generate()

summary.markdown(f'Totally {"".join([f"{count[format]} {format}s, " for format in count])[:-2]}')
