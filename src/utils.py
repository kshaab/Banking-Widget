import json
import os
from typing import List, Dict, Any

def get_transactions(file: str) -> List[Dict[str, Any]]:
    """Возвращает список словарей с данными о транзакции из JSON-файла"""
    if not os.path.exists(file):
        return []
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'operations.json')
    transactions = get_transactions(file_path)
    for transaction in transactions:
        print(json.dumps(transaction, indent=4, ensure_ascii=False))

