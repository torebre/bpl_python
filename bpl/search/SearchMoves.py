


class SearchMoves:
    MAX_NS_ALL_PERM = 6
    searchPM = {}

    def __init__(self, Minit, lib, verbose = False, fast_mode = False):

        if fast_mode:
            self.MAX_NS_ALL_PERM = self.MAX_NS_ALL_PERM - 2

        self.M = Minit
        self.searchPM.update({"lib": lib})
        self.searchPM.update({"verbose": verbose})
        self.searchPM.update({"fast_mode": fast_mode})
        self.searchPM.update({"MAX_NS_ALL_PERM": lib})


    def move_opt_subids(self, list_sid):
        if list_sid is not None:
            optimize_subids(self.searchPM, self.M, list_sid)
        else:
            optimize_subids()



    def optimize_subids(self, searchPM, Q, list_sid):
        if list_sid is None:
            list_sid = range(0, Q.ns)

        for sid in list_sid:
            if searchPM["verbose"]:
                print("choose subid for stroke: ", sid)

            optimize_this_subid(Q, sid, searchPM["lib"], searchPM["verbose"])



    