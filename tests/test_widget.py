import pytest

from src.masks import InvalidCardNumberError, InvalidAccountNumberError
from src.widget import mask_account_card, get_date, InvalidNameCard


# Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
# Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.

@pytest.mark.parametrize(
    "account_card, mask",
    [
        ("Visa 4276310049981287", "Visa 4276 31** **** 1287"),
        ("Maestro 4621978532149576", "Maestro 4621 97** **** 9576"),
        ("Счет 64125795412389135479", "Счет **5479"),
        ("Visa Classic 6489123754961537", "Visa Classic 6489 12** **** 1537"),
        ("Visa Gold 6179531648915347", "Visa Gold 6179 53** **** 5347")
    ]
)
def test_mask_account_card(account_card, mask):
    """Тест для проверки маскировки номера карты или счета,
     при его корректном распознавании типа """
    assert mask_account_card(account_card) == mask


def test_nonstandart_account_card_name():
    """Тест функции при неправильном вводе названия карты/счета"""

    with pytest.raises(InvalidNameCard):
        mask_account_card("Oleg 4987164489953148")
        mask_account_card("615792440668159")
        mask_account_card()


def test_nonstandart_account_card_number():
    """Тест функции при неправильном кол-ве символов в номере карты"""

    with pytest.raises(InvalidCardNumberError):
        mask_account_card("Visa 427631004998")
        mask_account_card("Maestro 548743")
        mask_account_card("Mastercard 8")
        mask_account_card("Visa ")
        mask_account_card()


def test_nonstandart_account_number():
    """Тест функции при неправильном кол-ве символов в номере карты"""

    with pytest.raises(InvalidAccountNumberError):
        mask_account_card("Счет 427631004998")
        mask_account_card("Счет 548743")
        mask_account_card("Счет 8")
        mask_account_card("Счет ")
        mask_account_card()


# Тесты даты
@pytest.mark.parametrize(
    "date, formatted_date",
    [
        ("2023-10-15T12:45:30.123456", "15.10.2023"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2000-01-01T00:00:00.000001", "01.01.2000"),
        ("2022-07-04T14:30:00.000000", "04.07.2022"),
        ("2024-05-20T08:15:45.987654", "20.05.2024"),
    ],
)
def test_get_date(date: str, formatted_date: str) -> None:
    """Тест для проверки правильности преобразования даты"""

    assert get_date(date) == formatted_date


def test_nonstandart_get_date():
    """Тест функции по преобразованию даты при неправильном вводе или его отсутсвии"""
    with pytest.raises(ValueError):
        get_date("2024-05-20T08:45.987654")
        get_date("13.03.2015")
        get_date()
