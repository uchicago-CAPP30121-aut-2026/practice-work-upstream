"""
Team Tutorial #4: Point class
"""

import math

class Point:
    def __init__(self, x, y):
        """
        Constructor for the Point class

        Args:
            x: (float) x-coordinate
            y: (float) y-coordinate
        """

        self.x = x
        self.y = y

    def distance_to_origin(self):
        """
        Calculate the distance to the origin

        Returns: distance (float)

        """
        return math.sqrt(self.x**2 + self.y**2)

    def to_polar(self):
        """
        Compute the polar coordinates

        Returns (Tuple[float, float]: radial coordinate, angular
          coordinate in degrees (tuple)

        """
        ### YOUR CODE HERE ###
        return None

    def distance(self, other):
        """
        Calculate the distance between two points

        Args:
            other: (Point) the other point

        Returns (float): distance
        """
        ### YOUR CODE HERE ###
        return None
