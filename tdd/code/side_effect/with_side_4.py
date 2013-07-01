import unittest
from mock import patch
from os import remove
import with_side_1
from with_side_vars import *

# using unittest and mock
@patch('with_side_1.FNAME', new=TMP)
class TestReadFromDiskMocked(unittest.TestCase):
    def setUp(self):
        open(TMP, 'w').write(TEXT)

    def tearDown(self):
        remove(TMP)

    def test_read_from_disk(self):
        res = with_side_1.read_from_disk()
        self.assertEqual(res, DESIRED)


if __name__ == '__main__':
    unittest.main()

