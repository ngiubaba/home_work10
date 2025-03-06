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


@pytest.mark.parametrize(
    "begin_number, end_number, expected_result",
    [
        ("1", "3", ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        ("10", "12", ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        ("999", "1001", ["0000 0000 0000 0999", "0000 0000 0000 1000", "0000 0000 0000 1001"]),
    ]
)
def test_card_number_generator(begin_number: str, end_number: str, expected_result: list[str]) -> None:
    """
    Параметризованный тест для функции card_number_generator.
    """
    result = card_number_generator(begin_number, end_number)
    assert list(result) == expected_result
