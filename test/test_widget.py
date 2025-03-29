import pytest
from src.widget import mask_account_card, get_date


# Параметризованные тесты для корректных данных
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # Тесты для номеров карт
        ("1234567812345678", "1234 56** **** 5678"),  # 16-значный номер карты
        ("1234123412341234", "1234 12** **** 1234"),  # Другой 16-значный номер карты
        ("1234567890123456", "1234 56** **** 3456"),  # Еще один 16-значный номер карты
        # Тесты для номеров счетов
        ("12345678901234567890", "**7890"),  # 20-значный номер счета
        ("98765432109876543210", "**3210"),  # Другой 20-значный номер счета
        ("11112222333344445555", "**5555"),  # Еще один 20-значный номер счета
    ],
)
def test_mask_account_card_valid(input_data, expected_output):
    # Проверяем, что функция возвращает правильный результат для корректных данных
    assert mask_account_card(input_data) == expected_output


# Параметризованные тесты для некорректных данных
@pytest.mark.parametrize(
    "input_data",
    [
        "1234",  # Слишком короткий номер
        "1234567812345678abcd",  # Некорректные символы
        "",  # Пустая строка
        "1234567890123456789",  # 19 символов (ни карта, ни счет)
        "123456789012345678901",  # 21 символ (ни карта, ни счет)
    ],
)
def test_mask_account_card_invalid(input_data):
    # Проверяем, что функция корректно обрабатывает некорректные данные
    result = mask_account_card(input_data)
    # Ожидаем, что функция либо вернет исходную строку, либо выбросит исключение
    assert result == input_data or isinstance(result, ValueError)


@pytest.mark.parametrize(
    "input_date",
    [
        "2023/10/05",  # Нестандартный разделитель
        "05-10-2023",  # Обратный формат
        "2023-13-01",  # Некорректный месяц
        "No date here",  # Отсутствие даты
        "",  # Пустая строка
    ],
)
def test_get_date_invalid(input_date):
    # Проверяем, что функция выбрасывает ValueError для некорректных данных
    with pytest.raises(ValueError):
        get_date(input_date)

    # Тесты для граничных случаев
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            ("123456781234567", "123456781234567"),  # 15 символов (не карта и не счет)
            ("12345678123456789", "12345678123456789"),  # 17 символов (не карта и не счет)
            ("123456789012345678901234567890", "123456789012345678901234567890"),  # 30 символов (не карта и не счет)
        ],
    )
    def test_mask_account_card_edge_cases(input_data, expected_output):
        assert mask_account_card(input_data) == expected_output

    # Тесты для строк с пробелами и нечисловыми символами
    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            ("1234 5678 1234 5678", "1234 5678 1234 5678"),  # Пробелы в номере карты
            ("1234-5678-1234-5678", "1234-5678-1234-5678"),  # Дефисы в номере карты
            ("1234abcd5678efgh", "1234abcd5678efgh"),  # Буквы в номере карты
        ],
    )
    def test_mask_account_card_invalid_characters(input_data, expected_output):
        assert mask_account_card(input_data) == expected_output
