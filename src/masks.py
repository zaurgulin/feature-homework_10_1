import logging
import os

path_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils_log.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
#    filename=path_file,
    filename="../logs/masks_log.log",
    filemode="w",
    )
get_mask_card_number_logger = logging.getLogger()
get_mask_account_logger = logging.getLogger()

def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера карты"""
    get_mask_card_number_logger.info("Создаю маску номера карты")
    if card_number.isdigit():
        get_mask_card_number_logger.error("Неправильный номер карты")
        get_mask_card_number_logger.info("Маска номера карты создана")
    if len(card_number) != 16:
        raise ValueError("Неправильный номер карты")
    return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
#    else:
#        raise TypeError


def get_mask_account(ass_number: str) -> str | None:
    """Функция маскировки номера счета"""
    get_mask_account_logger.info("Создаю маску номера счета")
    if ass_number.isdigit():
        get_mask_account_logger.error("Неправильный номер счета")
        get_mask_account_logger.info("Маска номера счета создана")
    if len(ass_number) != 20:
        raise ValueError("Неправильный номер счета")
    return f"{"*" * 2}{ass_number[-4::]}"

#    else:
#        raise TypeError


#print(get_mask_card_number("7000792289606361"))
#print(get_mask_account("73654108430135874305"))