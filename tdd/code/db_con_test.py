import unittest
from mock import patch

import db_con

SIMPLE_LIST = ['one', 'two', 'three']


class FakeTestFetcher(db_con.TestFetcher):
    def __init__(self):
        self.tests = SIMPLE_LIST


def test_with_fake_test():
    fake = FakeTestFetcher()
    assert fake.get_last() == 'three'


def return_simple_list(arg):
    return SIMPLE_LIST


@patch('db_con.TestFetcher.fetch_from_db', new=return_simple_list)
class TestDbConMock(unittest.TestCase):
    def test_fetch_from(self):
        tf = db_con.TestFetcher()
        self.assertEqual(tf.get_last(), 'three')
        self.assertEqual(str(tf), 'one\ntwo\nthree')


if __name__ == '__main__':
    unittest.main()
