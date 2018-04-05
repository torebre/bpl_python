import numpy as np




class MCMC:



    def __init__(self, debug_full_score = False):
        self.debug_full_score = debug_full_score



    def mh_shape_type(self, sid, bid, M, lib):

        # Make proposal
        curr_shape_type = M.S[sid].shapes_type[:, :, bid]
        prop_shape_type = propose_shape_type(M, sid, bid, lib, M.parameters)

        # Score proposal
        curr_score = score_shape_type(M, sid, bid, lib, M.parameters)
        if self.debug_full_score:
            curr_score2 = score_shape_type(M, sid, bid, lib, M.parameters)

        M.S[sid].shapes_type[:, :, bid] = prop_shape_type
        prop_score = score_shape_type(M, sid, bid, lib, M.parameters, True)

        if not np.