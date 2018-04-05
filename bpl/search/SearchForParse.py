

def SearchForParse(M, lib, verbose = False, fast_mode = False):
    if M.size == 0:
        return

    if verbose:
        print("searching for parse (BEGINS)\n")

    Do = SearchMoves(M, lib, verbose, fast_mode)
    Do.disp_score()

    Do.move__opt_grad()

    Do.move_opt_subids()
    Do.disp_score()

    Do.move_opt_dir_order_rel()

    Do.move_split_merge()

    M = Do.M

    if verbose:
        print("searching for parse (ENDS)\n")

    return M
