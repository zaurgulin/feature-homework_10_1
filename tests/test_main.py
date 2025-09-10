from typing import Any
from unittest.mock import mock_open, patch

from src.main import choice_state, ending_result, file_selection, filter_by_world, sort_by_rub
from src.processing import sort_by_date

transaction_list_sample = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "amount": 31957.58,
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
]


@patch("builtins.input", side_effect="1")
@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
@patch("src.utils.get_info_transactions_json")
def test_file_selection_json(mock_get_json: Any, mock_file: Any, mock_input: Any) -> None:
    assert file_selection() == [{"amount": 100, "currency": "USD"}]


@patch("builtins.input", side_effect="2")
@patch("builtins.open", new_callable=mock_open, read_data="amount;currency\n100;USD")
@patch("src.transactions_csv_xlsx.transactions_csv")
def test_file_selection_csv(mock_get_csv: Any, mock_file: Any, mock_input: Any) -> None:
    assert file_selection() == [{"amount": 100, "currency": "USD"}]


@patch("builtins.input", side_effect="3")
@patch("builtins.open", new_callable=mock_open, read_data=b"\x3c\x80\x00\x00\x00")
@patch("src.transactions_csv_xlsx.transactions_xlsx")
def test_file_selection_xlsx(mock_get_xlsx: Any, mock_file: Any, mock_input: Any) -> None:
    assert file_selection() == []


@patch("builtins.input", side_effect=["EXECUTED"])
def test_choice_state(mock_input: Any) -> None:
    assert choice_state(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_choice_sort_by_date(mock_input: Any) -> None:
    mock_input.return_value = "да"
    assert sort_by_date(transaction_list_sample) == transaction_list_sample


@patch("builtins.input", side_effect=["RUB"])
def test_sort_by_rub(mock_input: Any) -> None:
    assert sort_by_rub(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_filter_by_world(mock_input: Any) -> None:
    mock_input.return_value = "да"
    assert filter_by_world(transaction_list_sample, "Перевод организации") == transaction_list_sample


def test_ending_result() -> None:
    assert ending_result(transaction_list_sample) is None