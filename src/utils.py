import json
import os
import logging
from typing import List, Union, Any

# filename изменить на свой путь к файлу с расширением .log
logging.basicConfig(
    filename="C:\PycharmProjects\pythonProject7\mylog.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s %(module)s %(levelname)s: %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)


def get_info_transactions_json(file_path: str) -> List[Any]:
    """
    возвращает список словарей с данными о финансовых транзакциях или пустой список
    :param file_path:
    :return:
    """

    data_empty_list: list = []

    if not os.path.exists(file_path):
        logging.warning(f"The file {file_path} does not exist!")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            operation = json.load(f)
            if len(operation) == 0 or type(operation) != list:
                logging.warning(f"The file {file_path} is empty!")
                return data_empty_list
            else:
                logging.debug(f"The file {file_path} is valid!")
                return operation
        except json.decoder.JSONDecodeError as e:
            logging.error(f"JSON encoding error: {e}")
            return data_empty_list


if __name__ == "__main__":
    data = get_info_transactions_json("C:\\\\PycharmProjects\\\\pythonProject7\\\\data\\\\operations.json")
    print(data)