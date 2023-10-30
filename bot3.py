import pandas as pd

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