#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Class Rectangle validated private instance attribute width and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor Function using property and setter and count the
        number of instances
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Method to retrieve the value of Width Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to retrieve the value of Height Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the calculated area of Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Returns the calculated perimeter of Rectangle instance"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """Return the string representation of the rectangle"""
        if self.height == 0 or self.width == 0:
            return ""
        pic = ""
        for i in range(self.height):
            for j in range(self.width):
                pic += str(self.print_symbol)
            pic += "\n"
        pic = pic[:-1]
        return pic

    def __repr__(self):
        """Return the object function representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Detect instance deletion of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to return the biggest rectangle by area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method to create a square Rectangle instance"""
        return cls(size, size)
