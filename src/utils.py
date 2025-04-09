import json
import logging
import os
from collections import Counter
from typing import Any, Union

from src.external_api import convert_rub
from src.processing import find_by_description

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
    file_path = os.path.join("data", file_name)
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
            logger.debug("Перевод из json файла")
            dict_transaction = json.loads(content)

            if len(dict_transaction) >= 1:
                logger.info("Функция выполнена")
                return dict_transaction
            else:
                return []


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


def counter_category(transactions_data: list, categories: list[str]) -> dict[str, int]:
    """Функция подсчета операций по категориям"""

    categories_count = Counter()

    for category in categories:
        transactions = find_by_description(transactions_data, category)
        for i in range(len(transactions)):
            categories_count.update([category])

    return dict(categories_count)
