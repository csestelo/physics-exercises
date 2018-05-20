from math import cos, sin, radians, hypot, atan2, degrees

from typing import Union


class Vector:
    def __init__(self, ax: float, ay: float):
        """
        :param ax: component on the x axis of a given vector
        :param ay: component on the y axis of a given vector
        """
        self.ax = ax
        self.ay = ay

    @classmethod
    def from_magnitude_and_angle(cls, magnitude: float, angle: float):
        """
        :param magnitude: The magnitude/absolute value of a vector
        :param angle: The angle in degrees of a vector
        """
        ax = cos(radians(angle)) * magnitude
        ay = sin(radians(angle)) * magnitude
        return cls(ax, ay)

    def two_vectors_sum(self, bx: float, by: float):
        cx = self.ax + bx
        cy = self.ay + by

        return cx, cy

    def two_vectors_sub(self, bx: float, by: float):
        cx = self.ax + -bx
        cy = self.ay + -by

        return cx, cy

    def multiplication_with_a_scalar(self, times: float):
        ax, ay = (times * self.ax, times * self.ay)
        return ax, ay

    def get_components(self):
        return self.ax, self.ay

    def calculate_magnitude(self) -> Union[int, float]:
        return hypot(self.ax, self.ay)

    def calculate_horizontal_angle(self):
        """
        Calculates the angle, in degrees, for a given vector
        """
        radian_angle = atan2(self.ay, self.ax)

        return degrees(radian_angle)
