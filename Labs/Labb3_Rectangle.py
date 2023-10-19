import math

class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        """
        Initialize a Rectangle with the given width, height, and position (x, y).
        Parameters:
        - width (float): The width of the rectangle.
        - height (float): The height of the rectangle.
        - x (float): The x-coordinate of the top-left corner of the rectangle.
        - y (float): The y-coordinate of the top-left corner of the rectangle.
        """
        self.set_dimensions(width, height)
        self.set_position(x, y)

    @property
    def area(self):
        """
        Calculate and return the area of the rectangle.
        Returns:
        float: The area of the rectangle.
        """
        return self.width * self.height

    @property
    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        Returns:
        float: The perimeter of the triangle.
        """
        return 2 * (self.width + self.height)

    def __eq__(self, other):
        """
        Check if this rectangle is equal to another rectangles dimensions and position.
        Parameters:
        - other (Rectangle): The other rectangle to compare with.
        Returns:
        bool: True if the rectangles are equal, False otherwise.
        """
        if isinstance(other, Rectangle):
            return (self.width == other.width) and (self.height == other.height) and (self.x == other.x) and (self.y == other.y)
        return False

    def __lt__(self, other):
        """
        Compare this rectangles area with another rectangle and check if it is less than.
        Parameters:
        - other (Rectangle): The other rectangle to compare with.
        Returns:
        bool or NotImplemented: True if this rectangles area is less, False if not comparable, or NotImplemented.
        """
        if isinstance(other, Rectangle):
            return self.area < other.area
        return NotImplemented

    def __le__(self, other):
        """
        Compare this rectangles area with another rectangle and check if it is less than or equal to.
        Parameters:
        - other (Rectangle): The other rectangle to compare with.
        Returns:
        bool or NotImplemented: True if this rectangles area is less or equal, False if not comparable, or NotImplemented.
        """
        if isinstance(other, Rectangle):
            return self.area <= other.area
        return NotImplemented

    def __gt__(self, other):
        """
        Compare this rectangles area with another rectangle and check if it is greater than.
        Parameters:
        - other (Rectangle): The other rectangle to compare with.
        Returns:
        bool or NotImplemented: True if this rectangles area is greater, False if not comparable, or NotImplemented.
        """
        if isinstance(other, Rectangle):
            return self.area > other.area
        return NotImplemented

    def __ge__(self, other):
        """
        Compare this rectangles area with another rectangle and check if it is greater than or equal to.
        Parameters:
        - other (Rectangle): The other rectangle to compare with.
        Returns:
        bool or NotImplemented: True if this rectangles area is greater or equal, False if not comparable, or NotImplemented.
        """
        if isinstance(other, Rectangle):
            return self.area >= other.area
        return NotImplemented

    def __repr__(self):
        """
        Return a string representation of the rectangle, including its dimensions and position.
        Returns:
        str: A string representation of the rectangle.
        """
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"

    def __str__(self):
        """
        Return a string representation of the rectangle.
        Returns:
        str: A string representation of the rectangle.
        """
        return f"Rectangle with dimensions {self.width}x{self.height} at position ({self.x}, {self.y})"

    def set_dimensions(self, width, height):
        """
        Set the dimensions (width and height) of the rectangle. Raise an error if they are negative.
        Parameters:
        - width (float): The new width for the rectangle.
        - height (float): The new height for the rectangle.
        Raises:
        ValueError: If the width or height is negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative.")
        self.width = width
        self.height = height

    def set_position(self, x, y):
        """
        Set the position (x, y) of the top-left corner of the rectangle.
        Parameters:
        - x (float): The new x-coordinate of the top-left corner.
        - y (float): The new y-coordinate of the top-left corner.
        """
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        """
        Translate the position of the rectangle by the specified values (dx and dy).
        Parameters:
        - dx (float): The horizontal translation.
        - dy (float): The vertical translation.
        Raises:
        - ValueError: If dx or dy are not valid numbers.
        """
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise ValueError("Translation values must be valid numbers.")
        self.x += dx
        self.y += dy

    def is_point_inside(self, point_x, point_y):
        """
        Check if a point with coordinates (point_x, point_y) is inside the rectangle.
        Parameters:
        - point_x (float): The x-coordinate of the point to check.
        - point_y (float): The y-coordinate of the point to check.
        Returns:
        bool: True if the point is inside the rectangle, False otherwise.
        """
        return (self.x <= point_x <= self.x + self.width) and (self.y <= point_y <= self.y + self.height)
    





