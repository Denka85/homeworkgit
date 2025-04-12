import os
import requests
from dotenv import load_dotenv
from typing import Dict

load_dotenv()


def convert_to_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли

    Args:
        transaction: словарь с данными транзакции (должен содержать amount и currency)

    Returns:
        Сумма в рублях (float)

    Raises:
        ValueError: если валюта не поддерживается
        ConnectionError: если проблемы с API
    """
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB').upper()

    if currency == 'RUB':
        return float(amount)

    if currency not in ('USD', 'EUR'):
        raise ValueError(f"Unsupported currency: {currency}")

    api_key = os.getenv('EXCHANGE_RATE_API_KEY')
    api_url = os.getenv('EXCHANGE_RATE_API_URL')

    if not api_key or not api_url:
        raise ValueError("API credentials not configured")

    try:
        response = requests.get(
            api_url,
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': api_key}
        )
        response.raise_for_status()

        rate = response.json()['rates']['RUB']
        return float(amount) * rate

    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"API request failed: {str(e)}")
    except (KeyError, ValueError) as e:
        raise ValueError(f"Invalid API response: {str(e)}")