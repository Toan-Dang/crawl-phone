import pandas as pd

def read_csv():
    df = pd.read_csv('Products.csv')
    return df['url'].values.tolist()