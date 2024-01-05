#!/usr/bin/python3
"""Rectangle that defines a rectangle by: (based on 0-rectangle)"""

class Rectangle():
    """
    Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """
        Rectangle class
        Args:
            -width (defualt = 0): int
            -heigth (defualt = 0): int
        """
        self.height = height
        self.width = width

        @property
        def width(self):
            """Getter width"""
            return self.__width

        @width.setter
        def width(self, value):
            """
            Getter Value
            Args:
                - value: int
            """
            if not isinstance(value, int):
                raise TypeError('width must be an integer')

            if value < 0:
                raise ValueError('width must be >= 0')

            self.__width = value

            @property
            def height(self):
                """
                Getter Height
                """
                return self.__heigh

            @height.setter
            def height(self, value):
                """
                Getter value
                Args:
                    - value: int
                """
                if not isinstance(value, int):
                    raise TypeError('height must be an integer')

                if value < 0:
                    raise ValueError('height must be >= 0')

                self.__height = value

                self.__height = value
