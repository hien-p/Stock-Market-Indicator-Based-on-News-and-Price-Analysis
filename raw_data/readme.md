# The above code defines 3 functions for fetching and returning different stock data from an API.

Here's a quick documentation on how to use them:
## get_ticker_overview(symbol)
This function returns an overview of the given stock symbol.

* Arguments:
    * symbol (str): 3 digits name of the desired stock.
* Returns:
    *   pandas.DataFrame: A DataFrame containing the stock overview data.
* Raises:
    * ValueError: Raised whenever the symbol argument is not a string with a length of 3.
    * ValueError: Raised whenever the API response is not successful.

Usage:
```python
import requests
import pandas as pd
from pandas import json_normalize

symbol = "AAA"
overview = get_ticker_overview(symbol)
```

## get_stock_historical_data(symbol, start_date, end_date)
This function returns the stock historical daily data for the given symbol, within the specified date range.

* Arguments:
    * symbol (str): 3 digits name of the desired stock.
    * start_date (str): the start date to get data (YYYY-mm-dd).
    * end_date (str): the end date to get data (YYYY-mm-dd).
* Returns:
    *   pandas.DataFrame: A DataFrame containing the stock historical data for the given symbol.
* Raises:
    * ValueError: Raised whenever the symbol argument is not a string with a length of 3.
    * ValueError: Raised whenever the start_date or end_date argument is not a string with a valid date format (YYYY-mm-dd).
    * ValueError: Raised whenever the API response is not successful.

Usage:
```python
import requests
import pandas as pd
from pandas import json_normalize

symbol = "AAA"
start_date = "2022-01-01"
end_date = "2022-01-31"

historical_data = get_stock_historical_data(symbol, start_date, end_date)
```

## stock_intraday_data(symbol: str, page_num: int, page_size: int) -> pd.DataFrame
This function returns the stock intraday data for the given symbol, with the specified page number and size.

* Arguments:
    * symbol (str): 3 digits name of the desired stock.
    * page_size (int): the number of rows in a page to be returned by this query, suggested to use 5000.
    * page_num (int): the page index starting from 0.

* Returns:
    *   pandas.DataFrame: A DataFrame containing the stock intraday data for the given symbol.
* Raises:
    * ValueError: Raised whenever the symbol argument is not a string with a length of 3.
    * ValueError: Raised whenever the page_num or page_size argument is not a positive integer.

Usage:
```python
import requests
import pandas as pd
from pandas import json_normalize

symbol = "AAA"
page_num = 0
page_size = 5000

intraday_data = stock_intraday_data(symbol, page_num, page_size)
```

## generate_weeks_data()
Description:
This function takes a stock symbol, start date, and end date as input and returns two data frames containing weekly and yearly summary data of the stock. The weekly data frame includes the open, high, low, close, and volume of the stock for each week between the start and end dates. The yearly data frame includes the same values, but summarized for each year between the start and end dates.

* Syntax:
    * generate_weeks_data(symbol, start_date, end_date)

* Input Parameters:
    * symbol (str): A string that represents the stock symbol. It should be a three-digit name of the desired stock.
    * start_date (str): A string that represents the start date to get data. It should be in the format "YYYY-mm-dd".
    * end_date (str): A string that represents the end date to get data. It should be in the format "YYYY-mm-dd".
* Output
    * weekly_data (DataFrame): A data frame that contains weekly summary data of the stock for the given symbol and within the specified date range.
    * yearly_data (DataFrame): A data frame that contains yearly summary data of the stock for the given symbol and within the specified date range.
```
Weekly data: Open        High         Low       Close      Volume
TradingDate                                                            
2021-01-04   133.5200  133.610001  126.760002  129.410004  2606169000
2021-01-11   128.899994  132.630005  127.860001  132.050003  2142620100
2021-01-18   128.779999  139.070007  128.500000  139.070007  2283089600
```

