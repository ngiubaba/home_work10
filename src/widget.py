from datetime import datetime

from src import masks
from src.masks import InvalidCardNumberError, InvalidAccountNumberError

class InvalidNameCard(Exception):
    pass


def mask_account_card(card: str) -> str:
    """Функция принимающая тип карты или счета и возвращающая скрытую часть"""

    number = ""
    text = ""
    for i in card:
        if i.isdigit():
            number += i
        else:
            text += i

    text_lower = text.lower()

    if "счет" in text_lower:
        if len(number) == 20:
            return f"{text}{masks.get_mask_account(number)}"
        else:
            raise InvalidAccountNumberError("Номер счета должен состоять из 20 цифр")
    elif "visa" in text_lower or "mastercard" in text_lower or "maestro" in text_lower:
        if len(number) == 16:
            return f"{text}{masks.get_mask_card_number(number)}"
        else:
            raise InvalidCardNumberError("Номер карты должен содержать 16 цифр")
    else:
        raise InvalidNameCard("Не верное наименование карты/счета")



def get_date(date: str) -> str:
    """Функция принимающая строку в определенном формате и возвращает дд.мм.гггг"""
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        raise ValueError("Введен не верный формат даты")
    else:
        formatted_date = date_obj.strftime("%d.%m.%Y")
        return formatted_date
