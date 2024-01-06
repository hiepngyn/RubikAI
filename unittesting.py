import unittest
from cube import RubiksCube

class TestCubeFunctions(unittest.TestCase):

    def clockwise_face_rotation_unittest(self):
        cube = RubiksCube
        cube.horizontal_turn(0,False)

        