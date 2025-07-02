from typing import Any

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_log_my_function() -> Any:
    @log()
    def add_numbers(x: int, y: int) -> int:
        return x + y

    result = add_numbers(5, 8)
    assert result == 13


def test_console_output_error(capsys: CaptureFixture) -> None:
    @log()
    def divide(x: float, y: float) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert "Функция divide начала работу" in captured.out
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0)" in captured.out


def test_console_output_success(capsys: CaptureFixture) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    result = add(7, 3)
    captured = capsys.readouterr()
    assert "Функция add начала работу" in captured.out
    assert "Функция add закончила работу" in captured.out
    assert "add ok" in captured.out
    assert result == 10


def test_log_write_to_file_success() -> Any:
    file = "test_decorator.txt"

    @log(filename=file)
    def check_func(x: int, y: int) -> int:
        return x + y

    result = check_func(5, 8)
    assert result == 13
    with open("test_decorator.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "check_func ok, result: 13." in content


def test_log_write_to_file_error() -> Any:
    file = "test_decorator.txt"

    @log(filename=file)
    def check_func(x: float, y: float) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        check_func(5, 0)
    with open("test_decorator.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "check_func error: ZeroDivisionError. Inputs: (5, 0)" in content
