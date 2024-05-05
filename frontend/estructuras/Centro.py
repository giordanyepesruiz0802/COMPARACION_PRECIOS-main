import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import max_values

centro_l= dbc.Container([
   html.H6("VALOR UNITARIO COMPARADO", className='mb-4 text-center'),
    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                id='tabla_granulometria',
                columns=[
                    {'name': 'Valor Menor', 'id': 'VALOR_MENOR', 'editable': False},  # Modificar el texto del encabezado
                ],
                data=max_values.to_dict('records'),
                style_table={'overflowX': 'auto'}
            ),
            md=12
        )
    ], className='shadow p-3 border rounded')
], className='bg-light py-4')