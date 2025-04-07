import re


def filter_by_state(list_transaction: list[dict[str, str]], state: str = "EXECUTED") -> list:
    """Функция принимает словари, а возвращает новый список словарей,
    который содержит только словари с ключом"""

    buffer_list = []
    for i in list_transaction:
        if i["state"] == state:
            buffer_list.append(i)
    return buffer_list


class LengthListError(Exception):
    pass


def sort_by_date(list_transaction: list[dict[str, str]], date: bool = True) -> list:
    """Функция принимает список словарей,
    а возвращает список отсортированный по дате"""
    if len(list_transaction) == 0:
        raise LengthListError("Введено пустое значение")
    else:
        return sorted(list_transaction, key=lambda x: x["date"], reverse=date)


def find_by_description(list_transaction: list, find_word: str) -> list:
    """Функция принимает список словарей и строку поиска,
    возвращает списки в которых есть эта строка"""
    r = re.compile(find_word, re.IGNORECASE)
    filtered_transactions = filter(lambda x: r.search(x["description"]), list_transaction)
    return list(filtered_transactions)