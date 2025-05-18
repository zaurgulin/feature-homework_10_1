import re
from collections import Counter


def get_transactions_on_search_bar(data: list[dict], search_bar: str) -> list[dict]:
    """Возвращает список словарей с данными о банковских операциях по строке поиска"""
    pattern = rf"{search_bar}"
    transactions = []
    for transaction in data:
        for tr in transaction.values():
            if re.findall(pattern, str(tr), flags=re.IGNORECASE):
                transactions.append(transaction)
    return transactions


def count_operations(data: list[dict], categories: list) -> dict:
    """Возвращает словарь с количеством операций по категориям"""
    common_categories = [category.lower() for category in categories]
    operations_to_count = []
    for transaction in data:
        if str(transaction.get("description")).lower() in common_categories:
            operations_to_count.append(transaction.get("description"))
    result = Counter(operations_to_count)
    return dict(result)

