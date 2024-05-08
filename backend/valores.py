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
