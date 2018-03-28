import unittest
import numpy as np

from bpl.bottomup.skeleton import bwmorph_endpoints


class TestStringMethods(unittest.TestCase):

    def test_end(self):
        matrix = np.matrix('0 0 0; 0 1 0; 0 0 1')
        self.assertTrue(bwmorph_endpoints.isEnd(1, 1, matrix, 3, 3))


if __name__ == '__main__':
    unittest.main()