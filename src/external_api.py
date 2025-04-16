import os
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли"""
    currency = transaction['currency'].upper()
    amount = transaction['amount']

    if currency == 'RUB':
        return amount

    if currency not in ('USD', 'EUR'):
        raise ValueError(f"Unsupported currency: {currency}")

    # Получаем курс от API
    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/latest?base={currency}",
        headers={"apikey": os.getenv("API_KEY")}
    )
    response.raise_for_status()

    return amount * response.json()['rates']['RUB']