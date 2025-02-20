import pytest

from src.masks import InvalidAccountNumberError, InvalidCardNumberError, get_mask_account, get_mask_card_number


# Проверки номера карты
@pytest.mark.parametrize(
    "card_number, mask",
    [
        ("4276310049981287", "4276 31** **** 1287"),
        ("5112236163973336", "5112 23** **** 3336"),
        ("5064355506228782", "5064 35** **** 8782"),
        ("9831756489651254", "9831 75** **** 1254"),
    ],
)
def test_get_mask_card_number(card_number: str, mask: str) -> None:
    """Тест для проверки правильности маскирования номера карты"""

    assert get_mask_card_number(card_number) == mask


def test_get_mask_nonstandart_card_number() -> None:
    """Тест для проверки работы функции при нестандартном номере карт,
    разной длины номера карт, а так же наличие букв в номере и отсутствие номера"""

    with pytest.raises(InvalidCardNumberError):
        get_mask_card_number("9843871563147851874")
        get_mask_card_number("5688188375123")
        get_mask_card_number("6")
        get_mask_card_number("89327432FMD3456G")
        get_mask_card_number("")


# Проверки номера счета
@pytest.mark.parametrize(
    "number_account, mask",
    [
        ("61778486332213909509", "**9509"),
        ("12313346236137207109", "**7109"),
        ("37763857132929736475", "**6475"),
        ("97955102605871887237", "**7237"),
    ],
)
def test_get_mask_account(number_account: str, mask: str) -> None:
    """Тест для правильности маскирования номера счета"""

    assert get_mask_account(number_account) == mask


def test_get_mask_nonstandart_account_number() -> None:
    """Тест для проверки работы функции при нестандартном номере счета,
    разной длины номера счета, а так же наличие букв в счете и отсутствие счета"""

    with pytest.raises(InvalidAccountNumberError):
        get_mask_account("5461587951348915672")
        get_mask_account("5688188375123")
        get_mask_account("6")
        get_mask_account("89327432FMD3456G4985")
        get_mask_account("")
