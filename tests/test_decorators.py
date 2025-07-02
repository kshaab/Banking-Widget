import pytest
from src.decorators import log

def test_log_my_function():
    @log()
    def add_numbers(x, y):
        return x + y
    result = add_numbers(5, 8)
    assert result == 13

def test_console_output_error(capsys):
    @log()
    def divide(x, y):
        return x / y
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert "Функция divide начала работу" in captured.out
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0)" in captured.out

def test_console_output_success(capsys):
    @log()
    def add(x, y):
        return x + y
    result = add(7, 3)
    captured = capsys.readouterr()
    assert "Функция add начала работу" in captured.out
    assert "Функция add закончила работу" in captured.out
    assert "add ok" in captured.out
    assert result == 10

def test_log_write_to_file_success():
    file = "test_decorator.txt"
    @log(filename=file)
    def check_func(x, y):
        return x + y
    result = check_func(5, 8)
    assert result == 13
    with open ("test_decorator.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert f"check_func is ok, result: 13."

def test_log_write_to_file_error():
    file = "test_decorator.txt"
    @log(filename=file)
    def check_func(x, y):
        return x / y
    with pytest.raises(ZeroDivisionError):
        check_func(5, 0)
    with open ("test_decorator.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "check_func error: ZeroDivisionError. Inputs: (5, 0)" in content


