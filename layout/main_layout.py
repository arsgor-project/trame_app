from trame.ui.vuetify import SinglePageLayout
from trame.widgets import vuetify

def build_layout(server):
    state, ctrl = server.state, server.controller

    with SinglePageLayout(server) as layout:
        layout.title.set_text("Авиарасчеты")
        with layout.content:
            with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
                with vuetify.VRow(style="height: 100%;"):
                    with vuetify.VCol(cols=4, classes="pa-0"):
                        with vuetify.VCard(height="100%", classes="elevation-2 d-flex flex-column"):
                            with vuetify.VCardTitle("Шаг 1"):
                                vuetify.VFileInput(
                                    v_model=("selected_file",),
                                    label="Выберите файл",
                                    outlined=True,
                                    dense=True,
                                    hide_details=True,
                                    accept="*",
                                    multiple=False,
                                    change=("selected_file = $event",)
                                )
                                vuetify.VBtn(
                                    "Добавить файл",
                                    click=ctrl.on_add_file,
                                    color="primary",
                                    classes="ma-2"
                                )
                            vuetify.VDivider(classes="my-2")
                            with vuetify.VCardText(style="overflow-y: auto; flex-grow: 1;"):
                                vuetify.VTreeview(
                                    items=("files",),
                                    activatable=True,
                                    open_on_click=True,
                                    dense=True,
                                    return_object=True,
                                    item_key="id",
                                    item_text="name",
                                    item_children="children",
                                    v_model=("active_file", None),
                                    open_all=True,
                                    key=("files_key", len(state.files[0]['children'])),
                                    update_active=(ctrl.on_tree_select, "[$event]")
                                )
                    
                    # Правая панель - таблица
                    with vuetify.VCol(cols=8, classes="pa-0"):
                        with vuetify.VCard(height="100%", classes="elevation-2 d-flex flex-column"):
                            vuetify.VCardTitle("Просмотр содержимого")
                            with vuetify.VContainer(
                                v_if=("table_data && table_data.length > 0",),
                                style="height: calc(100% - 48px); overflow-y: auto; padding: 0;"
                            ):
                                vuetify.VDataTable(
                                    items=("table_data",),
                                    headers=("headers",),
                                    hide_default_footer=True,
                                    density="compact",
                                    height="100%"
                                )
