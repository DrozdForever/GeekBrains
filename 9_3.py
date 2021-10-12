class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{sum(self._income.values())}$')


worker = Position('Johnny ', 'Silverhand', 'Rockstar', 100000, 50000)
worker.get_full_name()
worker.get_total_income()
