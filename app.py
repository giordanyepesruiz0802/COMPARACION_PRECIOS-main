import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash, dcc, Input, Output, callback
import pandas as pd 
from frontend.layout import layout
from backend.valores import max_values,item_1,item_2,valor_1,valor_2

data_csv = pd.read_csv('backend/Lista_oficial_de_precios_unitarios_fijos_de_Obra_P_blica_y_de_consultor_a_-_DEPARTAMENTO_DE_BOYAC__20240505.csv')

# Crear un diccionario de mapeo entre ITEM y VALOR
map_valor_1 = dict(zip(item_1['ITEM_1'], valor_1['PRECIO_UNITARIO_1']))
map_valor_2 = dict(zip(item_2['ITEM_2'], valor_2['PRECIO_UNITARIO_2']))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.layout = layout

@app.callback(
    Output('valor-menor-container', 'children'),
    [Input('tabla_valor_1', 'data'),
     Input('tabla_valor_2', 'data')]
)
def update_valor_menor(data_valor_1, data_valor_2):
    valor_1_df = pd.DataFrame(data_valor_1)
    valor_2_df = pd.DataFrame(data_valor_2)
    
    # Convertir las columnas a tipo float
    valor_1_df['PRECIO_UNITARIO_1'] = valor_1_df['PRECIO_UNITARIO_1'].astype(float)
    valor_2_df['PRECIO_UNITARIO_2'] = valor_2_df['PRECIO_UNITARIO_2'].astype(float)
    
    # Calcular el valor menor
    max_values['VALOR_MENOR'] = [min(v1, v2) for v1, v2 in zip(valor_1_df['PRECIO_UNITARIO_1'], valor_2_df['PRECIO_UNITARIO_2'])]
    
    return None

@app.callback(
    Output('VALOR_MENOR', 'data'),
    [Input('valor-menor-container', 'children')]
)
def update_comparison_table(_):
    return max_values.to_dict('records')

@app.callback(
    Output('tabla_item_comparado', 'data'),
    [Input('valor-menor-container', 'children')]
)
def update_item_comparison_table(_):
    # Obtener el valor menor comparado en el centro_1
    valor_menor = max_values['VALOR_MENOR'].min()
    
    # Filtrar los datos del CSV por palabras similares al valor menor
    edited_items = max_values[max_values['VALOR_MENOR'] == valor_menor]['ITEM'].tolist()
    
    # Filtrar los datos de la base de datos según los valores de item_1 y item_2
    filtered_data_1 = data_csv[data_csv['ITEM'].str.contains('|'.join(edited_items), case=False)]
    
    return filtered_data_1.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
    

