import pandas as pd
numeraciones = pd.read_csv(
    'CALLEJERO_VIGENTE_NUMERACIONES_202209.csv', sep=';', encoding='latin-1')
trameros = pd.read_csv(
    'CALLEJERO_VIGENTE_TRAMERO_202209.csv', sep=';', encoding='latin-1')
cruces = pd.read_csv('CALLEJERO_VIGENTE_CRUCES_202209.csv',
                     sep=';', encoding='latin-1')
viales = pd.read_csv('CALLEJERO_VIGENTE_VIALES_202209.csv',
                     sep=';', encoding='latin-1')
