from src import masks
from datetime import datetime


def mask_account_card(card: str) -> str:
    """Функция принимающая тип карты или счета и возвращающая скрытую часть"""
    number = ""
    text = ""
    for i in card:
        if i.isdigit():
            number += i
        else:
            text += i
    if "счет" in text.lower():
        return f"{text}{masks.get_mask_account(number)}"
    else:
        return f"{text}{masks.get_mask_card_number(number)}"


def get_date(date: str) -> str:
    """Функция принимающая строку в определенном формате и возвращает дд.мм.гггг"""
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date
