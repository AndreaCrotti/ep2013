import unittest
from mock import Mock, patch

import lib

fake_complex_object_auto = Mock(autospec=lib.ComplexObject)
fake_complex_object = Mock()
fake_complex_object.method = Mock()


# get some kind of class and make it behave the same way

class TestLib(unittest.TestCase):
    @patch('lib.listdir', new=lambda x: ['one', 'two', 'x'])
    def test_filter_dirs(self):
        res = list(lib.filter_dirs('.'))
        self.assertEqual(len(res), 1)

    # put the patch back and forth
    @patch('lib.ComplexObject', new=fake_complex_object_auto)
    def test_obj(self):
        v = lib.Obj()

    @patch('lib.ComplexObject', new=fake_complex_object)
    def test_obj(self):
        v = lib.Obj()
