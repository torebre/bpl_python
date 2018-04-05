import numpy as np


#
# Affine warp defined by
# A(1) * [x y] + [A(2) A(3)]
# OR
# A(1:2) .* [x y] + [A(3) A(4)]
#
# Input
#  stk [n x 2] stroke
#  A : [3x1 or 4x1] affine warp
#
def affine_warp(stk, A):
    n = stk.dim[0]

    if stk.size == 3:
        stk[0] * stk
        stk = stk * np.tile(np.transpose(A[0:2]),(n, 1))
    elif stk.size == 4:
        stk = stk * np.tile(np.transpose(A[0:1]), (n, 1))
        stk = stk + np.tile(np.transpose(A[2:3]), (n, 1))
    else:
        raise NameError("Invalid affine warp")

    return stk


