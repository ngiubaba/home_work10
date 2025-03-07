# import datetime
from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str = "") -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """

    :rtype: object
    """

    def log_function(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # start_time = datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")

            try:
                # start_message = f"{start_time} Функция {func.__name__} начала работу"
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                # {start_time}

                return result

            except Exception as e:
                error_message = str(e)
                log_message = f"Функция {func.__name__} error: {error_message}." f" Inputs: ({args}, {kwargs})"
                # {start_time}

                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return log_function
