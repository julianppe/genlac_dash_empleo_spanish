import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

external_stylesheets = [dbc.themes.JOURNAL]

app = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server

GENLAC_LOGO = "/assets/genlac.png"

dropdown = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Empleo y calificación", header=True),
            dbc.DropdownMenuItem("Tasa de participación laboral", href="/"),
            dbc.DropdownMenuItem("Tasa de empleo", href="/tasa-de-empleo"),
            dbc.DropdownMenuItem("Tasa de desempleo", href="/tasa-de-desempleo"),
            dbc.DropdownMenuItem("Tasa de informalidad laboral", href="/tasa-de-informalidad-laboral"),
            dbc.DropdownMenuItem("Horas semanales en trabajo remunerado", href="/horas-de-trabajo"),
            dbc.DropdownMenuItem("Empleadores", href="/empleador"),
            dbc.DropdownMenuItem("Asalariados", href="/asalariados"),
            dbc.DropdownMenuItem("Cuentapropista", href="/cuentapropista"),
            dbc.DropdownMenuItem("No remunerado", href="/no-remunerado"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Ingresos", header=True),
            dbc.DropdownMenuItem("Salario horario promedio", href="/salario-horario"),
            dbc.DropdownMenuItem("Ingreso laboral mensual", href="/ingreso-laboral"),
            dbc.DropdownMenuItem("Brecha salarial por género condicionada", href="/brecha-salarial-genero"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Calificación de la población adulta", header=True),
            dbc.DropdownMenuItem("Años de educación", href="/anios-educacion"),
            dbc.DropdownMenuItem("Porcentaje de adultos con calificación alta", href="/adultos-con-alta-calificacion"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicadores",
        className="ms-0",
        toggle_style={"color": "#460074"},
        align_end=False,
        style={'width':'100%'}

        )
    )
],
className="g-0 ms-auto flex-nowrap mt-5 mt-md-0",
align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            dropdown, 
                            className="ml-auto",
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
)
# Definimos el layout:
app.layout = html.Div(
    [
        dcc.Store(id="store", data='Argentina'),
        dbc.Container([
    dbc.Row(
        [
            navbar # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)


if __name__ == "__main__":
    app.run_server()