from typing import Any, Generator, Iterable


class InvalidValue(Exception):
    """Ошибка неверно введенных значений"""

    pass


def filter_by_currency(transaction_dict: list[dict], code: str) -> Iterable[dict]:
    """
    Функция итератор для фильтрации транзакций по коду
    """
    if not transaction_dict:
        raise InvalidValue("Обнаружены пустые данные")
    transaction_code = filter(lambda x: x["operationAmount"]["currency"]["code"] == code, transaction_dict)
    return transaction_code


def transaction_descriptions(transaction_dict: Any) -> Generator[Any]:
    """
    Функция возвращающая описание каждой транзакции
    """
    if len(transaction_dict) == 0 or transaction_dict == "[]":
        raise InvalidValue("Отсутствует или некорректный словарь")
    for transaction in transaction_dict:
        yield transaction["description"]


def card_number_generator(begin_number: str, end_number: str) -> Generator[str]:
    """
    Функция генерирующая номера карт в заданном диапазоне
    """
    int_begin = int(begin_number)
    int_end = int(end_number)
    last_number = 9999_9999_9999_9999

    if int_begin > last_number:
        raise InvalidValue("Начальный номер выходит за рамки формата номера карты")
    if int_begin < 1:
        int_begin = 1
    if int_end > last_number:
        raise InvalidValue("Конечный номер выходит за рамки формата номера карты")
    if int_begin > int_end:
        raise InvalidValue("Начальный номер карты не может быть больше конечного")

    for number in range(int_begin, int_end + 1):
        str_number = str(number)
        str_number = str_number.rjust(16, "0")

        groups = []
        for i in range(0, 16, 4):
            groups.append(str_number[i : i + 4])

        card_number = " ".join(groups)

        yield card_number
