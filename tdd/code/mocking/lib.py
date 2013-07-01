from os import listdir

def filter_dirs(pth):
    for l in listdir(pth):
        if 'x' in l:
            yield l


class ComplexObject(object):
    def method(self):
        print("Very complex and expensive")


class Obj(object):
    def __init__(self):
        self.c = ComplexObject()
        self.c.method()
