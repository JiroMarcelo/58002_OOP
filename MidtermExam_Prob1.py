import math
pi = math.pi


class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return round(2 * pi * self.__radius, 4)

    def area(self):
        return round(pi * self.__radius ** 2, 4)

    def display(self):
        print(f"You've input {self.__radius} as the radius,")
        print(f"The perimeter of the Circle is {self.perimeter()} and its area is {self.area()}")

c = float(input("Input the radius of the circle: "))
dis = Circle(c)
dis.display()

