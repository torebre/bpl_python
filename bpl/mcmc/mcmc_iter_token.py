




def mcmc_iter_token(MH, M, lib):

    # Shape tokens
    for sid in 0..M.ns:
        for bid in 0..M.S[sid].nsub:
            MH.mh_shape_token(sid, bid, M, lib)

    # Scale tokens
    for sid in 0..M.ns:
        for bid in 0..M.S[sid].nsub:
            MH.mh_scale_token(sid, bid, M, lib)

    for sid in 0..M.ns:
        MH.mh_token_position(sid, M, lib)

    for sid in 0..M.ns:
        if(M.S[sid].R.type == 'mid'):
            MH.mh_eval_spot_token(sid, M, lib)






