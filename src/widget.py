def mask_account_card(info: str) -> str:
    """Функция принимает информацию о карте и маскирует номер"""
    # Объединяем инфо о карте в список
    parts = info.split()
    # Создаем строку без номера используя срез
    card_type = " ".join(parts[:-1])
    # Создаем номер
    number = parts[-1]

    if "Счет" in card_type:
        masked_number = f"{card_type} **{number[-4:]}"

    else:
        masked_number = f"{card_type} {number[:4]} {number[4:6]}** **** {number[-4:]}"

    return masked_number


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    new_date = date[0:10].split("-")
    return ".".join(new_date[::-1])
