def report_error(arg):
    print("Error %s" % arg)


def smart_function(arg0):
    if rare_failure_condition():
        report_error(argO)
    else:
        normal_behaviour(arg0)


def rare_failure_condition():
    return True


def normal_behaviour(arg):
    return arg


if __name__ == '__main__':
    smart_function(42)
