from abc import ABC, abstractmethod

class Shape(ABC):
    """Defines a shape with width and height"""
    def __init__(self, width=None, height=None, radius=None, corners=None):
        self.width = width
        self.height = height
        self.radius = radius
        self.corners = corners

    @abstractmethod
    def getCorners(self):
        pass

    
    class shapeCalculator(Shape):
        """Calculates properties of a shape"""
        def area(self):
            pass
        def perimeter(self):
            pass

class Square(Shape):
    """Defines a square with width"""
    def __init__(self, width):
        super().__init__(width=width, corners=4)
    
    def getCorners(self):
        return self.corners

class Rectangle(Shape):
    """Defines a rectangle with width and height"""
    def __init__(self, width, height):
        super().__init__(width=width, height=height, corners=4)
    
    def getCorners(self):
        return self.corners

class Circle(Shape):
    """Defines a circle with radius"""
    def __init__(self, radius):
        super().__init__(radius=radius, corners=0)
    
    def getRadius(self):
        return self.corners

class SquareCalculator:
    """Calculates properties of a square"""
    @staticmethod
    def calc_Perimeter(square: Square):
        return 4 * square.width
    
    
    def calc_Area(square: Square):
        return square.width ** 2

class RectangleCalculator:
    """Calculates properties of a rectangle"""
    @staticmethod
    def calc_Area(rectangle: Rectangle):
        return 2 * (rectangle.width + rectangle.height)
    
    @staticmethod
    def calc_Perimeter(rectangle: Rectangle):
        return rectangle.width * rectangle.height

class CircleCalculator:
    """Calculates properties of a circle"""
    @staticmethod
    def calc_Area(circle: Circle):
        return 3.14 * circle.radius ** 2
    
    @staticmethod
    def calc_Diameter(circle: Circle):
        return 2 * circle.radius

# Using the classes
square = Square(4)
square_calc = SquareCalculator()
print(f"Square area: {square_calc.getArea(square)}, perimeter: {square_calc.getPerimeter(square)}, corners: {square.getCorners()}")

rectangle = Rectangle(4, 5)
rectangle_calc = RectangleCalculator()
print(f"Rectangle area: {rectangle_calc.getArea(rectangle)}, perimeter: {rectangle_calc.getPerimeter(rectangle)}, corners: {rectangle.getCorners()}")

circle = Circle(3)
circle_calc = CircleCalculator()
print(f"Circle area: {circle_calc.getArea(circle)}, circumference: {circle_calc.getPerimeter(circle)}, corners: {circle.getCorners()}")
