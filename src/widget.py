from datetime import datetime


def mask_account_card(info: str) -> str:
    """Функция принимает информацию о карте и маскирует номер"""
    if not info:
        return info

    # Проверяем, является ли строка номером карты (16 цифр) или счетом (20 цифр)
    if info.isdigit() and len(info) == 16:
        # Маскируем номер карты
        return f"{info[:4]} {info[4:6]}** **** {info[-4:]}"
    elif info.isdigit() and len(info) == 20:
        # Маскируем номер счета
        return f"**{info[-4:]}"
    else:
        # Возвращаем исходную строку для некорректных данных
        return info


def get_date(input_date: str) -> str:
    """
    Преобразует строку с датой в формате ISO (YYYY-MM-DDTHH:MM:SS)
    в строку с датой в формате DD.MM.YYYY
    """
    try:
        # Пробуем разобрать полный ISO-формат с временем
        date_obj = datetime.fromisoformat(input_date)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        try:
            # Если не получилось, пробуем разобрать только дату (YYYY-MM-DD)
            date_obj = datetime.strptime(input_date, "%Y-%m-%d")
            return date_obj.strftime("%d.%m.%Y")
        except ValueError:
            raise ValueError("Некорректный формат даты. Ожидается YYYY-MM-DD или ISO-формат")
