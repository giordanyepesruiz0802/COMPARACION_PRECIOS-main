import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash, dcc, Input, Output
import pandas as pd 
from frontend.layout import layout
from backend.valores import max_values, item_1, item_2, valor_1, valor_2
from difflib import get_close_matches
import dash_table



# Leer el archivo CSV
data_csv = pd.read_csv('backend/Lista_oficial_de_precios_unitarios_fijos_de_Obra_P_blica_y_de_consultor_a_-_DEPARTAMENTO_DE_BOYAC__20240505.csv')

# Crear diccionarios de mapeo entre ITEM y VALOR
map_valor_1 = dict(zip(item_1['ITEM_1'], valor_1['PRECIO_UNITARIO_1']))
map_valor_2 = dict(zip(item_2['ITEM_2'], valor_2['PRECIO_UNITARIO_2']))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)



nueva_tabla = html.Div([
    html.H6("Nombres Similares y sus Valores Correspondientes", className='mb-4 text-center'),
    dash_table.DataTable(
        id='tabla_similares',
        columns=[
            {'name': 'ITEM', 'id': 'ITEM'},
            {'name': 'TOTAL', 'id': 'TOTAL'},
            {'name': 'VALOR MENOR', 'id': 'VALOR_MENOR'}
        ],
        style_table={'overflowX': 'auto'}
    )
])

# Añade la nueva tabla al layout
app.layout = layout + nueva_tabla

# Callback para actualizar la nueva tabla
@app.callback(
    Output('tabla_similares', 'data'),
    [Input('valor-menor-container', 'children')]
)
def update_similares_table(_):
    # Obtener el valor menor comparado
    valor_menor = max_values['VALOR_MENOR'].min()
    
    # Determinar si el valor menor corresponde a item 1 o item 2
    if valor_menor in valor_1['PRECIO_UNITARIO_1'].values:
        item_df = item_1
        valor_key = 'PRECIO_UNITARIO_1'
    else:
        item_df = item_2
        valor_key = 'PRECIO_UNITARIO_2'
    
    # Obtener las palabras a buscar en la columna "ITEM"
    edited_items = item_df[item_df[valor_key] == valor_menor]['ITEM_1' if item_df is item_1 else 'ITEM_2'].tolist()
    
    # Filtrar los datos del CSV por palabras similares al valor menor
    similar_items = []
    for edited_item in edited_items:
        similar_items.extend(get_close_matches(edited_item, data_csv['ITEM'], n=1, cutoff=0.8))
    
    # Filtrar los datos del CSV según las palabras similares
    filtered_data = data_csv[data_csv['ITEM'].isin(similar_items)]
    
    # Obtener los valores de la columna "TOTAL"
    valores_menor = filtered_data['TOTAL'].tolist()
    
    # Crear diccionario para la nueva tabla
    similar_data = [{'ITEM': item, 'TOTAL': total, 'VALOR_MENOR': valor_menor} for item, total in zip(similar_items, valores_menor)]
    
    return similar_data
#Con esto, la nueva tabla tabla_similares se actualizará cada vez que cambie el valor en valor-menor-container, mostrando los nombres similares encontrados en la columna "ITEM", su correspondiente valor de la columna "TOTAL", y el valor menor de la tabla VALOR_MENOR. Asegúrate de ajustar el diseño y la posición de la nueva tabla según sea necesario en tu aplicación.






Message ChatGPT

ChatGPT can make mistakes. Consider checking important information.
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
