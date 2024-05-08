import dash_bootstrap_components as dbc
from dash import html

from .estructuras.derecha import Derecha
from .estructuras.izquierda import Izquierda
from .estructuras.Centro import centro_l
from .estructuras.abajo import tabla_resultados

layout = dbc.Container([
    dbc.Row([
        dbc.Col(Izquierda, md=4, style={'background-color': 'cadetblue'}),
        dbc.Col(centro_l, md=4, style={'background-color': 'lightcyan'}),
        dbc.Col(Derecha, md=4, style={'background-color': 'lightseagreen'}),
    ]),
    html.Div(id="valor-menor-container", style={"display": "none"}),
    #tabla_resultados
])
