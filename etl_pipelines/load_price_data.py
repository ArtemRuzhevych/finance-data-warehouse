import pandas as pd
import yfinance as yf
import sqlalchemy as db
import datetime as dt

def get_price_data(tickers, period = None):

    if period is None:
        end = dt.datetime.now()
        start = end - dt.timedelta(days=365)
    else:
        start, end = period

    data = yf.download(tickers, start=start, end=end)

    return data

def format_data(tickers, data):
    prices = []

    for ticker in tickers:
        ticker_data = pd.DataFrame({
            'TICKER': ticker,
            'DATE': data.index,
            'OPEN': data['Open'][ticker],
            'CLOSE': data['Close'][ticker],
            'HIGH': data['High'][ticker],
            'LOW': data['Low'][ticker],
        })
        prices.append(ticker_data)

    return pd.concat(prices)
