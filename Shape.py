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
    
    class shapeCalculator(ABC):
        """Calculates properties of a shape"""
        @staticmethod
        @abstractmethod
        def getArea(shape: Shape):
            pass
        
        @staticmethod
        @abstractmethod
        def getPerimeter(shape: Shape):
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
    
    def getCorners(self):
        return self.corners

class SquareCalculator:
    """Calculates properties of a square"""
    @staticmethod
    def getArea(square: Square):
        return square.getArea()
    
    @staticmethod
    def getPerimeter(square: Square):
        return square.getPerimeter()

class RectangleCalculator:
    """Calculates properties of a rectangle"""
    @staticmethod
    def getArea(rectangle: Rectangle):
        return rectangle.getArea()
    
    @staticmethod
    def getPerimeter(rectangle: Rectangle):
        return rectangle.getPerimeter()

class CircleCalculator:
    """Calculates properties of a circle"""
    @staticmethod
    def getArea(circle: Circle):
        return circle.getArea()
    
    @staticmethod
    def getPerimeter(circle: Circle):
        return circle.getPerimeter()

# Example usage
square = Square(4)
square_calc = SquareCalculator()
print(f"Square area: {square_calc.getArea(square)}, perimeter: {square_calc.getPerimeter(square)}, corners: {square.getCorners()}")

rectangle = Rectangle(4, 5)
rectangle_calc = RectangleCalculator()
print(f"Rectangle area: {rectangle_calc.getArea(rectangle)}, perimeter: {rectangle_calc.getPerimeter(rectangle)}, corners: {rectangle.getCorners()}")

circle = Circle(3)
circle_calc = CircleCalculator()
print(f"Circle area: {circle_calc.getArea(circle)}, circumference: {circle_calc.getPerimeter(circle)}, corners: {circle.getCorners()}")
