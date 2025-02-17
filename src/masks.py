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


def get_mask_account(number_account: str) -> str:
    """Функция скрывающая номер банковского счета"""
    number_account_str = str(number_account)
    if len(number_account_str) != 20:
        return "Введен не верный номер счета"
    else:
        account_mask = "**" + number_account_str[16:]
        return account_mask
