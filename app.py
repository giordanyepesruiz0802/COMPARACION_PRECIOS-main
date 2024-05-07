import dash
import dash_bootstrap_components as dbc 
from dash import html, Dash, dcc, Input, Output
import pandas as pd 
from frontend.layout import layout
from difflib import get_close_matches
from backend.valores import max_values,item_1,item_2,valor_1,valor_2


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.layout = layout

data_csv = pd.read_csv('backend/Lista_oficial_de_precios_unitarios_fijos_de_Obra_P_blica_y_de_consultor_a_-_DEPARTAMENTO_DE_BOYAC__20240505.csv')

@app.callback(
    Output('valor-menor-container', 'children'),
    [Input('tabla_valor_1', 'data'),
     Input('tabla_valor_2', 'data')]
)
def update_valor_menor(data_valor_1, data_valor_2):
    if data_valor_1 and data_valor_2:
        valor_1_df = pd.DataFrame(data_valor_1)
        valor_2_df = pd.DataFrame(data_valor_2)

        valor_1_df['PRECIO_UNITARIO_1'] = valor_1_df['PRECIO_UNITARIO_1'].astype(float)
        valor_2_df['PRECIO_UNITARIO_2'] = valor_2_df['PRECIO_UNITARIO_2'].astype(float)

        min_valor_1 = valor_1_df['PRECIO_UNITARIO_1'].min()
        min_valor_2 = valor_2_df['PRECIO_UNITARIO_2'].min()

        if min_valor_1 < min_valor_2:
            return {'valor_1': min_valor_1, 'item': item_1}
        else:
            return {'valor_2': min_valor_2, 'item': item_2}
    else:
        return None

@app.callback(
    Output('tabla_item_comparado', 'data'),
    [Input('valor-menor-container', 'children')]
)
def update_item_comparison_table(data):
    if data:
        min_valor = data.get('valor_1') if 'valor_1' in data else data.get('valor_2')
        item_df = data.get('item')

        edited_items = item_df[item_df['PRECIO_UNITARIO_1' if 'valor_1' in data else 'PRECIO_UNITARIO_2'] == min_valor]['ITEM_1' if 'valor_1' in data else 'ITEM_2'].tolist()

        similar_items = []
        for edited_item in edited_items:
            similar_items.extend(get_close_matches(edited_item, data_csv['ITEM'], n=1, cutoff=0.8))

        filtered_data = data_csv[data_csv['ITEM'].isin(similar_items)]

        return filtered_data.to_dict('records')
    else:
        return []

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
    

