from unittest import TestCase

from vector import Vector


class VectorTests(TestCase):
    def test_calculate_correct_components(self):
        expected_vec = {'ax': 4.330127018922194, 'ay': 2.4999999999999996}
        vec = Vector.from_magnitude_and_angle(magnitude=5.0, angle=30.0)

        self.assertEqual(expected_vec['ax'], vec.ax)
        self.assertEqual(expected_vec['ay'], vec.ay)

    def test_get_components(self):
        expected_vec = (4.330127018922194, 2.4999999999999996)
        vec = Vector.from_magnitude_and_angle(magnitude=5.0, angle=30.0)

        self.assertEqual(expected_vec, vec.get_components())

    def test_calculate_correct_magnitude(self):
        magnitude = Vector(ax=3.0, ay=4.0).calculate_magnitude()

        self.assertEqual(5, magnitude)
