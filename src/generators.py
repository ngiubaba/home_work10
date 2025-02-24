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
            groups.append(str_number[i: i + 4])

        card_number = " ".join(groups)

        yield card_number


if __name__ == "__main__":
    # Создаем генератор для диапазона от 1 до 10
    begin = ""
    # end = input("конечное")
    # transactions_data: list[dict] = [
    #     {
    #         "id": 939719570,
    #         "state": "EXECUTED",
    #         "date": "2018-06-30T02:08:58.425572",
    #         "operationAmount": {
    #             "amount": "9824.07",
    #             "currency": {
    #                 "name": "USD",
    #                 "code": "USD"
    #             }
    #         },
    #         "description": "Перевод организации",
    #         "from": "Счет 75106830613657916952",
    #         "to": "Счет 11776614605963066702"
    #     },
    #     {
    #         "id": 142264268,
    #         "state": "EXECUTED",
    #         "date": "2019-04-04T23:20:05.206878",
    #         "operationAmount": {
    #             "amount": "79114.93",
    #             "currency": {
    #                 "name": "USD",
    #                 "code": "USD"
    #             }
    #         },
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 19708645243227258542",
    #         "to": "Счет 75651667383060284188"
    #     },
    #     {
    #         "id": 873106923,
    #         "state": "EXECUTED",
    #         "date": "2019-03-23T01:09:46.296404",
    #         "operationAmount": {
    #             "amount": "43318.34",
    #             "currency": {
    #                 "name": "руб.",
    #                 "code": "RUB"
    #             }
    #         },
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 44812258784861134719",
    #         "to": "Счет 74489636417521191160"
    #     },
    #     {
    #         "id": 895315941,
    #         "state": "EXECUTED",
    #         "date": "2018-08-19T04:27:37.904916",
    #         "operationAmount": {
    #             "amount": "56883.54",
    #             "currency": {
    #                 "name": "USD",
    #                 "code": "USD"
    #             }
    #         },
    #         "description": "Перевод с карты на карту",
    #         "from": "Visa Classic 6831982476737658",
    #         "to": "Visa Platinum 8990922113665229"
    #     },
    #     {
    #         "id": 594226727,
    #         "state": "CANCELED",
    #         "date": "2018-09-12T21:27:25.241689",
    #         "operationAmount": {
    #             "amount": "67314.70",
    #             "currency": {
    #                 "name": "руб.",
    #                 "code": "RUB"
    #             }
    #         },
    #         "description": "Перевод организации",
    #         "from": "Visa Platinum 1246377376343588",
    #         "to": "Счет 14211924144426031657"
    #     }
    # ]
    generator = transaction_descriptions()
    print(generator)
    # Выводим сгенерированные номера карт
    for card in generator:
        print(card)