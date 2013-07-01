GLOBAL_VALUE = 0

from mock import patch

def report_error(arg):
    print(arg)


def test_adder():
    assert adder(0, 0) == 0
    assert adder(-1, 1) == 0


def adder(a, b):
    return a + b

test_adder()


def silly_function(value):
    global GLOBAL_VALUE
    GLOBAL_VALUE += 1
    return (value * 2) + GLOBAL_VALUE


if __name__ == '__main__':
    test_smart()
