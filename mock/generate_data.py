import requests
from random import choices, randint, choice
from typing import Dict
from model import Symbol

API_KEY = "HKLSF2H831ZMQKSQ"


def get_data(api, stock_symbol: str) -> Dict:
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api}"
    res = requests.get(url)
    return res.json()


def extract_json(api_key):
    symbol = choice(list(Symbol)).value
    data = get_data(api_key, symbol)["Time Series (Daily)"]
    rand_date = choices(list(data.keys()), k=randint(1, 8))

    return {key: data[key] for key in rand_date}


if __name__ == "__main__":
    try:
        print(extract_json(API_KEY))
    except KeyError:
        from time import sleep
        sleep(5)
        print(extract_json(API_KEY))

