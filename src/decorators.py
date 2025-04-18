from functools import wraps
from typing import Callable, Any, Optional
from time import time
import logging


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования функции, аргументов, результатов """

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            logging.basicConfig(
                filename=filename,
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
            )
            logging.info(f"Функция '{func_name}' начата")
            try:
                result = func(*args, **kwargs)
                logging.info(f"Функция '{func_name}' окончена, результат: {result}")
                return result
            except Exception as error:
                logging.basicConfig(
                    filename=filename,
                    level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                )
                logging.error(
                    f"Ошибка в функции '{func_name}' Ошибка: {type(error).__name__}. Вводные данные: {args}, {kwargs}"
                )
                raise
        return wrapper

    return decorator


def printing(func):
    """Фиксирует начало и конец работы функции"""

    def wrapper(*args, **kwargs):
        print(f"Function {func} started")
        result = func(*args, **kwargs)
        print(f"Function {func} finished")
        return result

    return wrapper


def timer(func):
    """Фиксирует время, которое затратит функция на выполнение"""

    def wrapper(*args, **kwargs):
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f"Time for work: {time_2 - time_1}")
        return result

    return wrapper


@printing
@timer
def my_function():
    for i in range(100000000):
        continue