import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import requests

symbol = 'AAPL'
start_date = '2015-01-01'
end_date = '2022-12-31'

data = yf.download(symbol, start=start_date, end=end_date)

data['SMA_50'] = data['Close'].rolling(window=50).mean()

data['Daily_Return'] = data['Close'].pct_change()

data['Strategy_Return'] = data['Daily_Return'] 

# * data['Signal'].shift(1)

data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

spy_data = yf.download('SPY', start=start_date, end=end_date)

spy_data['Daily_Return'] = spy_data['Close'].pct_change()

spy_data['Cumulative_Return'] = (1 + spy_data['Daily_Return']).cumprod()

plt.figure(figsize=(12, 6)) 
plt.plot(data.index, data['Cumulative_Return'], label='SMA Strategy') 
plt.plot(spy_data.index, spy_data['Cumulative_Return'], label='SPY') 
plt.xlabel('Date') 
plt.ylabel('Cumulative Returns') 
plt.legend() 
plt.show()

def implement_trading_strategy(data, short_window=50, long_window=200, stop_loss_percentage=0.05):
    # Calculate short-term and long-term moving averages
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Initialize positions
    position = None
    stop_loss_price = None
    trades = []

    # Implement trading strategy
    for index, row in data.iterrows():
        if row['Short_MA'] > row['Long_MA']:
            # Uptrend, generate buy signal
            if position is None:
                position = 'Buy'
                entry_price = row['Close']
                stop_loss_price = entry_price * (1 - stop_loss_percentage)
                trades.append(('Buy', index, entry_price))
        elif row['Close'] < stop_loss_price:
            # Sell signal due to stop loss
            if position == 'Buy':
                position = 'Sell'
                exit_price = stop_loss_price
                trades.append(('Sell', index, exit_price))
                position = None

    # Generate DataFrame for trades
    trade_df = pd.DataFrame(trades, columns=['Action', 'Date', 'Price'])
    trade_df.set_index('Date', inplace=True)
    return trade_df



