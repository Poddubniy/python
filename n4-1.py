"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
   В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
   Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def wages():
    script_name, hours, rate, prize = argv
    hours, rate, prize = int(hours), int(rate), int(prize)
    staff_salaries = (hours * rate) + prize
    return staff_salaries


print(wages())
