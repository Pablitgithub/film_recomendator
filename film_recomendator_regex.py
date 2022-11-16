import re
import pandas as pd
import numpy as np

df = pd.read_csv('imdb_top_1000.csv', sep=',')


def extract():
    df = pd.read_csv('imdb_top_1000.csv', sep=',')
    return df


def transform(df):
    entrada = input('Qué género te gustaría ver ')
    
    # Crea una nueva columna en las que pondrá  solamentelos géneros que coincidan con la entrada
    df['genre_contains'] = df['Genre'].apply(lambda x: re.findall(entrada, x))  
    
    # Coge en las que encuentre el género en la nueva columna que serán solo aquellas que contengan el género
    data = df[df['genre_contains'].str.len() > 0]
    data = data['Series_Title'].sample()

    return data


def load(data):
    print(data)


if __name__ == '__main__':
    data = extract()
    data = transform(data)
    print('La película que te recomendamos es: ', data)
