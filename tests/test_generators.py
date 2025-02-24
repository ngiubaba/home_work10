import pytest

from src.generators import InvalidValue, card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[dict]) -> None:
    """Тест функции при нормальной работе"""
    transactions_by_USD = filter_by_currency(transactions, "USD")
    for transaction in transactions_by_USD:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_no_dict_filter() -> None:
    """Тест функции на ввод пустых данных"""
    with pytest.raises(InvalidValue):
        filter_by_currency([], "USD")


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """Тест функции на нормальное функционирование"""
    transaction_decription = transaction_descriptions(transactions)
    transfer_org = "Перевод организации"
    transfer_account = "Перевод со счета на счет"
    transfer_card = "Перевод с карты на карту"
    for transaction in transaction_decription:
        assert transaction == transfer_card or transfer_org or transfer_account


def test_no_dict_transaction_descriptions() -> None:
    """Тест на отсутствие входных данных"""
    # test = None
    with pytest.raises(InvalidValue):
        next(transaction_descriptions([]))


def test_card_number_generator() -> None:
    test_result = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    begin_number = "1"
    end_number = "3"
    result = card_number_generator(begin_number, end_number)
    assert list(result) == test_result
