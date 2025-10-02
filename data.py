"""This is for all the code used to interact with the AlphaVantage API
and the SQLite database. Remember that the API relies on a key that is
stored in your `.env` file and imported via the `config` module.
"""

import sqlite3
import pandas as pd
import requests
from config import settings


class AlphaVantageAPI:
    def __init__(self, api_key=settings.alpha_api_key):
        self.__api_key = api_key

    def get_daily(self, ticker, output_size="full"):
        """Get daily time series of an equity from AlphaVantage API."""
        
        # Create URL
        url = (
            "https://www.alphavantage.co/query?"
            "function=TIME_SERIES_DAILY&"
            f"symbol={ticker}&"
            f"outputsize={output_size}&"
            f"apikey={self.__api_key}"
        )

        # Send request to API
        response = requests.get(url)

        # Check if request was successful (status code 200 = OK)
        if response.status_code != 200:
            raise ConnectionError(f"API request failed with status code {response.status_code}")

        # Parse JSON response
        response_data = response.json()

        # Check if expected data exists in response
        if "Time Series (Daily)" not in response_data:
            raise ValueError(f"Unexpected API response: {response_data}")

        # Extract the actual time series data
        stock_data = response_data["Time Series (Daily)"]

        # Load data into DataFrame
        df = pd.DataFrame.from_dict(stock_data, orient="index", dtype=float)

        # Convert index (which is string dates) to pandas datetime
        df.index = pd.to_datetime(df.index)
        df.index.name = "date"

        # Clean up column names
        df.columns = [c.split(" ")[1] for c in df.columns]

        # Return final DataFrame
        return df


class SQLRepository:
    def __init__(self,connection):
        self.connection=connection

    def insert_table(self, table_name, 
                     records: pd.DataFrame, if_exists="fail"):
        n_inserted = records.to_sql(name=table_name, 
                                        con=self.connection, if_exists=if_exists)
            
        return {
            "transaction_successful": True, 
            "records_inserted": n_inserted}

    def read_table(self,table_name,limit):
        """Read table from database.
    
        Parameters
        ----------
        table_name : str
            Name of table in SQLite database.
        limit : int, None, optional
            Number of most recent records to retrieve. If `None`, all
            records are retrieved. By default, `None`.
    
        Returns
        -------
        pd.DataFrame
            Index is DatetimeIndex "date". Columns are 'open', 'high',
            'low', 'close', and 'volume'. All columns are numeric.
        """
        # Create SQL query (with optional limit)
        if limit:
              sql=f"SELECT * FROM '{table_name}' Limit {limit}"
        else:
              sql=f"SELECT * FROM '{table_name}'"
            
    
        # Retrieve data, read into DataFrame
        df = pd.read_sql(
            sql=sql, con=self.connection, parse_dates=["date"], 
            index_col="date"
        )
    
        # Return DataFrame
        return df


