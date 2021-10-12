class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Car: {name}, color: {color}.')

    def go(self):
        print(f'{self.name} сar went')

    def stop(self):
        print(f'{self.name} сar stopped')

    def turn(self, direction):
        print(f'{self.name} сar turned {direction}')

    def show_speed(self):
        print(f'{self.name} сar speed {self.speed}')


class TownCar(Car):
    """City car"""

    def show_speed(self):
        print(f'{self.name} сar speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed())


class WorkCar(Car):
    """Cargo truck"""

    def show_speed(self):
        print(f'Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed())


class PoliceCar(Car):
    """Police car"""

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)
        print("It's a police car!\n")


class SportCar(Car):
    """Sports car"""


police_car = PoliceCar('Patriot', 'white', 80)
work_car = WorkCar('КаМаз', 'orange', 60)
town_car = TownCar('Kia Rio', 'gray', 70)
sport_car = SportCar('Porsche 911', 'red', 120)
list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    print()
    i.go()
    i.show_speed()
    i.turn('right')
    i.stop()
