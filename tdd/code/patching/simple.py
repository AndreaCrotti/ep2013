from mock import patch

class MyObject(object):
    def __init__(self):
        self.useful_parameter = self.method()
        
    def method(self):
        print("Slow method")
        return 42

