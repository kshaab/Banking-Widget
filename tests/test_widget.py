import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def card_number() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account_number() -> str:
    return "Счет 73654108430135874305"


def test_mask_card(card_number: str) -> None:
    assert mask_account_card(card_number) == "Visa Platinum 7000 79** **** 6361"


def test_mask_account(account_number: str) -> None:
    assert mask_account_card(account_number) == "Счет **4305"


@pytest.mark.parametrize(
    "user_input, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card_types(user_input: str, expected_result: str) -> None:
    assert mask_account_card(user_input) == expected_result


@pytest.mark.parametrize(
    "user_input, expected_result",
    [
        ("Vis 700079228960", "Неверный номер счета или карты"),
        ("Счет 7365410843", "Неверный номер счета или карты"),
        (" ", "Неверный номер счета или карты"),
        ("646864", "Неверный номер счета или карты"),
        ("VisaClassic6831982476737658", "Неверный номер счета или карты"),
    ],
)
def test_mask_account_card_invalid(user_input: str, expected_result: str) -> None:
    assert mask_account_card(user_input) == expected_result


@pytest.fixture
def date() -> str:
    return "2024-03-11T02:26:18.671407"


def test_date(date: str) -> None:
    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize(
    "date, expected_result",
    [
        ("2024-031:4738T", "Неверный формат даты"),
        ("11.03.2024", "Неверный формат даты"),
        (",dkdnjsn", "Неверный формат даты"),
        (" ", "Неверный формат даты"),
    ],
)
def test_date_invalid(date: str, expected_result: str) -> None:
    assert get_date(date) == expected_result
