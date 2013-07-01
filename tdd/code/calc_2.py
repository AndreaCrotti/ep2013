import unittest


from calc_1 import mysum, mysubstract


class TestCalculator(unittest.TestCase):
    def test_mysum(self):
        self.assertEqual(mysum(0, 0), 0)
        self.assertEqual(mysum(1, -1), 0)

    def test_mysub(self):
        self.assertEqual(mysubstract(1, 1), 0)


if __name__ == '__main__':
    unittest.main()
