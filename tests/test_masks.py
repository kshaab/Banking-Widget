import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "user_input, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("700079228960636162536", "Неверный номер карты"),
        ("Gjdybwudm", "Неверный номер карты"),
        (" ", "Неверный номер карты"),
    ],
)
def test_mask(user_input: str, expected_result: str) -> None:
    assert get_mask_card_number(user_input) == expected_result


@pytest.mark.parametrize(
    "user_input, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("73654108430135", "Неверный номер счета"),
        ("73654108430fyew", "Неверный номер счета"),
        (" ", "Неверный номер счета"),
    ],
)
def test_mask_account(user_input: str, expected_result: str) -> None:
    assert get_mask_account(user_input) == expected_result
