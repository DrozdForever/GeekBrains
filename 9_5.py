class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Selected tool: {self.title}. Start drawing')


class Pen(Stationery):
    def draw(self):
        print(f'Selected tool: {self.title}. Start drawing')


class Pencil(Stationery):
    def draw(self):
        print(f'Selected tool: {self.title}. Start drawing')


class Handle(Stationery):
    def draw(self):
        print(f'Selected tool: {self.title}. Start drawing')


stationery = Stationery('spray')
handle = Handle('handle')
pen = Pen('pen')
pencil = Pencil('pencil')

for i in [stationery, handle, pen, pencil]:
    i.draw()
