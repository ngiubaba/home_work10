def filter_by_currency(transaction_dict, code):
    """
    Функция итератор для фильтрации транзакций по коду
    :param transaction_dict:
    :param code:
    :return:
    """
    transaction_code = filter(lambda x: x["operationAmount"]["currency"]["code"] == code, transaction_dict)
    return transaction_code

def transaction_descriptions(transaction_dict):
    """
    Функция возвращающая описание каждой транзакции
    :param transaction_dict:
    :return:
    """
    for transaction in transaction_dict:
        yield transaction["description"]


def card_number_generator(begin, end):
    """
    Функция генерирующая номера карт в заданном диапазоне
    :param begin:
    :param end:
    :return:
    """
    int_begin = int(begin)
    int_end = int(end)
    last_number = 9999_9999_9999_9999


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
    generator = card_number_generator(1234567891012141, 1234567891012145)

    # Выводим сгенерированные номера карт
    for card in generator:
        print(card)