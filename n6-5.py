"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Выбрана {self.title}. (Метод Pen)'


class Pencil(Stationery):
    def draw(self):
        return f'Выбран {self.title}. (Метод Pencil)'


class Handle(Stationery):
    def draw(self):
        return f'Выбран {self.title}. (Метод Handle)'


stationery = Stationery('Концелярия')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

print(f'{stationery.draw()}')
print(f'{pen.draw()}')
print(f'{pencil.draw()}')
print(f'{handle.draw()}')
