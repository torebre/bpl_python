

def SearchForParse(M, lib, verbose = False, fast_mode = False):
    if M.size == 0:
        return

    if verbose:
        print("searching for parse (BEGINS)\n")

    Do = SearchMoves(M, lib, verbose, fast_mode)
