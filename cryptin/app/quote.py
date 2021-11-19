import warnings
warnings.filterwarnings('ignore')  # Hide warnings
import datetime as dt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.dates as mdates
import plotly.express as px

start = dt.datetime(2021, 1, 1)
end = dt.datetime(2021,5,29)
#We set the starting and ending dates of the data.

btc = web.DataReader("BTC-USD", 'yahoo', start, end)  # Collects data
btc.reset_index(inplace=True)

#bitcoin

crypto= btc[['Date','Adj Close']]
crypto= crypto.rename(columns = {'Adj Close':'BTC'})

crypto[ 'BTC_7DAY_MA' ] = crypto.BTC.rolling( 7).mean()

print(crypto.BTC.rolling( 7).mean())

#Ethereum

eth = web.DataReader("ETH-USD", 'yahoo', start, end)  # Collects data
eth.reset_index(inplace=True)
crypto["ETH"]= eth["Adj Close"]

# 7 day moving average
crypto[ 'ETH_7DAY_MA' ] = crypto.ETH.rolling( 7).mean()




#doge coin

doge = web.DataReader("DOGE-USD", 'yahoo', start, end)  # Collects data
doge.reset_index(inplace=True)
crypto["DOGE"]= doge["Adj Close"]

# 7 day moving average
crypto[ 'DOGE_7DAY_MA' ] = crypto.DOGE.rolling( 7).mean()