import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from .area_izquierda.izquierda1 import Izquierda_1
from .area_izquierda.izquierda2 import Izquierda_2

Izquierda= dbc.Container([
    dbc.Row([
        dbc.Col(Izquierda_1,md=6,style={'color':'khaki'}),
        dbc.Col(Izquierda_2,md=6,style={'color':'lightgray'}),

    ])

    
])