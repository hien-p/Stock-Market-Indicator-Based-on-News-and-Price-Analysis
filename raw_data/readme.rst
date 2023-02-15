Function Descriptions
=============

``get_ticker_overview(symbol: str) -> pandas.DataFrame``

This function returns an overview of the given stock symbol.
* Args:
symbol (str): 3 digits name of the desired stock.

* Returns:
pandas.DataFrame: A DataFrame containing the stock overview data.

* Raises:
| ValueError: Raised whenever the symbol argument is not a string with a length of 3.
| ValueError: Raised whenever the API response is not successful.
::
|``get_stock_historical_data(symbol: str, start_date: str, end_date: str) -> pandas.DataFrame``

