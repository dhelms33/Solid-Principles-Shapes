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
    """Defines a rectangle with width, height, and corner angle"""
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner
    
    def checkCorner(self):
        if self.corner == 90:
            return True
        else:
            return False
        
class SquareCalculator(Shape):
    """Calculates the area and perimeter of a Square"""
    def getArea(width):
        square_Area = width * width
        return square_Area
    
    def getPerimeter(width):
        square_Perimeter = 4*(width)
        return perimeter
    
class Circle:
    """Defines a circle with radius and circumference"""
    def __init__(self, radius, height):
        self.radius = radius
class Rectangle(Shape):
    def get_Area(self, width, height):
        rectangleArea = width * height
        return rectangleArea

Class CircleCalculator:
    """Calculates the area and circumference of a circle"""
    def getArea(radius):
        circle_Area = 3.14 * radius * radius
        return circle_Area
    
