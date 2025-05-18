import pytest
import functools
import logging
import sys


def log(func=None, *, filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__  # Fixed: use __name__ instead of .name
            # Настраиваем логирование
            logger = logging.getLogger(func_name)
            logger.setLevel(logging.INFO)

            # Удаляем все существующие обработчики, чтобы избежать дублирования
            logger.handlers = []

            # Если filename указан, пишем в файл
            if filename:
                file_handler = logging.FileHandler(filename)
                file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
                logger.addHandler(file_handler)
            else:
                # Если filename не указан, пишем в консоль
                console_handler = logging.StreamHandler(sys.stdout)
                console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
                logger.addHandler(console_handler)

            logger.info(f"Функция '{func_name}' начата")

            try:
                result = func(*args, **kwargs)
                logger.info(f"Функция '{func_name}' окончена, результат: {result}")
                return result
            except Exception as e:
                # Настраиваем логирование для ошибок
                logger.setLevel(logging.ERROR)
                logger.error(
                    f"Ошибка в функции '{func_name}'. Ошибка: {type(e).__name__}. Вводные данные: {args}, {kwargs}"
                )
                raise
            finally:
                # Удаляем обработчик, чтобы не мешать другим тестам
                logger.handlers = []

        return wrapper

    if func is not None:
        # Case when @log is used without parentheses
        return decorator(func)
    else:
        # Case when @log() or @log(filename=...) is used
        return decorator


def test_log_console_ok(capsys):
    """Проверяет тест на правильность вывода в консоль с учетом отсутствия ошибки"""

    @log
    def add(x, y):
        """Функция, которая суммирует два числа"""
        return x + y

    assert add(2, 3) == 5
    output = capsys.readouterr()
    captured = output.out
    assert "Функция 'add' начата" in captured


def test_log_console_error(capsys):
    """Проверяет тест на правильность вывода в консоль с учетом наличия ошибки"""

    @log
    def divide(x, y):
        """Функция, которая делит два числа"""
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    captured = capsys.readouterr()
    output = captured.out
    assert "Функция 'divide' начата" in output