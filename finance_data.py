import yfinance as yf


cple6 = yf.Ticker("CPLE6.SA")

# get stock info
cple6.info

# get historical market data
hist = cple6.history(period="max")

# show actions (dividends, splits)
cple6.actions

# show dividends
cple6.dividends

# show splits
cple6.splits


# Show function
for key, value in cple6.info.items():
    print(key, ":", value)
