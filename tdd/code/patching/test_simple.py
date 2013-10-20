from mock import patch
import unittest
from simple import MyObject


class TestSimple(unittest.TestCase):
    @patch('simple.MyObject.method')
    def test_simple(self, patched_myobject_method):
        patched_myobject_method.return_value = 43
        c = MyObject()
        self.assertEqual(c.useful_parameter, 43)
