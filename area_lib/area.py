from abc import ABC, abstractmethod
import math

from typing import Union, Tuple

__all__ = ['Circle', 'Triangle', 'AnotherShape']


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Вычисляет площадь фигуры"""
        pass


class AnotherShape(Shape):
    """
    Фигура, выбирающая конкретный класс в зависимости от переданных аргументов:
    - один числовой аргумент — круг,
    - три числовых аргумента — треугольник,
    - иначе — исключение.
    """

    def __init__(self, *args: Union[int, float]):
        # Проверяем что все аргументы - числа
        if not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("Все параметры должны быть числами")

        args = tuple(float(x) for x in args)

        if len(args) == 1:
            self.item = Circle(args[0])
        elif len(args) == 3:
            self.item = Triangle(*args)
        else:
            raise ValueError("Неподдерживаемое количество параметров")

    def area(self) -> float:
        return self.item.area()


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2




class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Сумма любых двух сторон должна быть больше третьей")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        half_p = (self.a + self.b + self.c) / 2
        return math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))

    def is_right_triangle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)
