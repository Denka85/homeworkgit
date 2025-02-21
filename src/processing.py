from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует операции по значению ключа 'state'.

    :param operations: Список операций, где каждая операция представлена словарём
                       с ключами (например, 'id', 'state', 'date', и т.д.).
    :param state: Значение поля 'state', по которому необходимо отфильтровать операции.
                  По умолчанию равняется 'EXECUTED'.
    :return: Новый список словарей, содержащий операции только с указанным 'state'.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате (ключ 'date') в порядке убывания или возрастания.

    :param operations: Список операций, где каждая операция представлена словарём
                       с ключом 'date' в формате ISO 8601 (например, '2019-07-03T18:35:29.512364').
    :param descending: Порядок сортировки. Если True (значение по умолчанию), сортировка идёт
                       по убыванию (самые поздние даты в начале). Если False, по возрастанию.
    :return: Новый список словарей, отсортированный по дате.
    """
    # Чтобы учесть точность времени, лучше дату преобразовать в datetime-объект.
    # В ISO 8601-формате (как '2019-07-03T18:35:29.512364') Python распознаёт строку через fromisoformat.
    sorted_operations = sorted(operations, key=lambda op: datetime.fromisoformat(op["date"]), reverse=descending)
    return sorted_operations
