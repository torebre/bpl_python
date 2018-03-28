



# function P = fit_bspline_to_traj(stk,nland)
def fit_bspline_to_traj(stk, nland):
    # neval = length_stk(stk);
    neval = length_stk(stk)

    # s = bspline_gen_s(nland,neval);
    s = bspline_gen_s(nland, neval)

    # P = bspline_fit(s,stk,nland);
    P = bspline_fit(s, stk, nland)

# end