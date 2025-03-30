import pytest
import os
from src.decorators import log

@log()
def divide(x, y):
    return x / y

@log('test_log.txt')
def divide_with_error(x, y):
    return x / y

def test_divide():
    assert divide(10, 2) == 5  # Проверка возврата результата
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)  # Проверка логирования ошибки

def test_divide_with_error():
    with pytest.raises(ZeroDivisionError):
        divide_with_error(10, 0)
    assert os.path.exists('test_log.txt')
