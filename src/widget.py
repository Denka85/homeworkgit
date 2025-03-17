from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа входной строки.

    :param input_string: Строка, содержащая тип и номер карты или счета.
    :return: Строка с замаскированным номером.
    """
    if "Счет" in input_string:
        return get_mask_account(int(input_string.split()[-1]))
    else:
        return get_mask_card_number(int(input_string.split()[-1]))


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате "2024-03-11T02:26:18.671407"
    в формат "ДД.ММ.ГГГГ".

    :param date_string: Строка с датой
    в формате "2024-03-11T02:26:18.671407".
    :return: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    return date_object.strftime("%d.%m.%Y")
