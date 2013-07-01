import unittest
import with_side_1
from os import remove

from with_side_vars import *
# using unittest

class TestReadFromDisk(unittest.TestCase):
    def setUp(self):
        self.old_fname = with_side_1.FNAME
        with_side_1.FNAME = TMP
        open(TMP, 'w').write(TEXT)

    def tearDown(self):
        with_side_1.FNAME = self.old_fname
        remove(TMP)

    def test_read_from_disk(self):
        res = with_side_1.read_from_disk()
        self.assertEqual(res, DESIRED)

# TODO: should also check the condition case where the file does not exist

if __name__ == '__main__':
    unittest.main()
