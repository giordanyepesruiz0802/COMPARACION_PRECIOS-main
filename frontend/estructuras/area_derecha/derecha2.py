import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback, dash_table

from backend.valores import item_2

Derecha_2= dbc.Container([
    html.H6("ITEM COTIZANTE 2", className='mb-4 text-center'),
    dash_table.DataTable(
        id='tabla_item_2',
        columns=[
            {'name':'ITEM_2','id':'ITEM_2','editable':True},
        ],
        data= item_2.to_dict('records'),
        style_table={'overflowX': 'auto'}
    ),
], className='shadow p-3 border rounded')
