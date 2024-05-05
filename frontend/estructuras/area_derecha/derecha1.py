import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import valor_2

Derecha_1= dbc.Container([
    html.H5("PRECIO UNITARIO COTIZANTE 2"),
    dash_table.DataTable(
        id='tabla_valor_2',
        columns=[
            {'name':'PRECIO_UNITARIO_2','id':'PRECIO_UNITARIO_2','editable':True},
        ],
    data= valor_2.to_dict('records'),
    style_table={'overflowX': 'auto'}
    
    )
        
    ]
)
