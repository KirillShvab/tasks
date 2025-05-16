import unittest
import math
from area_lib import Circle, Triangle


class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        circle = Circle(1)
        expected = math.pi
        self.assertAlmostEqual(circle.area(), expected, places=5)

    def test_area_zero_radius(self):
        circle = Circle(0)
        self.assertEqual(circle.area(), 0)

    def test_area_large_radius(self):
        circle = Circle(100)
        expected = math.pi * 100 ** 2
        self.assertAlmostEqual(circle.area(), expected, places=5)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-5)



if __name__ == '__main__':
    unittest.main()
