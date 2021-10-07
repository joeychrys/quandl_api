import json as j
import requests
import os


class stock():
    def __init__(self, ticker):
        self.API_KEY = os.environ.get("QUANDL_API")
        self.ticker = ticker

    def get_data(self, file_path):

        # send get request to API
        api_endpoint = f"https://data.nasdaq.com/api/v3/datasets/WIKI/{self.ticker}/data.json?api_key={self.API_KEY}"
        r = requests.get(api_endpoint)
        json = r.json()

        # save json response to json file
        try:
            json_file = open(f"{file_path}/{self.ticker}.json", "x")
        except Exception:
            print(f"File already exists, overriding {self.ticker}.json")
            json_file = open(f"{file_path}/{self.ticker}.json", "w")
            pass
        j.dump(json, json_file)
        json_file.close()

        return print(f"{self.ticker} downloaded to {file_path}/")