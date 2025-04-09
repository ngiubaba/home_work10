from src.generators import filter_by_currency
from src.processing import filter_by_state, find_by_description, sort_by_date
from src.utils import transaction_dictionary
from src.utils_files import read_csv, read_excel
from src.widget import get_date, mask_account_card


def main() -> None:

    filename_json = "operations.json"
    filename_csv = "data/transactions.csv"
    filename_excel = "data/transactions_excel.xlsx"

    print(
        """Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.\n"""
    )

    print(
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )
    user_change = input("Пользователь: ")

    list_transaction: list = []

    if user_change == "1":
        list_transaction = transaction_dictionary(filename_json)
        print("Программа: Для обработки выбран JSON-файл.\n")
    elif user_change == "2":
        list_transaction = read_csv(filename_csv)
        print("Программа: Для обработки выбран CVS-файл.")
    elif user_change == "3":
        list_transaction = read_excel(filename_excel)
        print("Программа: Для обработки выбран XLSX-файл.")

    good_change = True
    while good_change:
        print(
            """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )

        user_change_status = input("Пользователь: ")

        if user_change_status.upper() == "EXECUTED":
            list_transaction = filter_by_state(list_transaction, "EXECUTED")
            print(f'Программа: Операции отфильтрованы по статусу "{user_change_status.upper()}"\n')
            good_change = False
        elif user_change_status.upper() == "CANCELED":
            list_transaction = filter_by_state(list_transaction, "CANCELED")
            print(f'Программа: Операции отфильтрованы по статусу "{user_change_status.upper()}"\n')
            good_change = False
        elif user_change_status.upper() == "PENDING":
            list_transaction = filter_by_state(list_transaction, "PENDING")
            print(f'Программа: Операции отфильтрованы по статусу "{user_change_status.upper()}"\n')
            good_change = False
        else:
            print(f'Программа: Статус операции "{user_change_status}" недоступен.')

    print("Программа: Отсортировать операции по дате? Да/Нет")
    sort_date = input("Пользователь: ")
    is_date = True
    if sort_date.lower() == "да":
        is_date = True
    elif sort_date.lower() == "нет":
        is_date = False
    date = False
    if is_date:
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию?")
        sort_by_sort = input("Пользователь: ")
        if sort_by_sort.lower() == "по возрастанию":
            date = False
        elif sort_by_sort.lower() == "по убыванию":
            date = True
        list_transaction = sort_by_date(list_transaction, date)

    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")
    transactions_rub = input("Пользователь: ")
    if transactions_rub.lower() == "да":
        list_transaction = list(filter_by_currency(list_transaction, "RUB"))

    print(
        """\nПрограмма: Отфильтровать список транзакций по определенному слову
в описании? Да/Нет"""
    )
    sort_by_word = input("Пользователь: ")
    if sort_by_word == "да":
        word = input("Введите слово для фильтра: ")

        list_transaction = find_by_description(list_transaction, word)

    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")
    print("Программа:")
    print(f"Всего банковских операций в выборке: {len(list_transaction)}")

    for transaction in list_transaction:
        print()
        date_transactions = get_date(transaction["date"])
        description = transaction["description"]
        print(f"{date_transactions} {description}")
        from_ = ""
        if "from" in transaction:
            from_ = transaction["from"]
        to_ = transaction["to"]
        if from_ != from_ or from_ == "":
            print(f"{mask_account_card(to_)}")
        else:
            print(f"{mask_account_card(from_)} -> {mask_account_card(to_)}")
        amount = transaction["operationAmount"]["amount"]
        currency_name = transaction["operationAmount"]["currency"]["name"]
        print(f"Сумма: {amount} {currency_name}")


if __name__ == "__main__":
    main()
