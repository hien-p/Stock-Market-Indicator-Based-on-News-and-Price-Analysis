import pandas as pd

def read_from_csv(path='./full_vib.csv'):
    data = {}
    df = pd.read_csv(path)
    return {'date': df['Date'], 'open': df['Open'],\
            'closed': df['Closed'], 'high': df['Highest'],\
            'low': df['Lowest'], 'news': df['title'], 'label': df['pred']}


