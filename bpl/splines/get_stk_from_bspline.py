import numpy as np



# function stk = get_stk_from_bspline(P ,neval)
def get_stk_from_bspline(P, neval = None):
    # nland = size(P ,1);
    nland = P.shape[0]

    # if ~exist('neval', 'var')
    if neval is None:
        # % set the number of evaluations adaptively,
        # % based on the size of the stroke
        # PM = defaultps;
        PM = defaultps

        # neval = PM.spline_min_neval;
        neval = PM.spline_min_neval

        # s = bspline_gen_s(nland ,neval);
        s = bsplin_gen_s(nland, nevel)

        # stk = bspline_eval(s ,P);
        stk = bspline_eval(s, P)

        # sumdist = sum_pair_dist(stk);
        sumdist = sum_pair_dist(stk)

        # neval = max(neval ,ceil(sumdist . /PM.spline_grain));
        neval = max(neval, np.ceil(sumdist / PM.spline_grain))

        # neval = min(neval ,PM.spline_max_neval);
        neval = min(neval, PM.spline_max_neval)

    # end

    # s = bspline_gen_s(nland ,neval);
    s = bspline_gen_s(nland ,neval)

    # stk = bspline_eval(s ,P);
    return bspline_eval(s ,P)

# end

# function s = sum_pair_dist(D)
def sum_pair_dist(D):
# x1 = D(1:end -1,:);
    x1 = D[0:-1, :]

    # x2 = D(2:end,:);
    x2 = D[1:,:]

    # z = sqrt(sum((x 1 -x2) . ^2 ,2));
    z = np.sqrt(sum(np.power(x1 -x2, 2 ,2)))

    # s = sum(z);
    return sum(z)

# end