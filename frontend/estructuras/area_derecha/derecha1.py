import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import valor_2

Derecha_1= dbc.Container([
    html.H6("PRECIO UNITARIO COTIZANTE 2", className='mb-4 text-center'),
    dash_table.DataTable(
        id='tabla_valor_2',
        columns=[
            {'name': 'Precio Unitario 2', 'id': 'PRECIO_UNITARIO_2', 'editable': True},  # Modificar el texto del encabezado
        ],
        data=valor_2.to_dict('records'),
        style_table={'overflowX': 'auto'}
    ),
], className='shadow p-3 border rounded')
