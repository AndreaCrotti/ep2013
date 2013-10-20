import unittest
from mock import patch
unittest.defaultTestLoader

import lib

class TestLib(unittest.TestCase):
    @patch('lib.listdir', new=lambda x: ['one', 'two', 'x'])
    def test_filter_dirs(self):
        res = list(lib.filter_dirs('.'))
        self.assertEqual(len(res), 1)
