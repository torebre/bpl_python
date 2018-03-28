import unittest
import numpy as np
import matplotlib.pyplot as plt

import bpl.bottomup.skeleton.bwmorph as bw


class bwmorph_test(unittest.TestCase):

    # def test_thin(self):
    #     test_matrix = np.zeros([4, 4], dtype=bool)
    #     test_matrix[1, 2] = True
    #     test_matrix[2, 1] = True
    #     test_matrix[2, 2] = True
    #
    #     print("Input matrix:")
    #     print(test_matrix)
    #
    #     result = bw.thin(test_matrix)
    #
    #     print("Output matrix:")
    #     print(result)


    def test_thin2(self):
        test_matrix = np.zeros([3, 3], dtype = bool)
        test_matrix[0, 1] = True
        test_matrix[0, 2] = True
        test_matrix[1, 1] = True
        test_matrix[1, 2] = True

        print("Input matrix:")
        print(test_matrix)

        plt.matshow(test_matrix)
        plt.title("Input matrix")
        plt.show()

        result = bw.thin(test_matrix)

        print("Output matrix:")
        print(result)

        plt.matshow(result)
        plt.title("Output matrix")
        plt.show()




if __name__ == '__main__':
    unittest.main()