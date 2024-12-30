def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        raise TypeError


def get_mask_account(ass_number: str) -> str | None:
    """Функция маскировки номера счета"""
    if ass_number.isdigit() and len(ass_number) == 20:
        return f"{"*" * 2}{ass_number[-4::]}"
    else:
        raise TypeError


#print(get_mask_card_number("7000792289606361"))
#print(get_mask_account("73654108430135874305"))
