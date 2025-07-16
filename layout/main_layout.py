
from trame.widgets import vuetify
from layout.table_layout import table_viewer, left_panel

def build_layout(state, ctrl):
    
    with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
        with vuetify.VRow(style="height: 100%;"):
            with vuetify.VCol(cols=4, classes="pa-0"):
                left_panel(state, ctrl)    
            
            # Правая панель - таблица
            table_viewer(state, ctrl)
                    