import csv
import pandas as pd
from typing import List, Dict

def read_transactions_from_csv(csv_file: str) -> List[Dict[str, str]]:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей"""
    transactions_csv = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            transactions_csv.append(row)
    return  transactions_csv

if __name__ == "__main__":
    csv_data = '../data/transactions.csv'
    transactions = read_transactions_from_csv(csv_data)
    for transaction in transactions:
        print(transaction['id'], transaction['state'],
              transaction['date'], transaction['amount'],
              transaction['currency_name'], transaction['currency_code'],
              transaction['from'], transaction['to'], transaction['description'])


def read_transactions_from_excel(excel_file: str) -> List[Dict[str, str]]:
    """Считывает финансовые операции из EXCEL-файла и возвращает список словарей"""
    transactions_excel = []
    excel_data = pd.read_excel(excel_file)
    for index, row in excel_data.iterrows():
        transactions_excel.append(row.to_dict())
    return transactions_excel

if __name__ == "__main__":
    excel_data = '../data/transactions_excel.xlsx'
    transactions = read_transactions_from_excel(excel_data)
    for transaction in transactions:
        print(transaction['id'], transaction['state'],
              transaction['date'], transaction['amount'],
              transaction['currency_name'], transaction['currency_code'],
              transaction['from'], transaction['to'], transaction['description'])
