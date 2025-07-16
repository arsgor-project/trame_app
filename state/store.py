from logic.csv_loader import load_csv_content
from logic.file_tree import add_file_to_tree, handle_tree_selection

def setup_state_and_controllers(state, ctrl):
    state.files = [
        {
            'id': 'root',
            'name': 'Главная папка',
            'type': 'folder',
            'icon': 'mdi-folder',
            'children': [],
            'open': True
        }
    ]
    state.selected_file = None
    state.active_file = None
    state.table_data = []
    state.headers = []

    ctrl.on_add_file = lambda: add_file_to_tree(state)
    ctrl.on_tree_select = lambda items: handle_tree_selection(items, state)
