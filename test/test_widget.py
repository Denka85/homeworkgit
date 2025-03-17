import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def test_accounts_and_cards():
    return [
        {"input": "Счет 12345678901234567890", "expected": "Счет **7890"},
        {"input": "Visa Platinum 1234567890123456", "expected": "Visa Platinum 1234 56** **** 3456"},
        {"input": "Maestro 1234567890123456", "expected": "Maestro 1234 56** **** 3456"},
        {"input": "Счет 98765432109876543210", "expected": "Счет **3210"},
        {"input": "Счет 123", "expected": "Неверный номер счета"},
        {"input": "Visa 123456789012345", "expected": "Неверный номер карты"},
        {"input": "Invalid Input", "expected": "Неверный формат данных"},
        {"input": "", "expected": "Неверный формат данных"},
    ]


@pytest.fixture
def test_dates():
    return [
        {"input": "2024-01-15T12:34:56.789", "expected": "15.01.2024"},
        {"input": "2023-12-31T23:59:59.999", "expected": "31.12.2023"},
        {"input": "2022-02-28T00:00:00.000", "expected": "28.02.2022"},
        {"input": "2024-01-15", "expected": "Неверный формат даты"},
        {"input": "invalid-date", "expected": "Неверный формат даты"},
        {"input": "", "expected": "Неверный формат даты"},
    ]


@pytest.mark.parametrize("data", test_accounts_and_cards())
def test_mask_account_card(data):
    result = mask_account_card(data["input"])
    assert result == data["expected"], f"Ожидалось: {data['expected']}, Получено: {result}"


@pytest.mark.parametrize("data", test_dates())
def test_get_date(data):
    result = get_date(data["input"])
    assert result == data["expected"], f"Ожидалось: {data['expected']}, Получено: {result}"
