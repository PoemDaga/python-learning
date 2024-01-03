import yfinance as yf
import pandas as pd

amd = yf.Ticker('TSLA')

# !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json

amd_data = amd.history(period="max")

amd_data.reset_index(inplace=True)
amd_data.head()

# inf = yf.ticker.Ticker('TSLA').info
# print(inf)
