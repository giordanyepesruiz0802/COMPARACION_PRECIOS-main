import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import valor_1

Izquierda_2= dbc.Container([
    html.H5("PRECIO UNITARIO COTIZANTE 1", className='mb-4 text-center'),
    dash_table.DataTable(
        id='tabla_valor_1',
        columns=[
            {'name':'PRECIO_UNITARIO_1','id':'PRECIO_UNITARIO_1','editable':True},
        ],
        data= valor_1.to_dict('records'),
        style_table={'overflowX': 'auto'}
    ),
], className='shadow p-3 border rounded')

