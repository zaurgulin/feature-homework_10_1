from collections import Counter

from src.sorting import count_operations, get_transactions_on_search_bar


def test_get_transactions_on_search_bar(transactions_list: list) -> None:
    assert get_transactions_on_search_bar(transactions_list, "CANCELED") == [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_count_operations(transactions_list: list) -> None:
    assert count_operations(transactions_list, ["Перевод со счета на счет"]) == {"Перевод со счета на счет": 2}