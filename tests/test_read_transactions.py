from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.read_transactions import read_transactions_from_csv, read_transactions_from_excel

mock_csv = (
    "id;state;date;amount;currency_name;currency_code;from;to;description\n"
    "1;EXECUTED;2023-01-01;1000;RUB;643;Alice;Bob;Transfer\n"
    "2;CANCELLED;2023-01-02;2000;USD;840;Charlie;Dave;Refund\n"
)

mock_excel = pd.DataFrame(
    [
        {
            "id": "1",
            "state": "EXECUTED",
            "date": "2023-01-01",
            "amount": "1000",
            "currency_name": "RUB",
            "currency_code": "643",
            "from": "Alice",
            "to": "Bob",
            "description": "Transfer",
        },
        {
            "id": "2",
            "state": "CANCELLED",
            "date": "2023-01-02",
            "amount": "2000",
            "currency_name": "USD",
            "currency_code": "840",
            "from": "Charlie",
            "to": "Dave",
            "description": "Refund",
        },
    ]
)


@patch("builtins.open", new_callable=mock_open, read_data=mock_csv)
def test_read_valid_csv(mock_file: Any) -> None:
    transactions = read_transactions_from_csv("fake.csv")
    assert len(transactions) == 2
    assert transactions[0]["id"] == "1"
    assert transactions[1]["state"] == "CANCELLED"
    mock_file.assert_called_once_with("fake.csv", newline="", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_csv(mock_file: Any) -> None:
    transactions = read_transactions_from_csv("empty.csv")
    assert transactions == []


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n",
)
def test_csv_with_only_headers(mock_file: Any) -> None:
    transactions = read_transactions_from_csv("headers.csv")
    assert transactions == []


@patch("pandas.read_excel")
def test_read_excel_valid(mock_read_excel: Any) -> None:
    mock_read_excel.return_value = mock_excel
    result = read_transactions_from_excel("fake_excel.xlsx")
    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[1]["state"] == "CANCELLED"
    mock_read_excel.assert_called_once_with("fake_excel.xlsx")


@patch("pandas.read_excel")
def test_read_excel_empty(mock_read_excel: Any) -> None:
    mock_read_excel.return_value = pd.DataFrame()
    result = read_transactions_from_excel("empty.xlsx")
    assert result == []
    mock_read_excel.assert_called_once_with("empty.xlsx")
