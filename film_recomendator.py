import re
import pandas as pd
import numpy as np

df = pd.read_csv('imdb_top_1000.csv', sep=',')


def extract():
    df = pd.read_csv('imdb_top_1000.csv', sep=',')
    return df


def transform(df):
    entrada = input('Qué género te gustaría ver ')
    data = df[df['Genre'].str.contains(entrada)]
    data = data['Series_Title'].sample()
    return data


def load(data):
    print(data)


if __name__ == '__main__':
    data = extract()
    data = transform(data)
    print('La película que te recomendamos es: ', data)
