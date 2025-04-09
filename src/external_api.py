import os

import requests
from dotenv import load_dotenv


def convert_rub(from1: str, amount: float) -> float:
    load_dotenv()
    api_key = os.getenv("api_key")
    headers = {"apikey": f"{api_key}"}

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from1}&amount={amount}"
    responce = requests.request("GET", url, headers=headers)
    # print(responce.status_code)
    result = responce.json()["result"]
    return float(result)
