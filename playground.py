class MyClass:
    def __init__(self):
        self._protected_var = 10
        self.__private_var = 20

obj = MyClass()
try:
    print(obj._protected_var)
    #print(obj.__private_var)
except:
    print("error1")

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area():
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        

print(Rectangle(4,6).area())


from datetime import datetime

d = datetime.now()
print(d)

print(d.strftime('%Y-%m-%d'))