import yfinance as yf

import pandas as pd

msft = yf.Ticker("MSFT")

msft.actions
# show dividends
msft.dividends
# show splits
msft.splits

# get all stock info
print(msft.info)

# get historical market data
hist = msft.history(period="5y", interval="1d")
hist

# show meta information about the history (requires history() to be called first)
msft.history_metadata

# show actions (dividends, splits, capital gains)
msft.actions
msft.dividends
msft.splits
msft.capital_gains  # only for mutual funds & etfs

# show share count
msft.get_shares_full(start="2018-01-01", end=None)

# show financials:
# - income statement
print(msft.quarterly_income_stmt)
msft.quarterly_income_stmt
# - balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet
# - cash flow statement
msft.cashflow
msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
msft.major_holders
msft.institutional_holders
msft.mutualfund_holders

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
msft.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# show news
msft.news

# get option chain for specific expiration
opt = msft.option_chain('2023-12-01')
# data available via: opt.calls, opt.puts
data = yf.download("AAPL", period="3mo")
df = pd.DataFrame(data)
df.columns


#1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo