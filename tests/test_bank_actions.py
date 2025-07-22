
from src.actions_with_bank_operations import process_bank_search, process_bank_operations


sample_data = [
    {"description": "Перевод организации", "amount": 1000},
    {"description": "Оплата мобильной связи", "amount": 200},
    {"description": "Перевод организации", "amount": 300},
    {"description": "Покупка в магазине", "amount": 400},
    {"description": "", "amount": 150}
]


def test_process_bank_search_found():
    result = process_bank_search(sample_data, "перевод")
    assert len(result) == 2
    assert all("перевод" in t["description"].lower() for t in result)

def test_process_bank_search_not_found():
    result = process_bank_search(sample_data, "аренда")
    assert result == []

def test_process_bank_operations_counts_correctly():
    categories = ["Перевод организации", "Оплата мобильной связи", "Покупка в магазине"]
    result = process_bank_operations(sample_data, categories)
    assert result == {
        "Перевод организации": 2,
        "Оплата мобильной связи": 1,
        "Покупка в магазине": 1
    }
