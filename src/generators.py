from typing import Generator


def filter_by_currency(transactions_list, currency) -> Generator:
    """Функция, которая будет выводить транзакции по заданной валюте"""
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions_list):
    """Генератор, который вводит описание операции по очереди"""
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Функция которая генерирует номер карты"""
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"

    for card_number in card_number_generator(1, 20):
        return card_number