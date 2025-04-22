import csv
import pandas as pd


def transactions_csv(path_to_the_file: str) -> list:
    """Функция, для считывания финансовых операций из CSV принимает путь к файлу CSV
    и возвращает список словарей с транзакциями"""
    try:
        with open(path_to_the_file, encoding="utf-8") as file:
            pd.read_csv(file)
    except ValueError:
        return []
    except FileNotFoundError:
        return []
    else:
        with open(path_to_the_file, encoding="utf-8") as file:
            operations = pd.read_csv(file, delimiter=";")
            return operations.to_dict(orient="records")


def transactions_xlsx(path_to_the_file: str) -> list:
    """Функция, для считывания финансовых операций из EXCEL принимает путь к файлу EXCEL в качестве аргумента
    и возвращает список словарей с транзакциями"""
    try:
        pd.read_excel(path_to_the_file)
    except ValueError:
        return []
    except FileNotFoundError:
        return []
    else:
        operations = pd.read_excel(path_to_the_file)
        return operations.to_dict(orient="records")


# print(transactions_csv('../data/transactions.csv'))
# print(transactions_xlsx('../data/transactions_excel.xlsx'))


#print(transactions_csv("С:/PycharmProjects/pythonProject7/data/transactions.csv"))

