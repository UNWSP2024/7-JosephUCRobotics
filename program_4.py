# Author: Joseph Kracht
# Last Modified: 10/11/2025
# Title: Coordinates

# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

import math

def get_user_xyz_tuple(point_name):
    x = float(input("Enter the x value for point "+point_name+": "))
    y = float(input("Enter the y value for point "+point_name+": "))
    z = float(input("Enter the z value for point "+point_name+": "))
    return (x,y,z)

# get points
point_1 = get_user_xyz_tuple("1")
point_2 = get_user_xyz_tuple("2")

def calc_distance(point_a, point_b):
    return math.sqrt(math.pow(point_b[0] - point_a[0],2) + math.pow(point_b[1] - point_a[1], 2) + math.pow(point_a[2] - point_b[2],2))

# calc distance
distance = calc_distance(point_1, point_2)

# print distance
print("The distance between the two entered points is",distance)
