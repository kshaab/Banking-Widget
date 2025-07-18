import os

import requests
from dotenv import load_dotenv

from src.utils import get_transactions

load_dotenv()


def convert_to_rub(amount: float, from_currency: str) -> float:
    """Конвертирует валюту в рубли через API"""
    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"

    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)

    data = response.json()
    return float(data.get("result", 0.0))


def get_rub_amount(transaction: dict) -> float:
    """Возвращает суммы транзакций в рублях"""
    amount_str = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    amount = float(amount_str)
    if currency == "RUB":
        return amount
    if currency in ("USD", "EUR"):
        return convert_to_rub(amount, currency)
    return 0.0


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "operations.json")
    transactions = get_transactions(file_path)
    for i, transaction in enumerate(transactions, start=1):
        rub_amount = get_rub_amount(transaction)
        print(f"{i}) Сумма в рублях: {round(rub_amount, 2)}")
