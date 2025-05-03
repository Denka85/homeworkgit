import logging
from pathlib import Path


# Получаем путь к директории текущего файла
current_dir = Path(__file__).parent.parent
log_dir = current_dir / "logs"
log_dir.mkdir(exist_ok=True)

# Настройка логера
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)  # Ловит все сообщения от DEBUG и выше

# Хендлер для записи в файл
log_file = log_dir / "masks.log"
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

def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маскированный номер карты в формате: XXXX XX** **** XXXX.

    Пример:
    Вход: 7000792289606361
    Выход: "7000 79** **** 6361"

    :param card_number: Номер банковской карты в виде целого числа (16 цифр).
    :return: Маскированный номер карты в виде строки.
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        print("Номер карты должен содержать ровно 16 цифр.")

    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked_card


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маскированный номер счёта в формате: **XXXX.

    Пример:
    Вход: 73654108430135874305
    Выход: "**4305"

    :param account_number: Номер счёта в виде целого числа.
    :return: Маскированный номер счёта в виде строки.
    """
    account_str = str(account_number)
    if len(account_str) < 4:
        print("Номер счёта должен содержать минимум 4 цифры.")

    masked_account = f"**{account_str[-4:]}"
    return masked_account

# Пример использования
def mask_card_number(card_number: str) -> str:
    try:
        logger.debug(f"Маскирование карты: {card_number}")
        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Успешно замаскировано: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка маскирования: {e}")
        raise