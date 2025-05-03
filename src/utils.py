import json
import os
import logging
from typing import List, Dict, Any
from pathlib import Path

# Получаем путь к директории текущего файла

current_dir = Path(__file__).parent.parent
log_dir = current_dir / "logs"
log_dir.mkdir(exist_ok=True)

# Настройка логера
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)  # Ловит все сообщения от DEBUG и выше

# Хендлер для записи в файл
log_file = log_dir / "utils.log"
file_handler = logging.FileHandler(
    log_file,
    encoding='utf-8',
    mode='w'  # 'w' - перезапись
              # 'a' - дополнение
)
file_handler.setLevel(logging.DEBUG)

# Форматтер
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'  # Исправлено на 4-значный год
)
file_handler.setFormatter(formatter)

# Добавляем хэндлер к логеру
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON файла.

    Args:
        file_path: Путь к JSON файлу

    Returns:
        Список словарей с транзакций или пустой список при ошибках
    """
    try:
        # Проверяем существование файла
        if not os.path.exists(file_path):
            logger.error(f"Файл не найден: {file_path}")
            return []

        # Проверяем что это файл, а не директория
        if not os.path.isfile(file_path):
            logger.error(f"Указанный путь ведёт к директории: {file_path}")
            return []

        with open(file_path, 'r', encoding='utf-8') as f:
            logger.debug(f"Загрузка данных из файла: {file_path}")
            data = json.load(f)

            # Проверяем что данные - это список
            if not isinstance(data, list):
                logger.warning(f"Файл {file_path} не содержит JSON-массив")
                return []

            logger.info(f"Успешно загружено {len(data)} транзакций")
            return data

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {str(e)}", exc_info=True)
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при загрузке {file_path}: {str(e)}", exc_info=True)
        return []