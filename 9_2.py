class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def mass(self, weight=25, thickness=0.05):
        print(f'{self._length} m * {self._width} m * {weight} kg * {thickness} m = ' \
              f'{self._length * self._length * weight * thickness} t')


road = Road(50, 10000)
road.mass()
