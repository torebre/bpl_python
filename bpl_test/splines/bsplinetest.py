import unittest
import numpy as np

from bpl.splines.bspline_eval import bspline_eval


class TestStringMethods(unittest.TestCase):

    def test_recover(self):
        cpts = np.matrix('0 2; 0 4; 0 6; 0 8; 0 10')
        cpts = cpts + 10 * np.random.uniform() * np.random.rand(cpts.shape)

        nland = cpts.shape[0]
        sval = bspline_gen_s(nland)



if __name__ == '__main__':
    unittest.main()