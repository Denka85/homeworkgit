import functools
import logging
import sys


def log(filename=None):
    # Настройка логирования
    logger = logging.getLogger('FunctionLogger')
    logger.setLevel(logging.DEBUG)

    # Создание обработчика
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Логируем входные параметры
                logger.info(f'Calling {func.__name__} with args: {args} and kwargs: {kwargs}')
                result = func(*args, **kwargs)
                # Логируем результат
                logger.info(f'{func.__name__} returned: {result}')
                return result
            except Exception as e:
                # Логируем ошибку
                logger.error(f'Error in {func.__name__}: {e}', exc_info=True)
                logger.error(f'Function {func.__name__} called with args: {args} and kwargs: {kwargs}')
                raise

        return wrapper

    return decorator