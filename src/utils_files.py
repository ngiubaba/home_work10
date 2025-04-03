import csv
import os

import pandas as pd


def read_csv(filename: str) -> list:
    """
    Функция для чтения cvs файлов
    """

    transaction_data = list()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Корень проекта
    file_path = os.path.join(base_dir, filename)

    try:
        with open(file_path, encoding="utf-8") as csv_file:
            csv_data = csv.DictReader(csv_file, delimiter=";")
            for row in csv_data:
                if not row["id"].isdigit():
                    continue
                id = int(row["id"])
                state = row["state"]
                date = row["date"]
                amount = str(row["amount"])
                currency_name = row["currency_name"]
                currency_code = row["currency_code"]
                from_val = row["from"]
                to_val = row["to"]
                description = row["description"]
                transaction = {
                    "id": id,
                    "state": state,
                    "date": date,
                    "operationAmount": {
                        "amount": amount,
                        "currency": {
                            "name": currency_name,
                            "code": currency_code,
                        },
                    },
                    "description": description,
                    "from": from_val,
                    "to": to_val,
                }
                transaction_data.append(transaction)
    except FileNotFoundError as e:
        print(f"CSV file {filename} not found: {e}")
    except KeyError as e:
        print(f"field name in csv data {filename} not exists: {e}")
    except csv.Error as e:
        print(f"error parse {filename} csv data: {e}")

    return transaction_data


def read_excel(filename: str) -> list:
    """
    Функция для чтения xlxs файлов
    """

    transaction_data = list()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Корень проекта
    file_path = os.path.join(base_dir, filename)

    try:
        with open(file_path, "rb") as excel_file:
            excel_data = pd.read_excel(excel_file)
            excel_dict = excel_data.to_dict("records")
            for row in excel_dict:
                if row["id"] != row["id"]:
                    print(f"incorrect Excel data in {filename}: 'id' field must be numeric.")
                    continue
                id = int(row["id"])
                state = row["state"]
                date = row["date"]
                amount = str(row["amount"])
                currency_name = row["currency_name"]
                currency_code = row["currency_code"]
                from_val = row["from"]
                to_val = row["to"]
                description = row["description"]
                transaction = {
                    "id": id,
                    "state": state,
                    "date": date,
                    "operationAmount": {
                        "amount": amount,
                        "currency": {
                            "name": currency_name,
                            "code": currency_code,
                        },
                    },
                    "description": description,
                    "from": from_val,
                    "to": to_val,
                }
                transaction_data.append(transaction)
    except FileNotFoundError as e:
        print(f"Excel file {filename} not found: {e}")
    except KeyError as e:
        print(f"field name in Excel data {filename} not exists: {e}")
    except pd.errors.ParserError as e:
        print(f"error parse {filename} excel data: {e}")
    return transaction_data
