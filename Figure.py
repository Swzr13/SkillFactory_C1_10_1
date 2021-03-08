class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return (f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})')

rectangle_1 = Rectangle(x=5, y=10, width=50, height=100)
print(rectangle_1)