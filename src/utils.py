import json
import os
import logging


path_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils_log.log")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename=path_file,
#    filename="../logs/utils_log.log",
    filemode="w",
    datefmt="%m/%d/%Y %H:%M:%S",
    )
get_info_transactions_json_logger = logging.getLogger()


def get_info_transactions_json(path_file: str) -> list[dict[str]]:
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях или пустой список"""

    try:
        with open(path_file, "r", encoding="utf-8") as transactions_file:
            try:
                transactions_data = json.load(transactions_file)
            except json.JSONDecodeError:
                print("File empty")
                return []
    except FileNotFoundError:
        print("File not found")
        return []
    return transactions_data


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    transactions = get_info_transactions_json
    print(transactions)