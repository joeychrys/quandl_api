import json as j
import requests
import os

API_KEY = os.environ.get("QUANDL_API")

def get_data(database_code, dataset_code):

    # send get request to API
    api_endpoint = f"https://data.nasdaq.com/api/v3/datasets/{database_code}/{dataset_code}/data.json?api_key={API_KEY}"
    r = requests.get(api_endpoint)
    json = r.json()

    # save json response to json file
    try:
        json_file = open(f"stock_data/{dataset_code}.json", "x")
    except Exception:
        print(f"File already exists, overriding {dataset_code}.json")
        json_file = open(f"stock_data/{dataset_code}.json", "w")
        pass
    j.dump(json, json_file)
    json_file.close()

    return print("Finished")


def get_database_codes(file_name):

    # send get request to API
    api_endpoint = f"https://www.quandl.com/api/v3/databases?api_key={API_KEY}"
    r = requests.get(api_endpoint)
    json = r.json()

    # save json response to json file
    try:
        json_file = open(f"data_base_codes/{file_name}.json", "x")
    except Exception:
        print(f"{file_name} already exists, overriding {file_name}.json")
        json_file = open(f"data_base_codes/{file_name}.json", "w")
        pass
    j.dump(json, json_file)
    json_file.close()

    return print("Finished")


database_code = "WIKI"
dataset_code = "AAPL"

get_data(database_code=database_code, dataset_code=dataset_code)
get_database_codes(file_name="codes")
