import requests
import pandas as pd
from pandas import json_normalize
from datetime import datetime
import time
import unittest


# API request config for SSI API endpoints
headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'X-Fiin-Key': 'KEY',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Fiin-User-ID': 'ID',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'X-Fiin-Seed': 'SEED',
        'sec-ch-ua-platform': 'Windows',
        'Origin': 'https://iboard.ssi.com.vn',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://iboard.ssi.com.vn/',
        'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7'
        }

def get_ticker_overview(symbol):
    """
    This function returns an overview of the given stock symbol.
    
    Args:
        symbol (str): 3 digits name of the desired stock.
    
    Returns:
        pandas.DataFrame: A DataFrame containing the stock overview data.
        
    Raises:
        ValueError: Raised whenever the symbol argument is not a string with a length of 3.
        ValueError: Raised whenever the API response is not successful.
    """
    if not isinstance(symbol, str) or len(symbol) != 3:
        raise ValueError("Invalid symbol argument")
    
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{symbol}/overview"
    response = requests.get(url)
    
    response.raise_for_status()  # Raise an exception for non-200 status codes
    
    data = response.json()
    df = json_normalize(data)
    return df


def get_stock_historical_data(symbol, start_date, end_date):
    """
    This function returns the stock historical daily data for the given symbol, within the specified date range.
    
    Args:
        symbol (str): 3 digits name of the desired stock.
        start_date (str): the start date to get data (YYYY-mm-dd).
        end_date (str): the end date to get data (YYYY-mm-dd).
    
    Returns:
        pandas.DataFrame: A DataFrame containing the stock historical data for the given symbol.
        
    Raises:
        ValueError: Raised whenever the symbol argument is not a string with a length of 3.
        ValueError: Raised whenever the start_date or end_date argument is not a string with a valid date format (YYYY-mm-dd).
        ValueError: Raised whenever the API response is not successful.
    """
    try:
        fd = int(time.mktime(time.strptime(start_date, "%Y-%m-%d")))
        td = int(time.mktime(time.strptime(end_date, "%Y-%m-%d")))
    except ValueError:
        raise ValueError("Invalid date format")

    if not isinstance(symbol, str) or len(symbol) != 3:
        raise ValueError("Invalid symbol argument")
    
    url = f"https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/bars-long-term?ticker={symbol}&type=stock&resolution=D&from={fd}&to={td}"
    response = requests.get(url)

    response.raise_for_status()  # Raise an exception for non-200 status codes
    
    data = response.json()['data']
    df = json_normalize(data)
    df['tradingDate'] = pd.to_datetime(df.tradingDate.str.split("T", expand=True)[0])
    df.columns = df.columns.str.title()
    df.rename(columns={'Tradingdate':'TradingDate'}, inplace=True)
    return df

def stock_intraday_data(symbol: str, page_num: int, page_size: int) -> pd.DataFrame:
    """
    This function returns the stock intraday data for the given symbol, with the specified page number and size.

    Args:
        symbol (str): 3 digits name of the desired stock.
        page_size (int): the number of rows in a page to be returned by this query, suggested to use 5000.
        page_num (int): the page index starting from 0.

    Returns:
        pandas.DataFrame: A DataFrame containing the stock intraday data for the given symbol.

    Raises:
        ValueError: Raised whenever the symbol argument is not a string with a length of 3.
        ValueError: Raised whenever the page_num or page_size argument is not a positive integer.
    """
    if not isinstance(symbol, str) or len(symbol) != 3:
        raise ValueError("The symbol argument must be a string with a length of 3")

    if not isinstance(page_num, int) or not isinstance(page_size, int) or page_num < 0 or page_size <= 0:
        raise ValueError("The page_num and page_size arguments must be positive integers")

    # Determine if today is a weekday or weekend
    today = datetime.today()
    if today.weekday() > 4:  # Weekend
        url = f"https://apipubaws.tcbs.com.vn/stock-insight/v1/intraday/{symbol}/his/paging?page={page_num}&size={page_size}&headIndex=-1"
    else:  # Weekday
        url = f"https://apipubaws.tcbs.com.vn/stock-insight/v1/intraday/{symbol}/his/paging?page={page_num}&size={page_size}"

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Invalid API response")

    data = response.json()['data']
    df = json_normalize(data).rename(columns={'p': 'price', 'v': 'volume', 't': 'time'})
    return df

def get_latest_indices(headers=headers):
    """
    Retrieve the latest indices values
    """
    url = "https://fiin-market.ssi.com.vn/MarketInDepth/GetLatestIndices?language=vi&pageSize=999999&status=1"
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json_normalize(response.json()['items'])
    
    # Update column names to match response
    result = result.rename(columns={'indexId': 'Index', 'indexValue': 'Price', 'percentIndexChange': 'Percentage Change', 'indexChange': 'Change'})
    result = result[['Index', 'Price', 'Percentage Change', 'Change']]
    
    return result


def generate_weeks_data(symbol, start_date, end_date):
    """
    This function returns a weekly summary of the stock data for the given symbol, within the specified date range.
    
    Args:
        symbol (str): 3 digits name of the desired stock.
        start_date (str): the start date to get data (YYYY-mm-dd).
        end_date (str): the end date to get data (YYYY-mm-dd).
    
    Returns:
        tuple: Two DataFrames containing the weekly and yearly stock data for the given symbol.
    """
    # Get daily data for the full date range
    daily_data = get_stock_historical_data(symbol, start_date, end_date)

    # Create a DataFrame with weekly summary data
    weekly_data = pd.DataFrame({
        'Open': daily_data.groupby(pd.Grouper(key='TradingDate', freq='W-MON'))['Open'].first(),
        'High': daily_data.groupby(pd.Grouper(key='TradingDate', freq='W-MON'))['High'].max(),
        'Low': daily_data.groupby(pd.Grouper(key='TradingDate', freq='W-MON'))['Low'].min(),
        'Close': daily_data.groupby(pd.Grouper(key='TradingDate', freq='W-MON'))['Close'].last(),
        'Volume': daily_data.groupby(pd.Grouper(key='TradingDate', freq='W-MON'))['Volume'].sum()
    })
    
    # Create a DataFrame with yearly summary data
    yearly_data = pd.DataFrame({
        'Open': daily_data.groupby(pd.Grouper(key='TradingDate', freq='Y'))['Open'].first(),
        'High': daily_data.groupby(pd.Grouper(key='TradingDate', freq='Y'))['High'].max(),
        'Low': daily_data.groupby(pd.Grouper(key='TradingDate', freq='Y'))['Low'].min(),
        'Close': daily_data.groupby(pd.Grouper(key='TradingDate', freq='Y'))['Close'].last(),
        'Volume': daily_data.groupby(pd.Grouper(key='TradingDate', freq='Y'))['Volume'].sum()
    })

    return weekly_data, yearly_data





class TestFunctions(unittest.TestCase):
    
    def test_get_ticker_overview(self):
        result = get_ticker_overview("VCB")
        self.assertIsNotNone(result)
        
    def test_get_stock_historical_data(self):
        result = get_stock_historical_data("VCB", "2022-01-01", "2022-01-31")
        self.assertIsNotNone(result)
        
    def test_get_stock_intraday_data(self):
        result = stock_intraday_data("VCB", 0, 5000)
        self.assertIsNotNone(result)
        
    def test_get_latest_indices(self):
        result = get_latest_indices()
        self.assertIsNotNone(result)
        
    def test_generate_weeks_data(self):
        start_date = '2022-01-01'
        end_date = '2022-01-31'
        symbol = 'VCB'

        # generate the weekly and yearly data
        weekly_data, yearly_data = generate_weeks_data(symbol, start_date, end_date)

        # check if weekly data is not None and is a pandas DataFrame
        self.assertIsNotNone(weekly_data)
        self.assertIsInstance(weekly_data, pd.DataFrame)

        # check if yearly data is not None and is a pandas DataFrame
        self.assertIsNotNone(yearly_data)
        self.assertIsInstance(yearly_data, pd.DataFrame)

        # check if weekly data has 5 columns
        self.assertEqual(len(weekly_data.columns), 5)

        # check if yearly data has 5 columns
        self.assertEqual(len(yearly_data.columns), 5)

        # check if weekly data is grouped by week
        weekly_groups = weekly_data.groupby(pd.Grouper(freq='W-MON')).size()
        self.assertGreater(len(weekly_groups), 0)

        # check if yearly data is grouped by year
        yearly_groups = yearly_data.groupby(pd.Grouper(freq='Y')).size()
        self.assertGreater(len(yearly_groups), 0)

unittest.main()