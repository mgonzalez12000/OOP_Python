# Marco Gonzalez
# CS 3035-01
# The cylinder.py module contains a Cylinder subclass that inherits from the abstract class Shape3D. It will override
# the area method, volume method and both dunder methods __str__ __repr__ for appropriate string representations of a
# Cylinder object

from shape3d import Shape3D
import math
import doctest


class Cylinder(Shape3D):
    __radius: float = 0.1
    __height: float = 0.1

    def __init__(self, __radius, __height):
        self.__radius = __radius
        self.__height = __height

    def get_radius(self):
        """
        Gets the radius of a Cylinder object

        Args:
            self

        Returns:
            float: gets the radius of Cylinder

        Examples:
            >>> cylinder = Cylinder(12.0, 10.0)
            >>> cylinder.get_radius()
            12.0
            >>> cylinder_2 = Cylinder (15.3, 2.2)
            >>> cylinder_2.get_radius()
            15.3
            >>> cylinder_3 = Cylinder(2.3, 1.2)
            >>> cylinder_3.get_radius()
            2.3
        """
        return self.__radius

    def set_radius(self, __radius):
        """
        Sets the radius of Cylinder

        Args:
            self, __raduis

        Returns:
            float: sets new radius of Cylinder

        Examples:
            >>> cylinder = Cylinder(1, 5)
            >>> cylinder.set_radius(5)
            >>> cylinder.get_radius()
            5
            >>> cylinder_2 = Cylinder (15.3, 2.2)
            >>> cylinder_2.set_radius(19)
            >>> cylinder_2.get_radius()
            19
            >>> cylinder_3 = Cylinder(2.3, 1.2)
            >>> cylinder_3.set_radius(4)
            >>> cylinder_3.get_radius()
            4
        """
        self.__radius = __radius

    def get_height(self):
        """
        Gets the height of a Cylinder object

        Args:
            self

        Returns:
            float: the radius of the object

        Examples:
            >>> cylinder = Cylinder(12.0, 10.0)
            >>> cylinder.get_height()
            10.0
            >>> cylinder_2 = Cylinder (15.3, 2.2)
            >>> cylinder_2.get_height()
            2.2
            >>> cylinder_3 = Cylinder(2.3, 1.2)
            >>> cylinder_3.get_height()
            1.2
        """
        return self.__height

    def set_height(self, __height):
        """
        Sets a height for Cylinder

        Args:
            self, __height

        Returns:
            float: the radius of the object

        Examples:
            >>> cylinder = Cylinder(1, 5)
            >>> cylinder.set_height(10)
            >>> cylinder.get_height()
            10
            >>> cylinder_2 = Cylinder (15.3, 2.2)
            >>> cylinder_2.set_height(99)
            >>> cylinder_2.get_height()
            99
            >>> cylinder_3 = Cylinder(2.3, 1.2)
            >>> cylinder_3.set_height(89)
            >>> cylinder_3.get_height()
            89
        """
        self.__height = __height

    def area(self, **kwargs):
        """
        Returns total area of an object

        Args:
            self

        Returns:
            float: 2 * pi * radius^2 * height + 2 * pi * radius^2

        Examples:
            >>> cylinder = Cylinder(1, 5)
            >>> cylinder.area()
            37.7
            >>> cylinder_2 = Cylinder(15.3, 2.2)
            >>> cylinder_2.area()
            1682.32
            >>> cylinder_3 = Cylinder (2.3, 1.2)
            >>> cylinder_3.area()
            50.58
        """
        area_cylinder = 2 * math.pi * math.pow(self.__radius, 2) + 2 * math.pi * self.__radius * self.__height
        return round(area_cylinder, 2)

    def volume(self, **kwargs):
        """
        Returns total volume of an object

        Args:
            self

        Returns:
            float: pi * radius^2 * height

        Examples:
            >>> cylinder = Cylinder(1, 5)
            >>> cylinder.volume()
            15.71
            >>> cylinder_2 = Cylinder(15.3, 2.2)
            >>> cylinder_2.volume()
            1617.91
            >>> cylinder_3 = Cylinder (2.3, 1.2)
            >>> cylinder_3.volume()
            19.94
        """
        volume_cylinder = math.pi * math.pow(self.__radius, 2) * self.__height
        return round(volume_cylinder, 2)

    def __str__(self):
        """
        Returns apropiate string representation of Cylinder object

        Args:
            self

        Returns:
            str: Representation of Cylinder

        Examples:
            >>> cylinder = Cylinder(1, 5)
            >>> cylinder.__str__()
            'Cylinder contains radius: 1 height: 5'
            >>> cylinder_2 = Cylinder(15.3, 2.2)
            >>> cylinder_2.__str__()
            'Cylinder contains radius: 15.3 height: 2.2'
            >>> cylinder_3 = Cylinder(2.3, 1.2)
            >>> cylinder_3.__str__()
            'Cylinder contains radius: 2.3 height: 1.2'
        """
        return 'Cylinder contains ' + 'radius: ' + str(self.__radius) + ' height: ' + str(self.__height)

    def __repr__(self):
        """
        Returns apropiate string representation of Cylinder object

        Args:
            self

        Returns:
            str: Representation of Cylinder

        Examples:
            >>> cylinder = Cylinder(1, 5)
            >>> cylinder.__repr__()
            'Cylinder(1, 5)'
            >>> cylinder_2 = Cylinder(15.3, 2.2)
            >>> cylinder_2.__repr__()
            'Cylinder(15.3, 2.2)'
            >>> cylinder_3 = Cylinder(2.3, 1.2)
            >>> cylinder_3.__repr__()
            'Cylinder(2.3, 1.2)'
        """
        return 'Cylinder(' + str(self.__radius) + ', ' + str(self.__height) + ')'


doctest.testmod()
