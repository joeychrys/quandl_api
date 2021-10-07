from quandl import stock

ticker_list = ["AAPL"]

for tickers in ticker_list:
    stock(ticker=tickers).get_data(file_path="path/to/download")
