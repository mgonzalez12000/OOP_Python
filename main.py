# Marco Gonzalez
# CS 3035-01
# The main.py module is the "driver" of the entire program. main.py asks the user to input the amount of Pyramid
# and Cylinder objects he/she would like to make. It will generate these objects, and add it to the list in a random
# order by using the shuffle() and finally demonstrates that all the instance methods in the shape_list class
# properly work
# Video explanation: https://calstatela.instructuremedia.com/embed/29761ea8-6a8d-4270-a8b6-000c4b2af16b

from shape_list import ShapeList
from cylinder import Cylinder
from pyramid import Pyramid
import random

result = ShapeList()


def main():
    # Exception handling for user input
    while True:
        try:
            user_cylinder = int(input('Enter how many cylinders: '))
            if user_cylinder > 0:
                break
            else:
                print("Please input a number GREATER than 0! TRY AGAIN!")
        except ValueError:
            print('Please input a NUMBER! TRY AGAIN!')
            continue

    while True:
        try:
            user_pyramid = int(input('Enter how many pyramids: '))
            if user_pyramid > 0:
                break
            else:
                print("Please input a number GREATER than 0! TRY AGAIN!")
        except ValueError:
            print('Please input a NUMBER! TRY AGAIN!')
            continue

    print('----------------------------')

    color_choices = ['Blue', 'White', 'Red', 'Purple', 'Orange', 'Yellow', 'Green', 'Magenta', 'Maroon', 'Brown',
                     'Olive', 'Teal', 'Navy', 'Cyan', 'Grey', 'Pink', 'Peach', 'Teal', 'Maroon', 'Amber']

    for cylinder_user_input in range(0, user_cylinder):
        # Choosing a random color from the list
        color_cylinder = random.choice(color_choices)

        # Assigning a float value for the base, height, transparency
        radius_cylinder = round(random.uniform(0, 50), 2)
        height_cylinder = round(random.uniform(0, 50), 2)
        transparency_cylinder = round(random.uniform(0, 1), 2)

        # Create Cylinder object
        cylinder_object = Cylinder(radius_cylinder, height_cylinder)

        # Setting color, transparency, radius, height
        cylinder_object.set_color(color_cylinder)
        cylinder_object.set_transparency(transparency_cylinder)
        cylinder_object.set_radius(radius_cylinder)
        cylinder_object.set_height(height_cylinder)

        # Adding to the list in a random order
        result.append(cylinder_object)
        random.shuffle(result)

        # Printing color, radius, height, area
        print('Cylinder color:', cylinder_object.get_color())
        print('Cylinder transparency', cylinder_object.get_transparency())
        print('Cylinder radius:', cylinder_object.get_radius())
        print('Cylinder height:', cylinder_object.get_height())
        print('Cylinder volume:', cylinder_object.volume())
        print('Cylinder area', cylinder_object.area())
        print()

    # Average area of Cylinder's and display all Cylinder's
    print('Average area of cylinder:', result.average_area_of_cylinders())
    print(result.display_cylinders())
    print('----------------------------')

    for pyramid_user_input in range(0, user_pyramid):
        # Get random color
        color_pyramid = random.choice(color_choices)

        # Assigning a float value for the base, height, slant, transparency
        base_pyramid = round(random.uniform(0, 50), 2)
        height_pyramid = round(random.uniform(0, 50), 2)
        slant_pyramid = round(random.uniform(0, 50), 2)
        transparency_pyramid = round(random.uniform(0, 1), 2)

        # Creating the object
        pyramid_object = Pyramid(base_pyramid, height_pyramid, slant_pyramid)

        # Setting color, transparency, base, slant, height
        pyramid_object.set_color(color_pyramid)
        pyramid_object.set_transparency(transparency_pyramid)
        pyramid_object.set_base(base_pyramid)
        pyramid_object.set_height(height_pyramid)
        pyramid_object.set_slant(slant_pyramid)

        # Adding to the list in a random order
        result.append(pyramid_object)
        random.shuffle(result)

        # Printing color, transparency, base, height, slant, area
        print('Pyramid color:', pyramid_object.get_color())
        print('Pyramid transparency', pyramid_object.get_transparency())
        print('Pyramid base:', pyramid_object.get_base())
        print('Pyramid height:', pyramid_object.get_height())
        print('Pyramid slant:', pyramid_object.get_slant())
        print('Pyramid volume:', pyramid_object.volume())
        print('Pyramid area:', pyramid_object.area())
        print()

    # Average area of Pyramid and display all Pyramids
    print('Average area of pyramids', result.average_area_of_pyramids())
    print(result.display_pyramids())
    print('----------------------------')

    # Print Max and Min volumes of all Shape3D's
    print('List of objects:', result)
    print('Max volume of Shape3D:', result.max_volume())
    print('Min volume of Shape3D:', result.min_volume())


if __name__ == "__main__":
    main()
