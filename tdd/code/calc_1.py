def mysum(a, b):
    return a + b

def mysubstract(a, b):
    return a - b

def test_ops():
    assert mysum(0, 0) == 0
    assert mysum(1, -1) == 0
    assert mysubstract(1, 1) == 0

def test_combined():
    a = 10
    bvals = range(100)
    for b in bvals:
        assert mysubstract(mysum(a, b), a) == b


if __name__ == '__main__':
    test_ops()
    test_combined()
