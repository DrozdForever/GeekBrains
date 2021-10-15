class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f'{itm:03}' for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерностей матриц'


a = [[1, 2, 3], [6, 5, 4], [8, 7, 9], [1, 1, 1, 1]]
b = [[9, 87, 0], [56, 6, 6], [10, 15, 20], [2, 2, 2, 2]]

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
matrix = matrix_1 + matrix_2
print(matrix)
