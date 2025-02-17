import pytest

from src.masks import get_mask_card_number, get_mask_account, InvalidCardNumberError


@pytest.mark.parametrize("card_number, mask",
                         [
                             ("4276310049981287", "4276 31** **** 1287"),
                             ("5112236163973336", "5112 23** **** 3336"),
                             ("5064355506228782", "5064 35** **** 8782"),
                             ("9831756489651254", "9831 75** **** 1254")
                         ]
                         )
def test_get_mask_card_number(card_number, mask):
    """Тест для проверки правильности маскирования номера карты"""
    assert get_mask_card_number(card_number) == mask


def test_get_mask_nonstandart_card_nubmer():
    """Тест для проверки работы функции при нестандартном номере карт,
    разной длины номера карт, а так же наличие букв в номере и отсутствие номера"""
    with pytest.raises(InvalidCardNumberError):
        get_mask_card_number("9843871563147851874")
        get_mask_card_number("5688188375123")
        get_mask_card_number("6")
        get_mask_card_number("89327432FMD3456G")
        get_mask_card_number()


@pytest.mark.parametrize("number_account, mask",
                         [(""),
                          (""),
                          (""),
                          ("")
                          ])
# Функция
# get_mask_account
# :
# Тестирование правильности маскирования номера счета.
# Проверка работы функции с различными форматами и длинами номеров счетов.
# Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.