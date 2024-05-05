import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback

from .area_derecha.derecha1 import Derecha_1
from .area_derecha.derecha2 import Derecha_2


Derecha= dbc.Container([
    dbc.Row([
        dbc.Col(Derecha_1,md=6,style={'color':'lightgray'}),
        dbc.Col(Derecha_2,md=6,style={'color':'khaki'})


    ])

    
])