def filter_by_state(list_transaction: list[dict[str, str]], state: str = "EXECUTED") -> list:
    """Функция принимает словари, а возвращает новый список словарей,
    который содержит только словари с ключом"""

    buffer_list = []
    for i in list_transaction:
        if i["state"] == state:
            buffer_list.append(i)
    return buffer_list


def sort_by_date(list_transaction: list[dict[str, str]], date: bool = True) -> list:
    """Функция принимает список словарей,
    а возвращает список отсортированный по дате"""

    return sorted(list_transaction, key=lambda x: x["date"], reverse=date)
