import os
import json


file_name = "operations.json"
file_path = os.path.join("..", "data", file_name)
print(file_path)


def transaction_dictionary():
    dict_transaction = []

    if not os.path.exists(file_path):
        return dict_transaction
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            dict_transaction = json.load(f)
            if type(dict_transaction) is list:
                return dict_transaction
            else:
                return dict_transaction




if __name__ == "__main__" :
    print(transaction_dictionary())




