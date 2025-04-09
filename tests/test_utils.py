import json
from unittest.mock import mock_open, patch

from src.utils import get_info_transactions_json


def test_file_exists_with_valid_json():
    """
    Имитирует, что файл содержит корректный список JSON, возвращает этот список.
    :return:
    """
    data = [{"test": "test"}, {"test1": "test1"}]
    with patch("os.path.exists", return_value=True), patch("builtins.open", mock_open(read_data=json.dumps(data))):

        assert get_info_transactions_json("valid_json_file.json") == data


def test_file_exists_but_empty():
    """
    Имитирует, что существует файл и содержит пустой список, возвращает пустой список.
    :return:
    """
    with patch("os.path.exists", return_value=False), patch("builtins.open", mock_open(read_data="[]")):
        assert get_info_transactions_json("valid_json_file.json") == []


def test_file_not_exists():
    """
    Имитрует, что файл не существует, возвращает пустой список.
    :return:
    """
    with patch("os.path.exists", return_value=False):
        assert get_info_transactions_json("valid_json_file.json") == []


def test_file_exists_with_valid_but_empty_json():
    """
    Имитирует пустой список в JSON, возвращает пустой список.
    :return:
    """
    with patch("os.path.exists", return_value=True), patch("builtins.open", mock_open(read_data="[]")):

        assert get_info_transactions_json("empty_valid_json_file.json") == []