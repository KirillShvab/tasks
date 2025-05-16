import unittest
import math
from area_lib import Triangle

class TestTriangle(unittest.TestCase):
    def test_area_valid_triangle(self):
        tri = Triangle(3, 4, 5)
        self.assertAlmostEqual(tri.area(), 6.0, places=5)

    def test_area_equilateral_triangle(self):
        side = 6
        tri = Triangle(side, side, side)
        expected = (math.sqrt(3) / 4) * side ** 2
        self.assertAlmostEqual(tri.area(), expected, places=5)

    def test_zero_or_negative_sides_raise(self):
        with self.assertRaises(ValueError):
            Triangle(0, 4, 5)
        with self.assertRaises(ValueError):
            Triangle(-1, 4, 5)

    def test_invalid_triangle_sides_raise(self):
        # Сумма двух сторон меньше или равна третьей
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)
        with self.assertRaises(ValueError):
            Triangle(5, 1, 1)


if __name__ == '__main__':
    unittest.main()
