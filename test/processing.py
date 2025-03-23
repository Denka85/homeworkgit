from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:

    return [op for op in operations if op.get('state') == state]


def sort_by_date(operations: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:

    sorted_operations = sorted(
        operations,
        key=lambda op: datetime.fromisoformat(op['date']),
        reverse=descending
    )
    return sorted_operations