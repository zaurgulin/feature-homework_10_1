import json
from unittest.mock import mock_open, patch

from src.external_api import convert_to_rub

mock_conv_response = {"result": 7500}

mock_file = json.dumps(
    [
        {
            "operationAmount": {
                "amount": 10,
                "currency": {"code": "USD"},
            }
        },
        {
            "operationAmount": {
                "amount": 1200,
                "currency": {"code": "RUB"},
            }
        },
    ]
)


@patch("builtins.open", new_callable=mock_open, read_data=mock_file)
@patch("os.getenv", return_value="test_api_key")
@patch("requests.get")
def convert_to_rub(mock_get, mock_open, mock_file):
    mock_get.return_value.ok = True
    mock_get.return_value.json.return_value = mock_conv_response

    result = convert_to_rub("test_api_key")

    expected = [7500.0, 1200.0]

    assert result == expected