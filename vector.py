from math import cos, sin, radians, hypot

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

    def calculate_magnitude(self) -> Union[int, float]:
        return hypot(self.ax, self.ay)

    def get_components(self):
        return self.ax, self.ay
