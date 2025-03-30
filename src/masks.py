import logging
import os

os.makedirs("logs", exist_ok=True)
log_file = "logs/masks.log"
logger = logging.getLogger(__name__)
file_formatter = logging.Formatter("%(asctime)s %(name)s (%(funcName)s) %(levelname)s: %(message)s")
file_handler = logging.FileHandler(log_file, mode="w", encoding='utf-8')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

class InvalidCardNumberError(Exception):
    """Пользовательское исключение для неверного номера карты."""

    pass


def get_mask_card_number(number_cart: str) -> str:
    """Функция скрывающая номер банковской карты"""
    logger.info("Начало функции")

    if not number_cart.isdigit():
        logger.warning("Ошибка ввода номера карты (недопустимые символы)")
        raise InvalidCardNumberError("Номер карты должен состоять только из цифр")
    if len(number_cart) != 16:
        logger.warning("Ошибка ввода номера карты (неверное кол-во символов)")
        raise InvalidCardNumberError("Номер карты должен содержать 16 цифр")
    card_mask = number_cart[:4] + " " + number_cart[4:6] + "** **** " + number_cart[12:]
    logger.info("Конец функции")
    return card_mask


class InvalidAccountNumberError(Exception):
    """Пользовательское исключение для неверного номера счета"""

    pass


def get_mask_account(number_account: str) -> str:
    """Функция скрывающая номер банковского счета"""
    logger.info("Начало функции")
    if len(number_account) != 20:
        logger.warning("Ошибка ввода номера счета (неверное кол-во символов)")
        raise InvalidAccountNumberError("Номер счета должен состоять из 20 символов")
    if not number_account.isdigit():
        logger.warning("Ошибка ввода номера счета (недопустимые символы)")
        raise InvalidAccountNumberError("Номер счета должен состоять только из цифр")
    account_mask = "**" + number_account[16:]
    return account_mask
