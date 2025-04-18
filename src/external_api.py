import json
import os
import requests
from dotenv import load_dotenv
from json import JSONDecodeError


def convert_to_rub(transaction: dict) -> float:
    """
    Функция конвертации, возвращает сумму транзакции в рублях
    обращается к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли
    """
    load_dotenv(".env")
    api_key = os.getenv("API_KEY")
    headers = {"api-key": api_key}
#    amount_list = []

    amount_from_transaction = transaction["operationAmount"]["amount"]
    code_from_transaction = transaction["operationAmount"]["currency"]["code"]
    if amount_from_transaction == "0":
        return float(0)
    elif code_from_transaction != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_from_transaction}&amount={amount_from_transaction}"
        rub_amount = requests.request("GET", url=url, headers=headers)

        result = rub_amount.json()

        return float(result["result"])
    else:
        return float(amount_from_transaction)


#    with open(transaction, "r", encoding="utf-8") as f:
#        try:
#            operations = json.load(f)
#            for transaction in operations:
#                operation_amount = transaction.get("operationAmount")
#                if operation_amount is None:
#                    continue
#
#                code_from_transaction = operation_amount["currency"]["code"]
#                amount_from_transaction = float(operation_amount["amount"])
#
#                if code_from_transaction == "RUB":
#                    amount_list.append(amount_from_transaction)
#                elif code_from_transaction in ["USD", "EUR"]:
#
#                    url = f'https://api.apilayer.com/currency_data/convert?base=USD&symbols=EUR,GBP,JPY&amount=5'
#                    params = {"from": code_from_transaction, "to": "RUB", "amount": amount_from_transaction}
#                    response = requests.get(url, headers=headers, params=params)
#                    if response.ok:
#                        conversion_result = response.json()
#                        converted_amount = conversion_result.get("result", 0)
#                        amount_list.append(float(converted_amount))
#
#            return amount_list
#        except JSONDecodeError:
#            return []
#
#
#if __name__ == "__main__":
#    data = convert_sum("C:\\\\PycharmProjects\\\\pythonProject7\\\\data\\\\operations.json")
#    print(data)