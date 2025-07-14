# Banking Widget

### Виджет, который показывает несколько последних успешных банковских операций клиента. Поддерживает маскирование данных и сортировку. 

### Проект находится на стадии разработки.


## Содержание 

- [Использование](#использование)
- [Разработка](#разработка)
- [Зависимости](#зависимости)
- [Тестирование](#тестирование)
- [Автор](#автор)


## Содержание 

- [Использование](#использование)
- [Разработка](#разработка)
- [Зависимости](#зависимости)
- [Тестирование](#тестирование)
- [Автор](#автор)
## Использование
Клонируйте репозиторий: 
```bash
git clone https://github.com/kshaab/Banking-Widget
cd widget_project
```
Установите зависимости и активируйте виртуальное окружение: 
poetry install
poetry shell

Запустите файл: 
python src/<имя файла>.py

<<<<<<< feature/homework_10_3
## Разработка 

=======

## Разработка 

### Основные функции
- ### `get_mask_card_number(card_number: str) -> str` 
Маскирует номер карты.
get_mask_card_number("7000792289606361")
###  '7000 79** **** 6361'
- ### `get_mask_account(account: str) -> str` 
Маскирует номер счета.
get_mask_account("73654108430135874305")
###  '**4305'
- ### `mask_account_card(info: str) -> str` 
Маскирует номер карты, сохраняя ее название. 
mask_account_card("Visa Platinum 7000792289606361")
### 'Visa Platinum 7000 79** **** 6361'
- ### `get_date(date_str: str) -> str` 
Преобразует формат даты.
get_date("2024-03-11T02:26:18.671407")
### '11.03.2024'
- ### `filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]` 
Фильтрует список словарей по ключу.
filter_by_state(data, state="CANCELED")
- ### `sort_by_date(info: list[dict], reverse: bool = True) -> list[dict]` 
Сортирует список словарей по дате в порядке возрастания/убывания. 
sort_by_date(data, reverse=True)

## Зависимости
Управление зависимостями осуществляется через Poetry (pyproject.toml).

## Тестирование 

В проекте используется фреймворк pytest для запуска тестов.

Запуск тестов:
```
pytest
```

## Основные функции
### Masks
- ### `get_mask_card_number(card_number)` 
Маскирует номер карты.

get_mask_card_number("7000792289606361")
###  '7000 79** **** 6361'
- ### `get_mask_account(account)` 
Маскирует номер счета.

get_mask_account("73654108430135874305")
###  '**4305'
### Widget
- ### `mask_account_card(info)` 
Маскирует номер карты, сохраняя ее название.

mask_account_card("Visa Platinum 7000792289606361")
### 'Visa Platinum 7000 79** **** 6361'
- ### `get_date(date_str)` 
Преобразует формат даты.

get_date("2024-03-11T02:26:18.671407")
### '11.03.2024'
### Processing
- ### `filter_by_state(data, state)` 
Фильтрует список словарей по ключу.

filter_by_state(data, state="CANCELED")
- ### `sort_by_date(info, reverse)` 
Сортирует список словарей по дате в порядке возрастания/убывания. 

sort_by_date(data, reverse=True)
### Generators
- ### `filter_by_currency(transactions, currency_code)`
Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.

filter_by_currency(transactions, "USD")
- ### `transaction_descriptions(transactions)`
Возвращает описание каждой операции по очереди.

transaction_descriptions(transactions) 
- ### `card_number_generator(start, stop)`
Выдает номера карт в заданном формате и диапазоне.

for card_number in card_number_generator(1, 5)
### Decorators 
- ### `log(filename = None)`
Декоратор для логирования функции, выводит результат в консоль, либо в файл (при наличии аргумента с указанием файла).

@log(filename="mylog.txt")
### 'my_function ok, result: 3.'


## Зависимости
Управление зависимостями осуществляется через Poetry (pyproject.toml).


## Тестирование 

В проекте используется фреймворк pytest для запуска тестов.

Запуск тестов:
```bash
pytest tests/ -v
```

## Автор
[Ксения](https://github.com/kshaab)
