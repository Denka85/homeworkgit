import functools
import logging
import sys
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar('F', bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """Декоратор для логирования."""
    logger = logging.getLogger('FunctionLogger')
    logger.setLevel(logging.DEBUG)

    # Очистка предыдущих обработчиков
    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.FileHandler(filename) if filename else logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logger.info(f'Calling {func.__name__} with args: {args} and kwargs: {kwargs}')
                result = func(*args, **kwargs)
                logger.info(f'{func.__name__} returned: {result}')
                return result
            except Exception as e:
                logger.error(f'Error in {func.__name__}: {e}', exc_info=True)
                logger.error(f'Function {func.__name__} called with args: {args} and kwargs: {kwargs}')
                raise

        return cast(F, wrapper)

    return decorator