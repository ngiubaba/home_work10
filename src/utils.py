import json
import logging
import os
from typing import Any, Union

from src.external_api import convert_rub

os.makedirs("logs", exist_ok=True)
log_file = "logs/utils.log"
logger = logging.getLogger(__name__)
file_formatter = logging.Formatter("%(asctime)s %(name)s (%(funcName)s) %(levelname)s: %(message)s")
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def transaction_dictionary(file_name: str = "operations.json") -> Union[list[dict], dict]:
    logger.info("Начало функции")
    dict_transaction: list[dict[str, Any]] = []
    file_path = os.path.join("..", "data", file_name)
    if not os.path.exists(file_path):
        logger.debug("Файл пустой")
        return dict_transaction
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            logger.debug("Файл найден")
            content = f.read().strip()
            if not content:
                logger.debug("Файл пустой")
                return []
            logger.debug("Перевод в json файл")
            dict_transaction = json.loads(content)

            if type(dict_transaction) is list:
                logger.info("Функция выполнена")
                return dict_transaction
            else:
                return []


transaction_data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "10", "currency": {"name": "руб.", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


def get_transaction_amount(transaction_data: dict[str, Any]) -> float:
    logger.info("Начало функции")
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        logger.debug("Функция выполнена")
        return float(transaction_data["operationAmount"]["amount"])
    else:
        logger.debug("Будет выполнен перевод в RUB")
        amount = transaction_data["operationAmount"]["amount"]
        from1 = transaction_data["operationAmount"]["currency"]["code"]
        result = convert_rub(from1, amount)
        logger.info("Функция выполнена после перевода валюты")
        return float(result)


if __name__ == "__main__":
    logger.info("Запуск программы")
    print(get_transaction_amount(transaction_data))
