import library

library.run_func()
def failing():
    print("In changed function")

library.lib_func = failing
library.run_func()
