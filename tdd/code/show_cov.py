import unittest


def smart_division(a, b):
    """Run a 'smart' division
    """
    if b == 0:
        raise Exception("Can not divide by 0")

    res = a / b
    back_res = res * b

    if back_res != a:
        return a / float(b)
    else:
        return res


class TestSmartDivision(unittest.TestCase):
    pass
    # def test_division_by_0(self):
    #     """Test that dividing by 0 raises an exception
    #     """
    #     with self.assertRaises(Exception):
    #         smart_division(10, 0)

    # def test_float_division(self):
    #     """Check that the float division returns a correct result (with approximation)
    #     """
    #     self.assertAlmostEqual(smart_division(2, 3), 0.66, places=1)

    # def test_int_division(self):
    #     self.assertEqual(smart_division(1, 1), 1)
    #     self.assertEqual(smart_division(10, 2), 5)


if __name__ == '__main__':
    unittest.main()

# Use "nosetests-2.7 show_cov.py -sv --with-cov --cov-report=html"
# and open htmlcov/index.html to see the html report
