from trame.app import get_server
from layout.main_layout import build_layout
from state.store import setup_state_and_controllers
from trame.ui.vuetify import SinglePageLayout

server = get_server(client_type="vue2")
state, ctrl = server.state, server.controller

setup_state_and_controllers(state, ctrl)

with SinglePageLayout(server) as layout:
    layout.title.set_text("Авиарасчеты")
    with layout.content:
        build_layout(state, ctrl)

if __name__ == "__main__":
    server.start()