from mypy.types import names

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(nums: str) -> str | None:
    """Функция общей маскировки корты и счета"""
    if "Счет" in nums:
        name = nums.split()[0]
        account = nums.split()[1]
        return name + ' ' + get_mask_account(account)
    else:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))


def get_date(date: str) -> str | None:
    """Функция преобразования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date("2024-10-13T02:26:18.671407"))
