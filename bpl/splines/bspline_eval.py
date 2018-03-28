import numpy as np

# function [y ,Cof] = bspline_eval(sval ,cpts)
def bspline_eval(sval, cpts):

# assert(isvector(sval));
#     sval = sval(:);
#     sval = sval(:);

    # L = size(cpts ,1);
    L = cpts.shape[0]
    # ns = length(sval);
    ns = len(sval)

    # y = zeros(ns ,2);
    y = np.zeros((ns ,2))

    # S = repmat(sval ,[1 L]);
    S = np.tile(sval, (1, L))


    # I = repmat(0: L -1 ,[ns 1]);
    I = np.tile(range(0, L - 1) ,(ns, 1))

    # Cof =  vectorized_bspline_coeff(I ,S);
    Cof = vectorized_bspline_coeff(I ,S)

    # sumC = sum(Cof ,2);
    sumC = np.sum(Cof ,2)

    # Cof = Cof ./ repmat(sumC, [1 L]);
    Cof = Cof / np.tile(sumC, (1, L))

    # y(:, 1) = Cof * cpts(:, 1);
    y[:, 0] = Cof * cpts[:, 0]

    y[:, 1] = Cof * cpts[:, 1]

    return (sval, cpts)

# % Error checking
# assert (~any(isnan(y(:))));
# end