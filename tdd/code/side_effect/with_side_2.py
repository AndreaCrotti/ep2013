import with_side_1
from os import remove

from with_side_vars import *
import with_side_1

# first manual approach

def test_read_from_disk():
    old_fname = with_side_1.FNAME
    with_side_1.FNAME = TMP

    open(TMP, 'w').write(TEXT)
    assert with_side_1.read_from_disk() == DESIRED

    remove(TMP)
    with_side_1.FNAME = old_fname

# TODO: should also check the condition case where the file does not exist

if __name__ == '__main__':
    test_read_from_disk()

# Use "nosetests-2.7 with_side_two.py -sv --with-cov --cov-report=term-missing"
# to run the tests and show the report of the missing lines
