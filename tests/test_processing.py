import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        ("EXECUTED", [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]),
        ("CANCELED", [{"id": 2, "state": "CANCELED"}]),
        ("OPEN", []),
    ],
)
def test_filter_by_state(sample_data: list[dict], state: str, expected: list[dict]) -> None:
    assert filter_by_state(sample_data, state) == expected


@pytest.fixture
def data_list() -> list[dict]:
    return [
        {"id": 1, "date": "2024-03-11T14:26:00"},
        {"id": 2, "date": "2023-12-05T10:00:00"},
        {"id": 3, "date": "2024-03-11T14:26:00"},
        {"id": 4, "date": "неверная_дата"},
        {"id": 5},
        {"id": 6, "date": "2025-01-01T00:00:00"},
    ]


def test_sort_descending(data_list: list[dict]) -> None:
    result = sort_by_date(data_list, reverse=True)
    ids = [item["id"] for item in result]
    assert ids == [6, 1, 3, 2]


def test_sort_ascending(data_list: list[dict]) -> None:
    result = sort_by_date(data_list, reverse=False)
    ids = [item["id"] for item in result]
    assert ids == [2, 1, 3, 6]


def test_sort_with_same_dates(data_list: list[dict]) -> None:
    sorted_list = sort_by_date(data_list, reverse=True)
    i_1 = [index for index, item in enumerate(sorted_list) if item["id"] == 1][0]
    i_3 = [index for index, item in enumerate(sorted_list) if item["id"] == 3][0]
    assert i_3 == i_1 + 1


def test_invalid_dates_excluded(data_list):
    result = sort_by_date(data_list)
    ids = [item["id"] for item in result]
    assert 4 not in ids and 5 not in ids
