from datetime import datetime

from src import masks
from src.masks import InvalidAccountNumberError, InvalidCardNumberError


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
    else:
        if len(number) == 16:
            return f"{text}{masks.get_mask_card_number(number)}"
        else:
            raise InvalidCardNumberError("Номер карты должен содержать 16 цифр")



def get_date(date: str) -> str:
    """Функция принимающая строку в определенном формате и возвращает дд.мм.гггг"""
    try:
        if "Z" in date:
            date = date[:-1]  # Удаляем последний символ
        if "." in date:
            date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        raise ValueError("Введен не верный формат даты")
    else:
        formatted_date = date_obj.strftime("%d.%m.%Y")
        return formatted_date
