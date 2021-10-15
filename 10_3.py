class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['🦠' * rows for _ in range(self.nums // rows)]) + '\n' + '🦠' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
             else 'Ячеек в первой клетке меньше, чем во второй, вычитание невозможно!'

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        return Cell(self.nums // other.nums)


cell_1 = Cell(20)
cell_2 = Cell(25)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_2 * cell_1)
print(cell_2 // cell_1)
print(cell_2.make_order(5))
print(cell_1.make_order(2))
