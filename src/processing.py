from datetime import datetime

def filter_by_state(data: list[dict], state: str) -> list[dict]:
    return [item for item in data if item.get("state") == state]

def sort_by_date(data: list[dict], reverse: bool = False) -> list[dict]:
    # Проверка наличия ключа 'date' во всех элементах
    if any("date" not in item for item in data):
        raise KeyError("Key 'date' is missing in one or more items")

    # Преобразование строк в даты с обработкой ошибок
    try:
        sorted_data = sorted(
            data,
            key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"),
            reverse=reverse,
        )
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")

    return sorted_data