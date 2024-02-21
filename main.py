from utils.components import RecordGroup
from utils.streamlit_util import remove_streamlit_style
from models.record import Record
import streamlit as st

RECORDS_LIST_FILE = 'list.json'

class App:
    def __init__(self):
        self.data = None
        try:
            list_file = open(RECORDS_LIST_FILE, 'r')
            record_list = eval(list_file.read())
            self.data: list[Record] = [Record(**record) for record in record_list]
            list_file.close()
        except FileNotFoundError:
            st.error(f'File "{RECORDS_LIST_FILE}" not found')
            st.write('')
            st.write("Did you fork this template just now? If so, you need to upload your list file first.")
            st.code('''
            # Path: list.json
            [
                {
                    "cover": "<image_url>",
                    "artist": "<artist_name>",
                    "title": "<album_title>",
                    "genre": "<genre>",
                    "format": "<format>",
                    "country": "<country>",
                    "year": <year>
                },
                ...
            ]
            ''')
        except Exception:
            st.error(f'Wrong JSON format in "{RECORDS_LIST_FILE}". Please check the file and try again.')
        finally:
            if not isinstance(self.data, list):
                st.write("For more information, please check the [documentation](https://github.com/BayernMuller/vinyl/blob/main/README.md).")
                st.stop()
                

    @staticmethod
    def sort_func(x: Record, tag_list):
        return ''.join([str(getattr(x, tag, '')) for tag in tag_list])
    
    def run(self):
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
            with st.expander('filter', expanded=True):
                search = st.text_input('search', key='search')

            with st.expander('options', expanded=True):
                group_name = st.radio('group by', list(group_by.keys()), index=index_format, key='group_by')
                group_order = st.radio('order', ['ascending', 'descending'], index=0, key='order', horizontal=True, disabled=group_name == 'none')
            
            st.write("Developed by [@BayernMuller](https://github.com/bayernmuller)")
            st.write("Fork this template from [here](https://github.com/BayernMuller/vinyl/fork) and make your own list!")

        group_info = group_by[group_name]
        sort_by = group_info.get('sort_by')

        table = {}
        for record in self.data:
            if search and search.lower() not in str(record).lower():
                continue

            group = getattr(record, group_name, 'unknown')
            if group not in table:
                table[group] = []
            table[group].append(record)
            table[group] = sorted(table[group], key=lambda x: App.sort_func(x, sort_by))
            
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

            record_widget = RecordGroup()
            for record in records:
                record_widget.add_record(record)
                if record.format not in count:
                    count[record.format] = 0

                count[record.format] += 1

            record_widget.generate()

        if search:
            summary.markdown(f'Found {sum([len(records) for records in table.values()])} records for "{search}"')
        else:
            summary.markdown(f'Totally {"".join([f"{count[format]} {format}s, " for format in count])[:-2]}')

if __name__ == '__main__':
    st.set_page_config(page_title='Records', page_icon=':cd:', layout='wide')
    remove_streamlit_style()
    app = App()
    app.run()
