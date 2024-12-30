import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("1596837868705199") == "1596 83** **** 5199"

# Тесты на ошибочный ввод номеров карт
@pytest.mark.parametrize(
    "input_card_error",
    [
        (""),
        ("7865432678"),
        ("288198247673765881982476"),
    ],
)

def test_get_mask_card_number_error(input_card_error):
    with pytest.raises(TypeError):
        get_mask_card_number(input_card_error)
#
# # тесты на правильность маскировки номеров счетов
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305")
    ]
)

def test_get_mask_account(card_number, expected):
    assert get_mask_account(card_number) == expected


def test_invalid_card_number():
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number("7365410843013587430521a")


