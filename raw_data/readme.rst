\# The above code defines 3 functions for fetching and returning
different stock data from an API.

Here\'s a quick documentation on how to use them: \##
get_ticker_overview(symbol) This function returns an overview of the
given stock symbol.

-   

    Arguments:

    :   -   symbol (str): 3 digits name of the desired stock.

-   

    Returns:

    :   -   pandas.DataFrame: A DataFrame containing the stock overview
            data.

-   

    Raises:

    :   -   ValueError: Raised whenever the symbol argument is not a
            string with a length of 3.
        -   ValueError: Raised whenever the API response is not
            successful.

Usage:
`` `python import requests import pandas as pd from pandas import json_normalize  symbol = "AAA" overview = get_ticker_overview(symbol) ``\`

\## get_stock_historical_data(symbol, start_date, end_date) This
function returns the stock historical daily data for the given symbol,
within the specified date range.

-   

    Arguments:

    :   -   symbol (str): 3 digits name of the desired stock.
        -   start_date (str): the start date to get data (YYYY-mm-dd).
        -   end_date (str): the end date to get data (YYYY-mm-dd).

-   

    Returns:

    :   -   pandas.DataFrame: A DataFrame containing the stock
            historical data for the given symbol.

-   

    Raises:

    :   -   ValueError: Raised whenever the symbol argument is not a
            string with a length of 3.
        -   ValueError: Raised whenever the start_date or end_date
            argument is not a string with a valid date format
            (YYYY-mm-dd).
        -   ValueError: Raised whenever the API response is not
            successful.

Usage:
`` `python import requests import pandas as pd from pandas import json_normalize  symbol = "AAA" start_date = "2022-01-01" end_date = "2022-01-31"  historical_data = get_stock_historical_data(symbol, start_date, end_date) ``\`
