class InvalidCardNumberError(Exception):
    """Пользовательское исключение для неверного номера карты."""

    pass


def get_mask_card_number(number_cart: str) -> str:
    """Функция скрывающая номер банковской карты"""

    if not number_cart.isdigit():
        raise InvalidCardNumberError("Номер карты должен состоять только из цифр")
    if len(number_cart) != 16:
        raise InvalidCardNumberError("Номер карты должен содержать 16 цифр")
    card_mask = number_cart[:4] + " " + number_cart[4:6] + "** **** " + number_cart[12:]
    return card_mask


class InvalidAccountNumberError(Exception):
    """Пользовательское исключение для неверного номера счета"""

    pass


def get_mask_account(number_account: str) -> str:
    """Функция скрывающая номер банковского счета"""

    if len(number_account) != 20:
        raise InvalidAccountNumberError("Номер счета должен состоять из 20 цифр")
    if not number_account.isdigit():
        raise InvalidAccountNumberError("Номер счета должен состоять только из цифр")
    account_mask = "**" + number_account[16:]
    return account_mask
