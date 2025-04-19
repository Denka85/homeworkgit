
from unittest.mock import mock_open, patch

from src.utils import load_transactions



def test_load_transactions_empty_list():
    """Тест пустого списка"""
    test_data = '[]'
    with patch("builtins.open", mock_open(read_data=test_data)):
        result = load_transactions("dummy.json")
        assert result == []


def test_load_transactions_empty_file():
    """Тест пустого файла"""
    test_data = ''
    with patch("builtins.open", mock_open(read_data=test_data)):
        result = load_transactions("dummy.json")
        assert result == []


def test_load_transactions_invalid_json():
    """Тест невалидного JSON"""
    test_data = '{"id": 1}'  # Это словарь, а не список
    with patch("builtins.open", mock_open(read_data=test_data)):
        result = load_transactions("dummy.json")
        assert result == []


def test_load_transactions_file_not_found():
    """Тест отсутствия файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions("nonexistent.json")
        assert result == []