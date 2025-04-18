import csv
from unittest.mock import MagicMock, mock_open, patch
import pandas as pd


from src.transactions_csv_xlsx import transactions_csv, transactions_xlsx


def test_transactions_csv_correct_file():
    """ Имитирует успешное чтение CSV-файла и проверяет, что результат соответствует ожидаемому списку словарей. """
    mock_csv_content = "name;amount;date\nJohn;100;2023-01-01\nJane;150;2023-01-02\n"
    expected_result = [
        {"name": "John", "amount": "100", "date": "2023-01-01"},
        {"name": "Jane", "amount": "150", "date": "2023-01-02"},
    ]

    with patch("builtins.open", mock_open(read_data=mock_csv_content), create=True):
        with patch("csv.DictReader", return_value=csv.DictReader(mock_csv_content.splitlines(), delimiter=";")):
            result = transactions_csv("fake_file.csv")
            assert result == expected_result


def test_transactions_csv_empty_filename():
    """ Проверяет, что функция возвращает пустой список, если имя файла пустое."""
    assert transactions_csv("") == []


def test_transactions_csv_file_not_found():
    """ Симулирует случай, когда файл не найден, и проверяет, что возвращается пустой список."""
    with patch("builtins.open", MagicMock(side_effect=FileNotFoundError()), create=True):
        assert transactions_csv("fake_file.csv") == []


@patch("pandas.read_excel")
def test_transactions_xlsx(mock_read_excel):
    ''' Имитирует успешное чтение Excel-файла и проверяет, что результат соответствует ожидаемому списку словарей. '''
    mock_data = [{"transaction_id": 1, "amount": 100}, {"transaction_id": 2, "amount": 200}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    result = transactions_xlsx("test_file.xlsx")

    assert result == mock_data


def test_empty_filename():
    ''' Проверяет, что функция возвращает пустой список, если имя файла пустое. '''
    result = transactions_xlsx("")
    assert result == []


@patch("pandas.read_excel")
def test_file_not_found(mock_read_excel):
    ''' Проверяет, что функция возвращает пустой список, если файл не найден. '''
    mock_read_excel.side_effect = FileNotFoundError
    result = transactions_xlsx("test_file.xlsx")
    assert result == []