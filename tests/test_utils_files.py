# the test_table_utils module.

from unittest.mock import Mock, patch

import pandas as pd

from src.utils_files import read_csv, read_excel


@patch("csv.DictReader")
def test_read_csv(mock_csv: Mock) -> None:
    """Тест нормальной работы функции"""

    csv_data = [{"id": "111", "state": "EXECUTED", "date": "2024-12-15",
                 "amount": "111", "currency_name": "Ruble", "currency_code": "RUB",
                 "description": "test", "from": "Master Card", "to": "Visa"}]
    data = [{"id": 111, "state": "EXECUTED", "date": "2024-12-15",
             "operationAmount": {"amount": "111", "currency": {"name": "Ruble", "code": "RUB"}},
             "description": "test", "from": "Master Card", "to": "Visa"}]
    mock_csv.return_value = csv_data
    assert read_csv("data/transactions.csv") == data


def test_not_exist_csv() -> None:
    """Тест при отсутствии файла"""

    assert read_csv("data/none.csv") == []


@patch("csv.DictReader")
def test_invalid_csv(mock_csv: Mock) -> None:
    """Тест на отсутствие данных"""

    mock_csv.return_value = [{"ids": 111}]
    assert read_csv("data/transactions.csv") == []


@patch("pandas.read_excel")
def test_read_excel(mock_excel: Mock) -> None:
    """Тест нормальной работы функции"""

    excel_data = pd.DataFrame({"id": [111.0], "state": ["EXECUTED"], "date": ["2024-12-15"],
                               "amount": [111.0], "currency_name": ["Ruble"], "currency_code": ["RUB"],
                               "description": ["test"], "from": ["Master Card"], "to": ["Visa"]})
    data = [{"id": 111, "state": "EXECUTED", "date": "2024-12-15",
             "operationAmount": {"amount": "111.0", "currency": {"name": "Ruble", "code": "RUB"}},
             "description": "test", "from": "Master Card", "to": "Visa"}]
    mock_excel.return_value = excel_data
    assert read_excel("data/transactions_excel.xlsx") == data


def test_not_exist_excel() -> None:
    """Тест при отсутствии файла"""

    assert read_excel("data/none.xlsx") == []


@patch("pandas.read_excel")
def test_invalid_excel(mock_csv: Mock) -> None:
    """Тест на отсутствие данных"""

    mock_csv.return_value = pd.DataFrame({"ids": [111.0]})
    assert read_excel("data/transactions_excel.xlsx") == []