import pandas as pd

item1 = [
    "CONCRETO",
    "ACERO",
    "MADERA",
    "VINILO",
    "PINTURA",
    "CIELO RASO",
    "CERAMICA",
    "MORTERO",
    "CARPINTERIA",
    "BALDOSA",
    "MANO DE OBRA",
    "VIDRIOS"
]

item2 = [
    "CONCRETO",
    "ACERO",
    "MADERA",
    "VINILO",
    "PINTURA",
    "CIELO RASO",
    "CERAMICA",
    "MORTERO",
    "CARPINTERIA",
    "BALDOSA",
    "MANO DE OBRA",
    "VIDRIOS"
]

valor1 = [
    5000,
    3000,
    2500,
    3600,
    4800,
    20000,
    25000,
    8500,
    9200,
    7000,
    1000,
    800
]

valor2 = [
    10000,
    25000,
    11000,
    9500,
    4700,
    2000,
    8500,
    4250,
    2500,
    1500,
    750,
    250
]

item_1 = pd.DataFrame({
    "ITEM_1": item1
})

item_2 = pd.DataFrame({
    "ITEM_2": item2
})

valor_1 = pd.DataFrame({
    "PRECIO_UNITARIO_1": valor1
})

valor_2 = pd.DataFrame({
    "PRECIO_UNITARIO_2": valor2
})


max_values = pd.DataFrame({
    "VALOR_MENOR": [min(v1, v2) for v1, v2 in zip(valor1, valor2)]
})

#data = {
 #   'ITEM': ["CONCRETO", "GRANITO", "MADERA", "ACERO"],
 #   'VALOR_BASE': [40, 35, 30, 45]
#}
#base_datos = pd.DataFrame(data)

# Función para buscar el valor base según el item
#def buscar_valor_base(item):
 #   valor_base = base_datos[base_datos['ITEM'] == item]['VALOR_BASE'].values
  #  return valor_base[0] if len(valor_base) > 0 else None

# Agregar una columna con el valor base para item_1
#item_1['VALOR_BASE'] = item_1['ITEM_1'].apply(buscar_valor_base)

# Agregar una columna con el valor base para item_2
#item_2['VALOR_BASE'] = item_2['ITEM_2'].apply(buscar_valor_base)

# Crear tabla comparativa
#comparativa = pd.DataFrame({
 #   'ITEM_1': item_1['ITEM_1'],
  #  'ITEM_2': item_2['ITEM_2'],
  #  'VALOR_MENOR': item_1['VALOR_MENOR'],
  #  'VALOR_BASE_1': item_1['VALOR_BASE'],
  #  'VALOR_BASE_2': item_2['VALOR_BASE']
#})

#print(comparativa)
