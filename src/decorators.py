import functools

def log(filename=None):
    """Декоратор для логирования функции,
    выводит результат либо в файл, либо в консоль в зависимости от наличия аргумента"""
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
             print(f"Функция {func.__name__} начала работу")
             try:
                 result = func(*args, **kwargs)
                 print(f"Функция {func.__name__} закончила работу")
                 success_result = f"{func.__name__} ok, result: {result}."
                 if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_result + "\n")
                 else:
                    print(success_result)
                 return result
             except Exception as e:
                 error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                 if filename:
                     with open(filename, "a", encoding="utf-8") as text:
                         text.write(error_message + "\n")
                 else:
                     print(error_message)
                 raise
        return inner
    return wrapper


if __name__ == "__main__":
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
