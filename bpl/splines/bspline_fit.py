import numpy as np
import numpy.linalg as lin

from vectorized_bspline_coeff import vectorized_bspline_coeff

# function P = bspline_fit(sval ,X ,L)
def bspline_fit(sval, X, L):

    # sval = sval(:);

    # ns = length(sval);
    ns = len(sval)

    # asser t(isequal(size(X) ,[ns 2]));

    # S = repmat(sval ,[1 L]);
    S = np.tile(sval, (1, L))

    # I = repmat(0: L -1 ,[ns 1]);
    I = np.tile(range(0, L - 1), (ns, 1))

    # A = vectorized_bspline_coeff(I ,S);
    A = vectorized_bspline_coeff(I, S)

    # sumA = sum(A ,2);
    sumA = sum(A, 2)

    # Cof = A ./ repmat(sumA, [1 L]);
    Cof = A / np.tile(sumA, (1 ,L))

    # P = (Cof'*Cof)\Cof' * X;
    return np.linalg.lstsq(np.transpose(Cof)*Cof, np.transpose(Cof))[0] * X

# end