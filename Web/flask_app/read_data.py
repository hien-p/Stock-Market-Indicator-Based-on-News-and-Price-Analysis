import pandas as pd

def read_from_csv(path='./full_vib.csv'):
    data = {}
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date', ascending=True, inplace=True)
    data= {'date': df['Date'], 'open': df['Open'],\
            'closed': df['Closed'], 'high': df['Highest'],\
            'low': df['Lowest'], 'news': df['title'], 'label': df['pred']}
    for key in data:
        data[key] = data[key].tolist()
    return data

def request_candle_chart_data(path='./full_vib.csv'):
    data = read_from_csv()
    results = []
    news = []
    for date, hg, op, cl, lw, title, label in zip(data['date'], data['high'],\
     data['open'], data['closed'], data['low'], data['news'], data['label']):
     results.append({'x': date, 'y': [hg, op, cl, lw]})
     news.append({'date': date, 'title': title, 'label': label})
    return {'prices': results, 'news': news}