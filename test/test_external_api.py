import os
import pytest
from unittest.mock import Mock, patch
from src.external_api import convert_to_rub

os.environ["EXCHANGE_API_KEY"] = "xAPR6VuBpicDFRYDqGGxDrvgKVdL93ya"


def test_convert_rub_to_rub():
    """Тест конвертации RUB в RUB (должен вернуть ту же сумму)"""
    transaction = {
        'operationAmount': {
            'amount': '100.00',
            'currency': {'code': 'RUB'}
        }
    }
    assert convert_to_rub(transaction) == 100.00


def test_convert_usd_to_rub_success():
    """Тест успешной конвертации USD в RUB"""
    transaction = {
        'operationAmount': {
            'amount': '10.00',
            'currency': {'code': 'USD'}
        }
    }

    # Мокаем ответ API с курсом 75.5 RUB за 1 USD
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.5}}
    mock_response.raise_for_status.return_value = None

    with patch('requests.get', return_value=mock_response) as mock_get:
        result = convert_to_rub(transaction)
        assert result == 755.0  # 10 * 75.5
        mock_get.assert_called_once()


def test_convert_eur_to_rub_success():
    """Тест успешной конвертации EUR в RUB"""
    transaction = {
        'operationAmount': {
            'amount': '5.00',
            'currency': {'code': 'EUR'}
        }
    }

    # Мокаем ответ API с курсом 85.3 RUB за 1 EUR
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 85.3}}
    mock_response.raise_for_status.return_value = None

    with patch('requests.get', return_value=mock_response) as mock_get:
        result = convert_to_rub(transaction)
        assert result == 426.5  # 5 * 85.3
        mock_get.assert_called_once()


def test_invalid_transaction_structure():
    """Тест с неверной структурой транзакции"""
    # Неправильная структура - operationAmount как число
    transaction = {'operationAmount': 100.0, 'currency': 'RUB'}
    with pytest.raises(AttributeError):
        convert_to_rub(transaction)

    # Неправильная структура - нет вложенности currency
    transaction = {
        'operationAmount': {
            'amount': '100.00',
            'currency': 'RUB'
        }
    }
    with pytest.raises(AttributeError):
        convert_to_rub(transaction)
