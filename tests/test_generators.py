import pytest
from src.generators import transaction_descriptions, filter_by_currency, card_number_generator
from src.config_test_generators import transactions_list, usd_transactions


@pytest.mark.parametrize("description", ["Перевод организации"])
def test_transaction_descriptions(transactions_list, description):
    """Функция тестирует выдачу списка описания операций"""
    trans = transaction_descriptions(transactions_list)
    assert next(trans) == description


def test_filter_by_currency(transactions_list, usd_transactions):
    """Функция тестирует выдачу списка операция по названию валют"""
    result = filter_by_currency(transactions_list, "USD")
    assert next(result) == usd_transactions


def test_card_number_generator():
    """Функция тестирует генератор номеров карт"""
    card_number = card_number_generator(1, 9999999999999999)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"