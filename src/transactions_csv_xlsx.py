import csv

import pandas as pd


def transactions_csv(filename: str) -> list:
    """ Считывает CSV файл с транзакциями и возвращает список словарей этих транзакций """
    if len(filename) == 0 or not isinstance(filename, str):
        return []
    try:
        with open(filename, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        return []


def transactions_xlsx(filename: str) -> list:
    """ Считывает Excel файл с транзакциями и возвращает список словарей этих транзакций """
    if len(filename) == 0 or not isinstance(filename, str):
        return []
    try:
        ecxel_data = pd.read_excel(filename)
        ecxel_data = ecxel_data.to_dict("records")
        return ecxel_data
    except FileNotFoundError:
        return []


#print(transactions_csv("С:/PycharmProjects/pythonProject7/data/transactions.csv"))

