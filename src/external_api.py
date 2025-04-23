import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "https://api.apilayer.com/exchangerates_data"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """Convert transaction amount to RUB using current exchange rates."""
    currency = transaction.get('operationAmount', {}).get('currency', {}).get('code', 'RUB').upper()
    try:
        amount = float(transaction['operationAmount']['amount'])
    except (KeyError, ValueError):
        raise ValueError("Invalid transaction amount")

    if currency == 'RUB':
        return amount

    if currency not in ('USD', 'EUR'):
        raise ValueError(f"Unsupported currency: {currency}")

    api_key = os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        raise ValueError("API key not configured")

    try:
        response = requests.get(
            f"{API_BASE_URL}/latest?base={currency}",
            headers={"apikey": api_key},
            timeout=10
        )
        response.raise_for_status()
        rate = response.json()['rates']['RUB']
        return round(amount * rate, 2)
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {str(e)}")