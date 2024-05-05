import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash,dcc,Input,Output,callback,dash_table

from backend.valores import max_values

centro_l= dbc.Container([
   html.H5("VALOR UNITARIO COMPARADO"),
   dash_table.DataTable(
      id='VALOR_MENOR',
      columns=[
          {'name':'PRECIO MENOR','id':'VALOR_MENOR','editable':False},
        ],
     data= max_values.to_dict('records'),
     style_table={'overflowX': 'auto'}
  )
])