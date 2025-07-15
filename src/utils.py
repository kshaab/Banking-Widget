import json
import logging
import os
from typing import Any, Dict, List, cast

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

log_file = os.path.join(os.path.dirname(__file__), "../logs/utils.log")
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_transactions(file: str) -> List[Dict[str, Any]]:
    """Возвращает список словарей с данными о транзакции из JSON-файла"""
    if not os.path.exists(file):
        logger.error("Файл не найден")
        return []
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        logger.info(f"Загружены транзакции из файла: {file}")
        return cast(List[Dict[str, Any]], data)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "operations.json")
    transactions = get_transactions(file_path)
    for transaction in transactions:
        print(json.dumps(transaction, indent=4, ensure_ascii=False))
