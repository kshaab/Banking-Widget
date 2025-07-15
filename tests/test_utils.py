import json
from unittest.mock import mock_open, patch

from src.utils import get_transactions


def test_get_transactions_success() -> None:
    fake_data = [{"id": 8, "amount": "33"}, {"id": 1, "amount": "1987"}]
    fake_json = json.dumps(fake_data)
    with patch("builtins.open", mock_open(read_data=fake_json)):
        with patch("os.path.exists", return_value=True):
            result = get_transactions("any_path.json")
            assert result == fake_data


def test_get_transactions_file_not_found() -> None:
    with patch("os.path.exists", return_value=False):
        result = get_transactions("missing.json")
        assert result == []
