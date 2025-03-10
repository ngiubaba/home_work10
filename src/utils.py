import json
import os
from typing import Any, Union

from src.external_api import convert_rub


def transaction_dictionary(file_name: str = "operations.json") -> Union[list[dict], dict]:
    dict_transaction: list[dict[str, Any]] = []
    file_path = os.path.join("..", "data", file_name)
    if not os.path.exists(file_path):
        return dict_transaction
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []

            dict_transaction = json.loads(content)

            if type(dict_transaction) is list:
                return dict_transaction
            else:
                return []


# transaction_data = {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "10",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   }


def get_transaction_amount(transaction_data: dict[str, Any]) -> float:
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction_data["operationAmount"]["amount"])
    else:
        amount = transaction_data["operationAmount"]["amount"]
        from1 = transaction_data["operationAmount"]["currency"]["code"]
        result = convert_rub(from1, amount)
        return float(result)


# if __name__ == "__main__" :
#     print(transaction_dictionary())
