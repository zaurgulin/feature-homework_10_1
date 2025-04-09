from src.decorators import log


@log(filename='mylog.txt')
def my_function(x, y):
    """Функция, которая суммирует два числа"""
    return x + y


def test_log_console_ok(capsys):
    """Проверяет тест на правильность вывода в консоль с учетом отсутствия ошибки"""
    my_function(2, 3)
    output = capsys.readouterr()
    assert output.out == "my_function ok\n"


def test_log_console_error(capsys):
    """Проверяет тест на правильность вывода в консоль с учетом наличия ошибки"""
    my_function(2, "3")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (2, '3'), {}\n"