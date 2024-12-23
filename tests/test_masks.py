import pytest

from src.masks import get_mask_card_number, get_mask_account


# Тесты на правильность маскировки номеров карт
@pytest.mark.parametrize(
    "value, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("5999414228426353", "5999 41** **** 6353")
    ]
)

def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected

# Тесты на ошибочный ввод номеров карт
@pytest.mark.parametrize(
    "input_card_error",
    [
        "",
        None,
        "7865432678"
        "288198247673765881982476",
        "Visa",
        "Visa Classic",
        "Данные введены некорректно"
    ]
)

def test_get_mask_card_number_error(input_card_error):
    with pytest.raises(TypeError):
        get_mask_card_number(input_card_error)

# тесты на правильность маскировки номеров счетов
@pytest.mark.parametrize(
    "value, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305")
    ]
)

def test_get_mask_card_number(card_number):
    assert get_mask_card_number(*73654108430135874305*) == card_number


def test_invalid_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(7365410843013587430521)
    assert 'str (exc_info.value)' == "Номер карты должен состоять из 16 цифр"

