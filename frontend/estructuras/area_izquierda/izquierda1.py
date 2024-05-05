import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import item_1

Izquierda_1= dbc.Container([
html.H5("ITEM COTIZANTE 1", className='mb-4 text-center'),
    dash_table.DataTable(
        id='tabla_item_1',
        columns=[
            {'name':'ITEM_1','id':'ITEM_1','editable':True},
        ],
        data= item_1.to_dict('records'),
        style_table={'overflowX': 'auto'}
    ),
], className='shadow p-3 border rounded')
