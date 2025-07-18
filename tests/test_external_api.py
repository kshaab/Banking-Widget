from typing import Any
from unittest.mock import patch

from src.external_api import convert_to_rub, get_rub_amount


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv", return_value="fake_api_key")
def test_convert_to_rub(mock_getenv: Any, mock_get: Any) -> None:
    mock_get.return_value.json = lambda: {"result": 123.45}

    result = convert_to_rub(100, "USD")

    assert result == 123.45
    mock_get.assert_called_once()
    mock_getenv.assert_called_once_with("API_KEY")


def test_get_rub_amount_rub() -> None:
    transaction = {"operationAmount": {"amount": "2000", "currency": {"code": "RUB"}}}
    result = get_rub_amount(transaction)
    assert result == 2000.0


@patch("src.external_api.convert_to_rub", return_value=999.99)
def test_get_rub_amount_usd(mock_convert: Any) -> None:
    transaction = {"operationAmount": {"amount": "20", "currency": {"code": "USD"}}}
    result = get_rub_amount(transaction)
    assert result == 999.99
    mock_convert.assert_called_once_with(20.0, "USD")


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv", return_value="fake_api_key")
def test_convert_to_rub_no_result(mock_getenv: Any, mock_get: Any) -> None:
    mock_get.return_value.json = lambda: {}

    result = convert_to_rub(100, "EUR")
    assert result == 0.0
