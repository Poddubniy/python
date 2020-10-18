"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} начала движение'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turned(self):
        return f'Машина {self.name} свернула'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} равна {self.speed}\n'


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Сбавьте скорость, вы едите больше 60 \n'
        else:
            return f'Ваша скорость в пределах допустимой нормы \n'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Сбавьте скорость, вы едите больше 40 \n'
        else:
            return f'Ваша скорость в пределах допустимой нормы \n'


class PoliceCar(Car):
    pass


mustang = SportCar(250, 'жёлтый', 'Mustang')
matis = TownCar(37, 'серый', 'Matis')
truck = WorkCar(65, 'белый', 'Truck')
ford = PoliceCar(133, 'чёрный', 'Ford', True)

print(f'{mustang.speed}')
print(f'{matis.color}')
print(f'{truck.name}')
print(f'{ford.is_police}\n')

print(f'{mustang.go()}')
print(f'{matis.stop()}')
print(f'{truck.turned()}')
print(f'{ford.show_speed()}')

print(f'{matis.show_speed()}')
print(f'{truck.show_speed()}')
