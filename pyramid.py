# Marco Gonzalez
# CS 3035-01
# The pyramid.py module contains a Pyramid subclass that inherits from the abstract class Shape3D. It will override the
# area method, volume method and both dunder methods __str__ __repr__ for appropriate string representations of a
# Pyramid object

from shape3d import Shape3D
import math
import doctest


class Pyramid(Shape3D):
    __base: float = 0.1
    __height: float = 0.1
    __slant: float = 0.1

    def __init__(self, __base, __height, __slant):
        self.__base = __base
        self.__height = __height
        self.__slant = __slant

    def get_base(self):
        """
        Gets the base of Pyramid

        Args:
            self

        Returns:
            float: the base of Pyramid

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.get_base()
            2.3
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.get_base()
            1.3
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.get_base()
            4.2
        """
        return self.__base

    def set_base(self, __base):
        """
        Sets the base of Pyramid

        Args:
            self, __base

        Returns:
            float: sets the base of Pyramid

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.set_base(4.2)
            >>> pyramid.get_base()
            4.2
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.set_base(99.3)
            >>> pyramid_2.get_base()
            99.3
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.set_base(85.34)
            >>> pyramid_3.get_base()
            85.34
        """
        self.__base = __base

    def get_height(self):
        """
        Gets the height of Pyramid

        Args:
            self

        Returns:
            float: the height of Pyramid

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.get_height()
            10.0
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.get_height()
            4.5
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.get_height()
            5.3
        """
        return self.__height

    def set_height(self, __height):
        """
        Sets the height of Pyramid

        Args:
            self, __height

        Returns:
            float: sets the height of Pyramid

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.set_height(23.2)
            >>> pyramid.get_height()
            23.2
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.set_height(34.23)
            >>> pyramid_2.get_height()
            34.23
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.set_height(25.25)
            >>> pyramid_3.get_height()
            25.25
        """
        self.__height = __height

    def get_slant(self):
        """
        Gets the slant of Pyramid

        Args:
            self

        Returns:
            float: the slant of Pyramid

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.get_height()
            10.0
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.get_height()
            4.5
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.get_height()
            5.3
        """
        return self.__slant

    def set_slant(self, __slant):
        """
        Sets the slant of Pyramid

        Args:
            self, __slant

        Returns:
            float: sets the slant of Pyramid

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.set_slant(12.2)
            >>> pyramid.get_slant()
            12.2
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.set_slant(54.2)
            >>> pyramid_2.get_slant()
            54.2
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.set_slant(44.23)
            >>> pyramid_3.get_slant()
            44.23
        """
        self.__slant = __slant

    # This class shall override the area and volume methods to return the area and volume of a Pyramid.
    def area(self, **kwargs):
        """
        Returns the area of Pyramid

        Args:
            self

        Returns:
            float: 2 * base * slant + base^2

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.area()
            31.05
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.area()
            7.41
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.area()
            42.0
        """
        area_pyramid = 2 * self.__base * self.__slant + math.pow(self.__base, 2)
        return round(area_pyramid, 2)

    def volume(self, **kwargs):
        """
        Returns the volume of Pyramid

        Args:
            self

        Returns:
            float: 1/3 * base^2 * height

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.volume()
            17.63
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.volume()
            2.54
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.volume()
            31.16
        """
        volume_pyramid = 1/3 * math.pow(self.__base, 2) * self.__height
        return round(volume_pyramid, 2)

    # This class shall override the str() and repr() methods to print appropriate string
    # representations of the Pyramid object.
    def __str__(self):
        """
        Returns the appropiate string representation of Pyramid

        Args:
            self

        Returns:
            str: the string representation of Pyramid

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.__str__()
            'Pyramid contains base: 2.3 height: 10.0'
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.__str__()
            'Pyramid contains base: 1.3 height: 4.5'
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.__str__()
            'Pyramid contains base: 4.2 height: 5.3'
        """
        return 'Pyramid contains ' + 'base: ' + str(self.__base) + ' height: ' + str(self.__height)

    def __repr__(self):
        """
        Returns the appropiate string representation of Pyramid

        Args:
            self

        Returns:
            str: the string representation of Pyramid

        Examples:
            >>> pyramid = Pyramid(2.3, 10.0, 5.6)
            >>> pyramid.__repr__()
            'Pyramid(2.3, 10.0)'
            >>> pyramid_2 = Pyramid(1.3, 4.5, 2.2)
            >>> pyramid_2.__repr__()
            'Pyramid(1.3, 4.5)'
            >>> pyramid_3 = Pyramid(4.2, 5.3, 2.9)
            >>> pyramid_3.__repr__()
            'Pyramid(4.2, 5.3)'
        """
        return 'Pyramid(' + str(self.__base) + ', ' + str(self.__height) + ')'


doctest.testmod()
