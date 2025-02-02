import pytest

from src.widget import mask_account_card, get_date

# Тесты на правильность общей маскировки номера и счета
@pytest.mark.parametrize("number_card, expected",
    [
        ("Maestro 1212232334344545", "Maestro 1212 23** **** 4545"),
        ("Счет 73654108430135874305", "Счет **4305")])


def test_mask_account_card(number_card, expected):
    assert mask_account_card(number_card) == expected


# def test_get_mask_invalid_account_card():
#     with pytest.raises(TypeError):
#         mask_account_card('Счет 73654108430135874305')


@pytest.fixture
def date():
    return ['2024-10-13T02:26:18.671407', '2024-12-31']


@pytest.mark.parametrize("date, expected", [
                             ('2024-10-13T02:26:18.671407', '13.10.2024'),
                             ('2024-12-31', '31.12.2024')])

def test_get_date(date,expected):
    assert get_date(date) == expected
