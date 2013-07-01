from itertools import product
from ctypes import cdll

libsum = cdll.LoadLibrary('./libsum.so.1.0.1')
print("Checking sum defined in the C library")

for i in range(100):
    for j in range(100):
        # print("Checking that %d + %d is correct" % (i, j))
        assert libsum.sum(i, j) == i + j, "%d + %d failed!!" % (i, j)

# which an hardcore Pythonist would write as
# assert all(libsum.sum(i, j) == (i + j) for i, j in product(range(100), range(100)))
