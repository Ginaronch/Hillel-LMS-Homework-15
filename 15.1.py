from exeptions import WrongRectangle

class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        if width <= 0:
            raise ValueError("Значение ширины должно быть больше нуля")
        elif height <= 0:
            raise ValueError("Значение длины должно быть больше нуля")
        elif width == height:
            raise WrongRectangle("Длина и высота прямоугольника не могут быть равны")

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Ожидается объект типа Прямоугольник\Rectangle")
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Действие можно выполнить только к Прямоугольникам")
        total_area = self.get_square() + other.get_square()
        new_width = self.width
        new_height = total_area / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError("Умножать можно только на число")
        if n <= 0:
            raise ValueError("Множитель должен бть позитивным числом")
        new_area = int(self.get_square() * n)
        width = new_area // 2
        height = new_area // width
        return Rectangle(width, height)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height}) = {self.get_square()}"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
try:
    r6 = Rectangle(5,5)
except WrongRectangle as e:
    print(e)
r5 = Rectangle(0,8)