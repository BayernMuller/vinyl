from utils.components import Record, RecordData
from utils.streamlit_util import remove_streamlit_style, set_page_wide
import streamlit as st

def sort_func(x, tag_list):
    return ''.join([str(x.get(tag)) for tag in tag_list])

set_page_wide()
remove_streamlit_style()

try:
    list_file = open('list.json', 'r')
except FileNotFoundError:
    st.success("Welcome to your new record list! Add your records to a file named 'list.json' and run the app again.")
    st.balloons()
    st.stop()

try:
    record_list = eval(list_file.read())
except Exception as e:
    st.error(f'Error reading list.json. Please check the JSON format and try again.')
    st.stop()

st.title('Records')
summary = st.empty()

group_by = {
    'artist': {'sort_by': ['year', 'title'], },
    'genre': {'sort_by': ['artist', 'year'], },
    'format': {'sort_by': ['artist', 'year'], },
    'year': {'sort_by': ['artist', 'title'], },
    'country': {'sort_by': ['artist', 'year'], },
    'none': {'sort_by': ['artist', 'year'], },
}

index_format = list(group_by.keys()).index('format')

with st.sidebar:

    with st.expander('search', expanded=True):
        search = st.text_input('search', key='search')

    with st.expander('options', expanded=True):
        group_name = st.radio('group by', list(group_by.keys()), index=index_format, key='group_by')
        group_order = st.radio('order', ['ascending', 'descending'], index=0, key='order', horizontal=True)

    
    st.write("Developed by [@BayernMuller](https://github.com/bayernmuller)")
    st.write("Fork this template from [here](https://github.com/BayernMuller/vinyl/fork) and make your own list!")

group_info = group_by[group_name]
sort_by = group_info.get('sort_by')

table = {}
for record in record_list:
    if search and search.lower() not in str(record).lower():
        continue

    group = record.get(group_name, 'N/A')
    if group not in table:
        table[group] = []
    table[group].append(record)
    table[group] = sorted(table[group], key=lambda x: sort_func(x, sort_by))
    
table = dict(sorted(table.items(), key=lambda x: x[0], reverse=group_order == 'descending'))

if len(table) == 0:
    if search and len(search) > 0:
        st.error(f'No records found for "{search}"')
    else:
        st.info('No records found')
    st.stop()



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

if search:
    summary.markdown(f'Found {sum([len(records) for records in table.values()])} records for "{search}"')
else:
    summary.markdown(f'Totally {"".join([f"{count[format]} {format}s, " for format in count])[:-2]}')

