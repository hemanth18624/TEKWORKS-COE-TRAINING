# Base class
class Shape:
    def area(self):
        # Default area for Shape is 0
        return 0

# Subclass
class Square(Shape):
    def __init__(self, length):
        # Initialize the length of the square
        self.length = length

    def area(self):
        # Override the area method to calculate the area of the square
        return self.length * self.length

# Example usage
# Create an instance of the Square class with length 5
square = Square(5)

# Display the area of the square
print(f"Area of Square: {square.area()}")  # Output: 25

# Create an instance of the Shape class
shape = Shape()

# Display the default area of Shape
print(f"Area of Shape: {shape.area()}")  # Output: 0
