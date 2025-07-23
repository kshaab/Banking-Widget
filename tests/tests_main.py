from src.actions_with_bank_operations import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date

sample_data = [
    {
        "state": "EXECUTED",
        "date": "2023-01-01T10:00:00Z",
        "amount": 1000,
        "currency_name": "RUB",
        "description": "Оплата услуг",
    },
    {
        "state": "CANCELED",
        "date": "2023-05-05T12:00:00Z",
        "amount": 500,
        "currency_name": "USD",
        "description": "Покупка книги",
    },
]


def test_filter_by_state():
    result = filter_by_state(sample_data, state="EXECUTED")
    assert len(result) == 1
    assert result[0]["state"] == "EXECUTED"


def test_sort_by_date():
    sorted_data = sort_by_date(sample_data, reverse=False)
    assert sorted_data[0]["date"] < sorted_data[1]["date"]


def test_filter_by_currency():
    data = [
        {
            "amount": 1000,
            "currency_code": "RUB",
            "description": "Зачисление",
        },
        {
            "operationAmount": {"amount": 2000, "currency": {"code": "USD", "name": "Доллары"}},
            "description": "Перевод",
        },
        {"operationAmount": {"amount": 3000, "currency": {"code": "RUB", "name": "Рубли"}}, "description": "Оплата"},
    ]
    result = list(filter_by_currency(data, currency_code="RUB"))
    assert len(result) == 2


def test_process_bank_search():
    result = process_bank_search(sample_data, search="услуг")
    assert len(result) == 1
    assert "услуг" in result[0]["description"].lower()
