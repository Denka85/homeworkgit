import pytest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub


def test_convert_rub():
    """Тест для RUB (без конвертации)"""
    transaction = {'amount': 100.0, 'currency': 'RUB'}
    assert convert_to_rub(transaction) == 100.0


@patch('src.external_api.requests.get')
def test_convert_usd(mock_get):
    """Тест для USD с моком API"""
    # Настраиваем мок
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.5}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {'amount': 100.0, 'currency': 'USD'}
    result = convert_to_rub(transaction)

    assert result == 7550.0  # 100 * 75.5
    mock_get.assert_called_once()


@patch('src.external_api.requests.get')
def test_convert_eur(mock_get):
    """Тест для EUR с моком API"""
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 85.3}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {'amount': 50.0, 'currency': 'EUR'}
    result = convert_to_rub(transaction)

    assert result == 4265.0  # 50 * 85.3
    mock_get.assert_called_once()


def test_unsupported_currency():
    """Тест на неподдерживаемую валюту"""
    transaction = {'amount': 100.0, 'currency': 'GBP'}
    with pytest.raises(ValueError, match="Unsupported currency: GBP"):
        convert_to_rub(transaction)