import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table
import pandas as pd
from difflib import get_close_matches



tabla_resultados = dbc.Container([
    html.H6("Resultados de la Comparación", className='mb-4 text-center'),
    dash_table.DataTable(
        id='tabla_resultados',
        columns=[
            {'name': 'Item Similar', 'id': 'ITEM'},
            {'name': 'Valor Total', 'id': 'TOTAL'},
            {'name': 'Valor Menor', 'id': 'VALOR_MENOR'}
        ],
        style_table={'overflowX': 'auto'}
    ),
], className='shadow p-3 border rounded')
