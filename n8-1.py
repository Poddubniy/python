"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def split(cls, date):
        date_list = date.split(".")
        for i in range(0, 3):
            date_list[i] = int(date_list[i])
        print(date_list)

    @staticmethod
    def validation(date):
        try:
            date_list = date.split(".")
            for i in range(0, 3):
                date_list[i] = int(date_list[i])
        except ValueError:
            print("Вы ошиблись в указании даты!")


birthday = Date("08.04.1992")
print(birthday.date)
Date.split("08.04.1992")
Date.validation("o8.04.1992")
birthday.validation("08.04.1992")
