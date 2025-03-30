import json
import os
from typing import List, Dict
import requests
from dotenv import load_dotenv

def load_transactions(file_path: str) -> List[Dict]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


load_dotenv()  # Загружает переменные из .env


def convert_currency(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли."""
    currency = transaction.get('currency', 'RUB')
    amount = transaction.get('amount', 0.0)

    if currency == 'RUB':
        return amount

    api_key = os.getenv('EXCHANGE_API_KEY')
    url = f"https://api.exchangerate-api.com/v4/latest/{currency}?api_key={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        rate = response.json()['rates']['RUB']
        return amount * rate
    except (requests.RequestException, KeyError):
        return 0.0  # или выбросить исключение