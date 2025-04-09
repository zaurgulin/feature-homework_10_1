import json
import os
import requests
from dotenv import load_dotenv
from json import JSONDecodeError


def convert_sum(file_path):
    """
    возвращает сумму транзакции в рублях
    обращается к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли
    :param file_path:
    :return:
    """
    load_dotenv(".env")
    api_key = os.getenv("API_KEY")
    headers = {"api-key": api_key}
    amount_list = []

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            operations = json.load(f)
            for transaction in operations:
                operation_amount = transaction.get("operationAmount")
                if operation_amount is None:
                    continue

                code_from_transaction = operation_amount["currency"]["code"]
                amount_from_transaction = float(operation_amount["amount"])

                if code_from_transaction == "RUB":
                    amount_list.append(amount_from_transaction)
                elif code_from_transaction in ["USD", "EUR"]:

                    url = f"https://api.apilayer.com/currency_data/convert?base=USD&symbols=EUR,GBP,JPY&amount=5"
                    params = {"from": code_from_transaction, "to": "RUB", "amount": amount_from_transaction}
                    response = requests.get(url, headers=headers, params=params)
                    if response.ok:
                        conversion_result = response.json()
                        converted_amount = conversion_result.get("result", 0)
                        amount_list.append(float(converted_amount))

            return amount_list
        except JSONDecodeError:
            return []


if __name__ == "__main__":
    data = convert_sum("C:\\\\PycharmProjects\\\\pythonProject7\\\\data\\\\operations.json")
    print(data)