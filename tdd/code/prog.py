import library

def dependent():
    # the lib_func can be changed at run-time
    print(library.lib_func())

dependent()
library.lib_func = lambda: 42
dependent()
