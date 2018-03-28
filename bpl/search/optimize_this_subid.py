import numpy as np



def optimize_this_subid(Q, sid, lib, verbose = False):

    iter = 0
    nsub = Q.S[sid].nsub
    bool_change = np.ones(nsub, dtype = bool)

    while np.any(bool_change) and iter < 10:
        for bid in range(0, nsub):
            score = score_all_subid(Q, sid, bid, lib)
            curr_id = Q.S[sid].ids(bid)
            new_id = np.argmax(score)
            Q.S[sid].ids(bid) = new_id
            bool_change[bid] = curr_id != new_id

        if nsub == 1:
            bool_change = False

        if verbose:
            print("iter: ", iter)

        iter = iter + 1

