import os
import pytest
from unittest.mock import Mock, patch
import requests
from src.external_api import convert_to_rub

os.environ["EXCHANGE_API_KEY"] = "xAPR6VuBpicDFRYDqGGxDrvgKVdL93ya"

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

def test_convert_missing_amount():
    with pytest.raises(ValueError):
        convert_to_rub({'currency': 'USD'})

@patch('requests.get')
def test_api_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout()
    with pytest.raises(ValueError):
        convert_to_rub({'amount': 100, 'currency': 'USD'})

