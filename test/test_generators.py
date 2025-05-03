import logging
from functools import wraps


def log(func=None, *, filename=None):
    """
    Упрощённый декоратор для логирования вызовов функций

    Параметры:
    ----------
    func : function, optional
        Функция для декорирования (используется при вызове без скобок)
    filename : str, optional
        Имя файла для записи логов. По умолчанию - вывод в консоль

    Примеры использования:
    ---------------------
    >>> @log
    ... def add(a, b):
    ...     return a + b

    >>> @log(filename='operations.log')
    ... def sub(a, b):
    ...     return a - b
    """
    # Настройка базового логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=filename
    )

    # Для случая @log без скобок
    if func is not None:
        return _make_wrapper(func)

    # Для случая @log(...) с параметрами
    return _make_wrapper


def _make_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.info(f'Вызов {func.__name__} с аргументами: {args}, {kwargs}')
            result = func(*args, **kwargs)
            logging.info(f'Функция {func.__name__} вернула: {result}')
            return result
        except Exception as e:
            logging.error(f'Ошибка в {func.__name__}: {str(e)}', exc_info=True)
            raise

    return wrapper