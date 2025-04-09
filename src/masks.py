import logging

# filename изменить на свой путь к файлу с расширением .log
logging.basicConfig(
    filename="C:\PycharmProjects\pythonProject7\logs\masks.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s %(module)s %(levelname)s: %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)


def get_mask_card_number(number_card: str) -> str:
    """Функция которая принимает на вход номер карты и возвращает ее маску."""
    try:
        # logging.debug("The work has been successfully done.")
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    except Exception as e:
        # logging.error(f"Error in get_mask_card_number {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """Функция которая принимает номер аккаунта и возвращает его маску."""
    try:
        # logging.debug("The work has been successfully done.")
        return account_number[-4:]
    except Exception as e:
        # logging.error(f"Error in get_mask_account {e}")
        raise