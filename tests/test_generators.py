import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, InvalidValue


def test_filter_by_currency(transactions: list[dict]) -> None:
    transactions_by_USD = filter_by_currency(transactions, "USD")
    for transaction in transactions_by_USD:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"
