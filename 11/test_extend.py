class parent():
    """the parent class for extend"""
    def __init__(self):
        self.age = 20
    
    def print_age(self):
        print(self.age)


# 
class child(parent):
    """the child class for extended"""


childTest = child()
childTest.print_age()