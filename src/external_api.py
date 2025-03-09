import requests
import os
from dotenv import load_dotenv


def convert_rub(from1, amount):
    load_dotenv()
    api_key = os.getenv('api_key')
    headers = {
        "apikey": f"{api_key}"
        }
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from1}&amount={amount}"
    responce = requests.request("GET", url, headers=headers)
    # print(responce.status_code)
    result = responce.json()["result"]
    return result

# if __name__ == "__main__":
#     print(convert_rub("EUR", "1"))
