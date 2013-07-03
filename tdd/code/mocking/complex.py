class ComplexObject(object):
    def method(self):
        print("Very complex and expensive")


class Obj(object):
    def __init__(self):
        self.c = ComplexObject()
        self.c.method()
