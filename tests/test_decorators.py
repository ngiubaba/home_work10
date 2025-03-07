from typing import Any

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_decorators_log(capsys: CaptureFixture[Any]) -> None:
    """Тест для проверки декоратора логирования функций"""

    @log()
    def myfunc(s: str) -> str:
        return s

    myfunc("Hello")
    output = capsys.readouterr()
    answer = output.out.rstrip()
    result = "myfunc ok"

    assert answer == result


def test_log_error(capsys: CaptureFixture[Any]) -> None:
    """the test for the log decorator when an error is called as a result of executing the wrapped function."""

    @log()
    def myfunc(a: int, b: int = 0) -> float:
        if b == 0:
            raise ValueError
        return a / b

    with pytest.raises(ValueError):
        myfunc(1, 0)
    captured = capsys.readouterr()
    result = "Функция myfunc error: . Inputs: ((1, 0), {})"
    answer: str = captured.out.rstrip()
    assert answer == result
