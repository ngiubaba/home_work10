import json
from typing import Any
from unittest.mock import mock_open, patch

import pytest

from src.utils import get_transaction_amount, transaction_dictionary


def test_transaction_dictionary_success() -> None:
    """Тест на успешное чтение данных"""
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_json = json.dumps(mock_data)

    with patch("os.path.exists", return_value=True), patch("builtins.open", mock_open(read_data=mock_json)):
        result = transaction_dictionary("operations.json")
        assert result == mock_data


def test_transaction_dictionary_file_not_found() -> None:
    """Тестирем что при отсутствующем файле, функция возвращает пустой список"""

    with patch("os.path.exists", return_value=False):
        result = transaction_dictionary("operations.json")
        assert result == []


def test_transaction_dictionary_empty_file() -> None:
    """Тест при пустом файле, функция вернет пустой список"""
    mock_json = ""

    with patch("os.path.exists", return_value=True), patch("builtins.open", mock_open(read_data=mock_json)):
        result = transaction_dictionary("operations.json")
        assert result == []


@pytest.mark.parametrize(
    "transaction, amount",
    [
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "9999.0", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            9999.0,
        )
    ],
)
def test_get_transaction_amount(transaction: dict[str, Any], amount: float) -> None:
    """testing getting transaction amount."""

    with patch("requests.request") as mock_convert:
        mock_convert.return_value.json.return_value = {"result": 9999.0}
        assert get_transaction_amount(transaction) == amount
