# Marco Gonzalez
# CS 3035-01
# Module shape_list has a class ShapeList. The ShapeList class is a subclass of the type list. The class will be used
# to store Shape3D objects in a list. This class will also have instance methods that calculate the average area of
# both Cylinders and Pyramids, the max and min volumes for objects that store in the list, and display Cylinders
# and Pyramids.

from cylinder import Cylinder
from pyramid import Pyramid
import doctest


class ShapeList(list):

    def __init__(self, *args):
        list.__init__(self, *args)

    def average_area_of_cylinders(self):
        """
        Returns the average area for the type Cylinder

        Args:
            self

        Returns:
            float: total area of all Cylinder/count of Cylinders

        Examples:
            >>> cylinder_1 = Cylinder(1, 5)
            >>> cylinder_2 = Cylinder(2.3, 7.9)
            >>> pyramid_1 = Pyramid(2, 7, 5)
            >>> pyramid_2 = Pyramid(2.5, 9.1, 4.1)
            >>> shape_list = ShapeList()
            >>> shape_list.append(cylinder_1)
            >>> shape_list.append(cylinder_2)
            >>> shape_list.append(pyramid_1)
            >>> shape_list.append(pyramid_2)
            >>> shape_list.average_area_of_cylinders()
            92.55
        """
        total = 0.0
        count = 0.0
        for index in range(len(self)):
            if type(self[index]) == Cylinder:
                total += self[index].area()
                count += 1
        return round(total/count, 2)

    def average_area_of_pyramids(self):
        """
        Returns the average area for the type Pyramid

        Args:
            self

        Returns:
            float: total area of all Pyramid/count of Pyramid

        Examples:
            >>> cylinder_1 = Cylinder(1, 5)
            >>> cylinder_2 = Cylinder(2.3, 7.9)
            >>> pyramid_1 = Pyramid(2, 7, 5)
            >>> pyramid_2 = Pyramid(2.5, 9.1, 4.1)
            >>> shape_list = ShapeList()
            >>> shape_list.append(cylinder_1)
            >>> shape_list.append(cylinder_2)
            >>> shape_list.append(pyramid_1)
            >>> shape_list.append(pyramid_2)
            >>> shape_list.average_area_of_pyramids()
            25.38
        """
        total = 0.0
        count = 0.0
        for index in range(len(self)):
            if type(self[index]) == Pyramid:
                total += self[index].area()
                count += 1
        return round(total/count, 2)

    def max_volume(self):
        """
        Returns the max volume for Shape3D

        Args:
            self

        Returns:
            Shape3D: object with the highest volume

        Examples:
            >>> cylinder_1 = Cylinder(1, 5)
            >>> cylinder_2 = Cylinder(2.3, 7.9)
            >>> pyramid_1 = Pyramid(2, 7, 5)
            >>> pyramid_2 = Pyramid(2.5, 9.1, 4.1)
            >>> shape_list = ShapeList()
            >>> shape_list.append(cylinder_1)
            >>> shape_list.append(cylinder_2)
            >>> shape_list.append(pyramid_1)
            >>> shape_list.append(pyramid_2)
            >>> shape_list.max_volume()
            Cylinder(2.3, 7.9)
        """
        object_volume = self[0].volume()
        max_object = self[0]
        index = 0
        while index < len(self):
            if self[index].volume() > object_volume:
                object_volume = self[index].volume()
                max_object = self[index]
            index += 1
        return max_object

    def min_volume(self):
        """
        Returns the min volume for Shape3D

        Args:
            self

        Returns:
            Shape3D: object with the lowest volume

        Examples:
            >>> cylinder_1 = Cylinder(1, 5)
            >>> cylinder_2 = Cylinder(2.3, 7.9)
            >>> pyramid_1 = Pyramid(2, 7, 5)
            >>> pyramid_2 = Pyramid(2.5, 9.1, 4.1)
            >>> shape_list = ShapeList()
            >>> shape_list.append(cylinder_1)
            >>> shape_list.append(cylinder_2)
            >>> shape_list.append(pyramid_1)
            >>> shape_list.append(pyramid_2)
            >>> shape_list.min_volume()
            Pyramid(2, 7)
        """
        object_volume = self[0].volume()
        min_object = self[0]
        index = 0
        while index < len(self):
            if self[index].volume() < object_volume:
                object_volume = self[index].volume()
                min_object = self[index]
            index += 1
        return min_object

    def display_cylinders(self):
        """
        Returns all Cylinders

        Args:
            self

        Returns:
            Shape3D: all Cylinders

        Examples:
            >>> cylinder_1 = Cylinder(1, 5)
            >>> cylinder_2 = Cylinder(2.3, 7.9)
            >>> pyramid_1 = Pyramid(2, 7, 5)
            >>> pyramid_2 = Pyramid(2.5, 9.1, 4.1)
            >>> shape_list = ShapeList()
            >>> shape_list.append(cylinder_1)
            >>> shape_list.append(cylinder_2)
            >>> shape_list.append(pyramid_1)
            >>> shape_list.append(pyramid_2)
            >>> shape_list.display_cylinders()
            [Cylinder(1, 5), Cylinder(2.3, 7.9)]
        """
        list_cylinders = []
        for index in range(len(self)):
            if type(self[index]) == Cylinder:
                list_cylinders.append(self[index])
        return list_cylinders

    def display_pyramids(self):
        """
        Returns all Pyramids

        Args:
            self

        Returns:
            Shape3D: all Pyramids

        Examples:
            >>> cylinder_1 = Cylinder(1, 5)
            >>> cylinder_2 = Cylinder(2.3, 7.9)
            >>> pyramid_1 = Pyramid(2, 7, 5)
            >>> pyramid_2 = Pyramid(2.5, 9.1, 4.1)
            >>> shape_list = ShapeList()
            >>> shape_list.append(cylinder_1)
            >>> shape_list.append(cylinder_2)
            >>> shape_list.append(pyramid_1)
            >>> shape_list.append(pyramid_2)
            >>> shape_list.display_pyramids()
            [Pyramid(2, 7), Pyramid(2.5, 9.1)]
        """
        list_pyramids = []
        for index in range(len(self)):
            if type(self[index]) == Pyramid:
                list_pyramids.append(self[index])
        return list_pyramids


doctest.testmod()
