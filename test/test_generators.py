from typing import Any, Dict, Generator, List

def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор номеров карт."""
    for i in range(start, end + 1):
        yield f"0000 0000 0000 {i:04d}"

def filter_by_currency(
    transactions: List[Dict[str, Any]],
    currency: str
) -> Generator[Dict[str, Any], None, None]:
    """Фильтрация транзакций по валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Generator[str, None, None]:
    """Генератор описаний транзакций."""
    for transaction in transactions:
        yield transaction["description"]