from src.actions_with_bank_operations import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_transactions import read_transactions_from_csv, read_transactions_from_excel
from src.utils import get_transactions
from src.widget import get_date, mask_account_card


def print_transactions(transactions: list[dict]):
    """Выводит отформатированную информацию о транзакциях"""
    for t in transactions:
        date_str = get_date(t.get("date"))
        description = t.get("description", "Без описания")

        from_info = t.get("from")
        to_info = t.get("to")

        operation = t.get("operationAmount", {})
        amount = None
        currency = ""

        if isinstance(operation, dict) and "amount" in operation:
            amount = operation.get("amount")
            currency = operation.get("currency", {}).get("name", "")
        else:

            amount = t.get("amount")
            currency = t.get("currency_name", "")

        from_masked = mask_account_card(from_info) if from_info else ""
        to_masked = mask_account_card(to_info) if to_info else ""

        print(f"{date_str} {description}")
        if from_masked and to_masked:
            print(f"{from_masked} -> {to_masked}")
        elif to_masked:
            print(f"{to_masked}")
        elif from_masked:
            print(f"{from_masked}")

        if amount and currency:
            print(f"Сумма: {amount} {currency}\n")
        else:
            print("Сумма: ---\n")


def main():
    """Объединяет работу модулей в единую программу вывода транзакций"""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    \nВыберите необходимый пункт меню:
  \n1. Получить информацию о транзакциях из JSON-файла
  \n2. Получить информацию о транзакциях из CSV-файла
  \n3. Получить информацию о транзакциях из XLSX-файла"""
    )

    while True:
        choice = input().strip()
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            file_path = "data/operations.json"
            transactions = get_transactions(file_path)
            break
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            file_path = "data/transactions.csv"
            transactions = read_transactions_from_csv(file_path)
            break
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            file_path = "data/transactions_excel.xlsx"
            transactions = read_transactions_from_excel(file_path)
            break
        else:
            print("Введите число от 1 до 3")

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING"
    )

    statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = input().strip().upper()
        if status in statuses:
            print(f"Операции отфильтрованы по статусу {status}")
            result = filter_by_state(transactions, state=status)
            break
        else:
            print(f"Статус операции '{status}' недоступен. Введите статус повторно:")

    print("Отсортировать операции по дате? Да/Нет")
    answer_1 = input().strip().lower()
    if answer_1 == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        answer_2 = input().strip().lower()
        reverse = answer_2 == "по убыванию"
        result = sort_by_date(result, reverse=reverse)
    print("Выводить только рублевые транзакции? Да/Нет")
    answer_3 = input().strip().lower()
    if answer_3 == "да":
        result = filter_by_currency(result, currency_code="RUB")
    elif answer_3 == "нет":
        pass
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer_4 = input().strip().lower()
    if answer_4 == "да":
        print("Введите слово: ")
        word = input().lower()
        result = process_bank_search(result, word)
    if not result:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("Распечатываю итоговый список транзакций...")
    print_transactions(result)
    print(f"Всего банковских операций в выборке: {len(result)}")


if __name__ == "__main__":
    main()
