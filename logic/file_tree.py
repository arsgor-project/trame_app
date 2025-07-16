import uuid
from logic.csv_loader import load_csv_content

def add_file_to_tree(state):
    file_info = state.selected_file
    if not file_info:
        print("Файл не выбран")
        return

    if isinstance(file_info, list):
        file_info = file_info[0]
    
    if 'content' not in file_info:
        print("⚠️ Файл не содержит контента")
        return

    new_file = {
        'id': str(uuid.uuid4()),
        'name': file_info['name'],
        'type': 'file',
        'icon': 'mdi-file-document',
        'content': file_info['content'].decode('cp1251', errors='replace')
    }


    new_files = state.files.copy()
    root = {**new_files[0]}
    new_children = root['children'].copy()
    new_children.append(new_file)
    root['children'] = new_children
    new_files[0] = root
    state.files = new_files
    #state.files[0]['children'].append(new_file)
    state.files_key += 1
    state.selected_file = None
    #print(state.files[0]['children'])


def handle_tree_selection(items, state):
    if items:
        item = items[0]
        if item.get('type') == 'file':
            if item['name'].lower().endswith('.csv'):
                try:
                    data, headers = load_csv_content(item['content'])
                    state.table_data = data
                    state.headers = headers
                except Exception as e:
                    print(f"Ошибка загрузки CSV: {e}")
                    state.table_data = []
                    state.headers = []
            else:
                state.table_data = []
                state.headers = []
    else:
        state.active_file = None
        state.table_data = []
        state.headers = []
