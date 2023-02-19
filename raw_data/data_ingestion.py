import requests
import csv
from datetime import datetime
from collections import defaultdict
import pandas as pd

def get_daily_articles(stock_list):
    """
    This function get_daily_articles takes in a list of stock names as its argument stock_list. 
    It uses the News API (url) to fetch articles related to the stocks in stock_list. For each stock name in the stock_list, it sends a request to the News API with the stock name as a query parameter.
    The response from the API is in JSON format, which is converted into a Python dictionary data. The articles from the response are grouped into a default dictionary daily_articles, where the key is the date of publication and the value is a list of articles published on that day.
    The daily_articles dictionary is then converted into a list of dictionaries daily_articles_list, where each element of the list is a dictionary with two keys: 'date' and 'articles'.
    Finally, the information is written to a CSV file daily_articles.csv with the following columns: 'date', 'title', 'description', and 'stock_group', where 'stock_group' is the stock name in uppercase. The writing to the file is done in the append mode ('a') so that the information for multiple stocks can be written to the same file without overwriting the previous information.    
    """
    
    url = 'https://newsapi.org/v2/everything?'
    api_key = "023de80d70c24555968bfa08759afad9"
  
    for stock_name in stock_list:
        parameters = {
            
            'q': f'VN-{stock_name}',
            'sortBy': 'relevancy',
            'apiKey': api_key
        }

  
        response = requests.get(url, params=parameters)
  
        data = response.json()
  
        articles = data['articles']
  
        # Group articles by day
        daily_articles = defaultdict(list)
        for article in articles:
            date = datetime.strptime(article['publishedAt'][:10], '%Y-%m-%d').date()
            daily_articles[date].append(article)
  
        # Convert the daily_articles dictionary to a list of dictionaries
        daily_articles_list = [{'date': date, 'articles': articles} for date, articles in daily_articles.items()]
  
        with open('daily_articles.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'title', 'description','stock_group'])
            for day in daily_articles_list:
                date = day['date']
                for article in day['articles']:
                    writer.writerow({
                        'date': str(date),
                        'title': article['title'],
                        'description': article['description'],
                        'stock_group': stock_name.upper()
                    })

# Read the text file into a list
with open('top_stock.txt') as f:
    stocks = f.readlines()

# Clean up the list and extract the name and stock code
stocks = [stock.strip().split(' (') for stock in stocks]
stocks = [(name, stock.replace(')', '')) for name, stock in stocks]

# Create the dataframe
df = pd.DataFrame(stocks, columns=['name', 'stock'])

# Get the list of stock codes
stock_list = df['stock'].tolist()

# Call the function
get_daily_articles(stock_list)

# Show a timestamp to indicate when the code was run
print(f"Code was run at: {datetime.now()}")


