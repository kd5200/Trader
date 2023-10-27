import alpaca_trade_api as tradeapi
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import requests
from keys import *


# Implementing my API keys from Alpaca
API_KEY = api_key
API_SECRET = api_secret
BASE_URL = endpoint

# Create an Alpaca API connection
api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version='v2')

# Get account information
account = api.get_account()
print(f"Account Status: {account.status}")
print(f"Buying Power: {account.buying_power}")