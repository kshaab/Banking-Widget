import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def currency() -> list:
   return [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {}},
        {},
    ]

@pytest.fixture
def descriptions() -> list:
    return [
        { "description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"}
    ]

def test_filter_by_currency(currency: list) -> None:
    result = list(filter_by_currency(currency, "USD"))
    assert result ==  [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}]
    assert list(filter_by_currency(currency, "ОРН")) == []
    assert list(filter_by_currency(currency, " ")) == []


def test_transaction_descriptions(descriptions: list) -> None:
    result = list(transaction_descriptions(descriptions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected
    assert list(transaction_descriptions([])) == []


@pytest.fixture
def card_number_range() -> tuple[int, int]:
    return 1, 4

def test_card_number_generator(card_number_range: int) -> None:
    start,stop = card_number_range
    generate = card_number_generator(start,stop)
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
    ]
    assert list(generate) == expected

def test_card_number_generator_completion():
    generate = card_number_generator(5, 5)
    card = next(generate)
    assert card == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(generate)

def test_card_number_format():
    for number in range(1, 10):
        card = next(card_number_generator(number, number))
        assert len(card.replace(" ", "")) == 16
        parts = card.split(" ")
        assert len(parts) == 4
        for part in parts:
            assert len(part) == 4
            assert part.isdigit()

