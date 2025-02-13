def get_mask_card_number(number_cart: int) -> str:
    """Функция скрывающая номер банковской карты"""
    number_cart_str = str(number_cart)
    if len(number_cart_str) != 16:
        return "Введен не верный номер карты"
    else:
        card_mask = number_cart_str[:4] + " " + number_cart_str[4:6] + "** **** " + number_cart_str[12:]
        return card_mask


def get_mask_account(number_account: int) -> str:
    """Функция скрывающая номер банковского счета"""
    number_account_str = str(number_account)
    if len(number_account_str) != 20:
        return "Введен не верный номер счета"
    else:
        account_mask = "**" + number_account_str[16:]
        return account_mask
