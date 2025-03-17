from datetime import datetime

import pytest

from processing import filter_by_state, sort_by_date


@pytest.fixture
def test_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15"},
        {"id": 2, "state": "PENDING", "date": "2024-01-14"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-16"},
        {"id": 4, "state": "CANCELED", "date": "2024-01-13"},
        {"id": 5, "date": "2024-01-12"},  # Нет ключа 'state'
        {"id": 6, "state": "EXECUTED", "date": "invalid_date"},  # Неправильный формат
        {"id": 7, "state": "EXECUTED", "date": "2024-01-17"},  # Корректная дата
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 7]),  # Стандартный случай
        ("PENDING", [2]),  # Один элемент
        ("CANCELED", [4]),  # Другой статус
        ("UNKNOWN", []),  # Нет совпадений
    ],
)
def test_filter_by_state(test_data, state, expected_ids):
    result = filter_by_state(test_data, state)
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_state_missing_key(test_data):
    # Элементы без ключа 'state' игнорируются
    result = filter_by_state(test_data, "EXECUTED")
    assert 5 not in [item["id"] for item in result]


@pytest.mark.parametrize(
    "reverse, expected_order",
    [
        (False, [5, 4, 2, 1, 3, 7]),  # По возрастанию (самая ранняя дата первая)
        (True, [7, 3, 1, 2, 4, 5]),  # По убыванию (самая поздняя дата первая)
    ],
)
def test_sort_by_date_valid(test_data, reverse, expected_order):
    # Исключаем элемент с некорректной датой (id=6)
    valid_data = [item for item in test_data if item["id"] != 6]
    result = sort_by_date(valid_data, reverse=reverse)
    assert [item["id"] for item in result] == expected_order


def test_sort_by_date_invalid_format(test_data):
    # Проверка обработки невалидных дат
    with pytest.raises(ValueError):
        sort_by_date([test_data[5]])  # Элемент с date="invalid_date"


def test_sort_by_date_missing_key(test_data):
    # Элементы без ключа 'date' вызывают ошибку
    with pytest.raises(KeyError):
        sort_by_date([{"id": 8, "state": "EXECUTED"}])


def test_sort_by_date_stable_sorting():
    data = [
        {"id": 1, "date": "2024-01-15"},
        {"id": 2, "date": "2024-01-15"},
    ]
    result = sort_by_date(data)
    # Порядок элементов с одинаковой датой сохраняется
    assert [item["id"] for item in result] == [1, 2]
