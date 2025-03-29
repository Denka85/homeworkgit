from typing import Iterator, List, Dict
import functools
from datetime import datetime


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор

    Args:
        transactions: Список словарей с транзакциями
        currency: Код валюты для фильтрации (например, "USD")

    Yields:
        Словари транзакций в указанной валюте
    """
    for transaction in transactions:
        if isinstance(transaction, dict):
            operation_amount = transaction.get('operationAmount', {})
            if isinstance(operation_amount, dict):
                currency_info = operation_amount.get('currency', {})
                if isinstance(currency_info, dict) and currency_info.get('code') == currency:
                    yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор описаний транзакций

    Args:
        transactions: Список словарей с транзакциями

    Yields:
        Описание каждой транзакции (str или None если нет описания)
    """
    for transaction in transactions:
        if isinstance(transaction, dict):
            yield transaction.get('description')


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в заданном диапазоне

    Args:
        start: Начальное значение (включительно)
        stop: Конечное значение (не включается)

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"
    """
    for number in range(start, stop):
        card_str = f"{number:016d}"
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Формируем строку с параметрами
            params = []
            if args:
                params.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                params.append(', '.join(f"{key}={repr(value)}" for key, value in kwargs.items()))
            params_str = ', '.join(params)

            try:
                # Вызываем функцию
                result = func(*args, **kwargs)

                # Формируем сообщение для логирования
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message = f"{timestamp} - {func.__name__}({params_str}) -> {repr(result)}\n"

                # Логируем результат
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(log_message)
                else:
                    print(log_message, end='')

                return result
            except Exception as e:
                # Формируем сообщение об ошибке
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                error_message = f"{timestamp} - {func.__name__}({params_str}) -> ERROR: {str(e)}\n"

                # Логируем ошибку
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(error_message)
                else:
                    print(error_message, end='')

                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator
