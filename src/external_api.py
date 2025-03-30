import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными транзакции
    :return: Сумма в рублях (float)
    """
    currency = transaction.get('currency', 'RUB').upper()
    amount = float(transaction.get('amount', 0))

    if currency == 'RUB':
        return amount

    try:
        response = requests.get(
            API_URL,
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': os.getenv('EXCHANGE_API_KEY')},
            timeout=10
        )
        response.raise_for_status()
        rate = response.json()['rates']['RUB']
        return round(amount * rate, 2)
    except (requests.RequestException, KeyError):
        return 0.0