import os
import json

from src.external_api import convert_rub


def transaction_dictionary(file_name = "operations.json"):
    dict_transaction = []
    file_path = os.path.join("..", "data", file_name)
    if not os.path.exists(file_path):
        return dict_transaction
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            dict_transaction = json.load(f)
            if type(dict_transaction) is list:
                return dict_transaction
            else:
                return dict_transaction

# transaction_data = {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "10",
#       "currency": {
#         "name": "руб.",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   }
def get_transaction_amount(transaction_data):
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        return transaction_data["operationAmount"]["amount"]
    else:
        amount = transaction_data["operationAmount"]["amount"]
        from1 = transaction_data["operationAmount"]["currency"]["code"]
        result = convert_rub(from1, amount)
        return result

# if __name__ == "__main__" :
#     print(get_transaction_amount(transaction_data))




