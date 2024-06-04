from abc import abstractmethod
from turtle import width

class Shape:
    """ Defines a shape with width and height"""
    #uses SOLID principle of single responsibility
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @abstractmethod
    def getArea(self):
        pass
    @abstractmethod
    def getPerimeter(self):
        pass
    
class Square(Shape):
    """Defines a square with width"""
    def __init__(self, width):
        self.width
    
    def check_Corner(self):
        if self.corner == 90:
            return True
        else:
            return False
        
class SquareCalculator(Shape):
    """Calculates the area and perimeter of a Square"""
    def get_Area(width):
        square_Area = width * width
        return square_Area
    
    def get_Perimeter(width):
        square_Perimeter = 4*(width)
        return square_Perimeter
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #do I need the above code?
class RectangleCalculator(Shape):
    def get_Area(self, width, height):
        rectangleArea = width * height
        return rectangleArea
    def get_Perimeter(self, width, height):
        rectanglePerimeter = 2*(width + height)
        return rectanglePerimeter
class Circle:
    """Defines a circle with radius and circumference"""
    def __init__(self, radius, height):
        self.radius = radius

class CircleCalculator(Shape):
"""Calculates the area and circumference of a circle"""
    def get_Area(radius):
        circle_Area = 3.14 * radius * radius
        return circle_Area
    
