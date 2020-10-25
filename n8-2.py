"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_division = input("Введите числа для деления (Пример - 180/20): ")

try:
    inp_division = inp_division.split("/")
    if int(inp_division[1]) == 0:
        raise OwnError("Упс! На ноль делить нельзя!")
    int(inp_division[0])
    int(inp_division[1])
except ValueError:
    print("Вы ошиблись и указали вместо числа, что-то другое!")
except OwnError as err:
    print(err)
else:
    print(f"Отлично! результат деления: {int(inp_division[0]) / int(inp_division[1])}")
