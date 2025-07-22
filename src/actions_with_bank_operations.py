import re
from src.read_transactions import read_transactions_from_csv
from collections import Counter

def process_bank_search(data:list[dict], search:str)->list[dict]:
    pattern = re.compile(rf'\b{re.escape(search.lower())}\b', re.IGNORECASE)
    matched_transactions = []
    for transaction in data:
        description = transaction.get("description", "").lower()
        if pattern.search(description):
            matched_transactions.append(transaction)
    return matched_transactions

def process_bank_operations(data:list[dict], categories:list)->dict:
    separated_categories = []
    for transactions in data:
        sep_category = transactions.get("description")
        if sep_category and sep_category in categories:
            separated_categories.append(sep_category)

    counted = Counter(separated_categories)
    return dict(counted)



if __name__ == "__main__":
    csv_data = "../data/transactions.csv"
    bank_operations = read_transactions_from_csv(csv_data)
    search = str(input("Введите название операции: ")).strip()
    matches = process_bank_search(bank_operations, search)
    if matches:
        print(f"Найдено {len(matches)} совпадений: ")
        for match in matches:
            print(match)
    else:
        print("Нет совпадений")
    file = "../data/transactions.csv"
    list_categories = [t.get("description") for t in bank_operations if t.get("description")]
    unique_categories = list(set(list_categories))
    category_counts = process_bank_operations(bank_operations, unique_categories)
    print("\nКоличество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count} операций")
