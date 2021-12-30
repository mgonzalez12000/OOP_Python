# Marco Gonzalez
# CS 3035-01
# Shape3D is an abstract class that also consists of abstract methods area and volume that will be overrode by it's
# subclasses. Both dunder methods __str__ and __repr__ will also be overrode by it's subclasses for an appropriate
# string representation of their object.

from abc import abstractmethod
import doctest


class Shape3D:
    __color: str = 'black'
    __transparency: float = 0.0

    def __init__(self, __color, __transparency):
        self.__color = __color
        self.__transparency = __transparency

    def get_color(self):
        """
        Gets the color of Shape3D object

        Args:
            self

        Returns:
            str: color of Shape#D object

        Examples:
            >>> shape3d = Shape3D('blue', 10.0)
            >>> shape3d.get_color()
            'blue'
            >>> shape3d_2 = Shape3D('white', 5.2)
            >>> shape3d_2.get_color()
            'white'
            >>> shape3d_3 = Shape3D('yellow', 4.5)
            >>> shape3d_3.get_color()
            'yellow'
        """
        return self.__color

    def set_color(self, __color):
        """
        Sets a color to a Shape3D

        Args:
            self. __color

        Returns:
            str: sets new color of Shape3D

        Examples:
            >>> shape3d = Shape3D('blue', 10.0)
            >>> shape3d.set_color('white')
            >>> shape3d.get_color()
            'white'
            >>> shape3d_2 = Shape3D('white', 5.2)
            >>> shape3d_2.set_color('blue')
            >>> shape3d_2.get_color()
            'blue'
            >>> shape3d_3 = Shape3D('yellow', 4.5)
            >>> shape3d_3.set_color('red')
            >>> shape3d_3.get_color()
            'red'
        """
        self.__color = __color

    def get_transparency(self):
        """
        Gets the transparency of Shape3D

        Args:
            self

        Returns:
            float: transparency level of Shape3D

        Examples:
            >>> shape3d = Shape3D('blue', 10.0)
            >>> shape3d.get_transparency()
            10.0
            >>> shape3d_2 = Shape3D('white', 5.2)
            >>> shape3d_2.get_transparency()
            5.2
            >>> shape3d_3 = Shape3D('yellow', 4.5)
            >>> shape3d_3.get_color()
            4.5
        """
        return self.__transparency

    def set_transparency(self, __transparency):
        """
        Sets the transparency of Shape3D

        Args:
            self, __transparency

        Returns:
            float: the transparency level of Shape3D

        Examples:
            >>> shape3d = Shape3D('blue', 10.0)
            >>> shape3d.set_transparency(1.0)
            >>> shape3d.get_transparency()
            1.0
            >>> shape3d_2 = Shape3D('white', 5.2)
            >>> shape3d_2.set_transparency(2.3)
            >>> shape3d_2.get_transparency()
            2.3
            >>> shape3d_3 = Shape3D('yellow', 4.5)
            >>> shape3d_3.set_transparency(99.8)
            >>> shape3d_3.get_transparency()
            99.8
        """
        self.__transparency = __transparency

    # The class shall have abstract method definitions for area() and volume() methods.
    @abstractmethod
    def area(self, other):
        pass

    @abstractmethod
    def volume(self, other):
        pass

    # This class shall override the str and repr methods to print string representations of the class.
    def __str__(self):
        """
        Returns an appropiate string representation of Shape3D

        Args:
            self

        Returns:
            str: A string representation of Shape3D

        Examples:
            >>> shape3d = Shape3D('blue', 10.0)
            >>> shape3d.__str__()
            'Shape3D contains color: blue transparency: 10.0'
            >>> shape3d_2 = Shape3D('white', 20)
            >>> shape3d_2.__str__()
            'Shape3D contains color: white transparency: 20'
            >>> shape3d_3 = Shape3D('orange', 4.23)
            >>> shape3d_3.__str__()
            'Shape3D contains color: orange transparency: 4.23'
        """
        return 'Shape3D contains ' + 'color: ' + str(self.__color) + ' transparency: ' + str(self.__transparency)

    def __repr__(self):
        """
        Returns an appropiate string representation of Shape3D

        Args:
            self

        Returns:
            str: A string representation of Shape3D

        Examples:
            >>> shape3d = Shape3D('blue', 10.0)
            >>> shape3d.__repr__()
            'Shape3D(blue, 10.0)'
            >>> shape3d_2 = Shape3D('white', 20)
            >>> shape3d_2.__repr__()
            'Shape3D(white, 20)'
            >>> shape3d_3 = Shape3D('orange', 4.23)
            >>> shape3d_3.__repr__()
            'Shape3D(orange, 4.23)'
        """
        return 'Shape3D(' + str(self.__color) + ', ' + str(self.__transparency) + ')'


doctest.testmod()
