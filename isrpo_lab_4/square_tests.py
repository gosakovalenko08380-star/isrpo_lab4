import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_int(self):
        self.assertEqual(area(5), 25)

    def test_area_negative_int(self):
        self.assertEqual(area(-3), 9)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_int(self):
        self.assertEqual(perimeter(4), 16)

    def test_perimeter_negative_int(self):
        self.assertEqual(perimeter(-2), -8)


if __name__ == '__main__':
    unittest.main()

