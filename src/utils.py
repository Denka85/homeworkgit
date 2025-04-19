import json
import os
from typing import List, Dict, Any


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON файла.

    Args:
        file_path: Путь к JSON файлу

    Returns:
        Список словарей с транзакциями или пустой список при ошибках
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Явно проверяем, что данные - это список
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        # Логирование ошибки может быть полезно для отладки
        print(f"Error loading transactions from {file_path}: {str(e)}")
        return []