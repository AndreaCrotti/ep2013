GLOBAL_VALUE = 0


def silly_function(value):
    global GLOBAL_VALUE
    GLOBAL_VALUE += 1
    return (value * 2) + GLOBAL_VALUE


if __name__ == '__main__':
    test_smart()
