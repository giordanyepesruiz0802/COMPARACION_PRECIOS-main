import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash, dcc, Input, Output, callback
import pandas as pd 
from frontend.layout import layout
from backend.valores import max_values

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout

@app.callback(
    Output('valor-menor-container', 'children'),
    [Input('tabla_valor_1', 'data'),
     Input('tabla_valor_2', 'data')]
)
def update_valor_menor(data_valor_1, data_valor_2):
    valor_1_df = pd.DataFrame(data_valor_1)
    valor_2_df = pd.DataFrame(data_valor_2)
    
    # Convertir las columnas a tipo numérico
    valor_1_df['PRECIO_UNITARIO_1'] = pd.to_numeric(valor_1_df['PRECIO_UNITARIO_1'], errors='coerce')
    valor_2_df['PRECIO_UNITARIO_2'] = pd.to_numeric(valor_2_df['PRECIO_UNITARIO_2'], errors='coerce')
    
    max_values['VALOR_MENOR'] = [min(v1, v2) for v1, v2 in zip(valor_1_df['PRECIO_UNITARIO_1'], valor_2_df['PRECIO_UNITARIO_2'])]
    
    return None

@app.callback(
    Output('VALOR_MENOR', 'data'),
    [Input('valor-menor-container', 'children')]
)
def update_comparison_table(_):
    return max_values.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)