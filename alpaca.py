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