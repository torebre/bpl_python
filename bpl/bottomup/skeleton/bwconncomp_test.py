import unittest
import numpy as np

from bpl.bottomup.skeleton.bwconncomp import bwconncomp


class bwconncomp_test(unittest.TestCase):

    def test_not_connected(self):
        matrix = np.matrix('0 0 0; 0 1 0; 0 0 1')
        self.assertTrue(len(bwconncomp(matrix, 8)) == 0)

    def test_connected(self):
        matrix = np.matrix('1 1 1; 1 1 1; 1 1 1')

        # TODO Check that this definition of connected is correct
        self.assertTrue(len(bwconncomp(matrix, 8)) == 1)


if __name__ == '__main__':
    unittest.main()