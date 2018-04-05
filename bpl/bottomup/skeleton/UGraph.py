import numpy as np


class UGraph:


    def __init__(self, G, E, EI, S, I):
        self.G = G
        self.E = E
        self.EI = EI
        self.S = S
        self.I = I

        # load('circle_masks', 'list_mask');
        # this.list_mask = list_mask;


    def getN(self):
        return self.G[0]

    def getImsize(self):
        return self.I[0]

    def getLink_ei_to_ni(self):
        k = len(self.S)
        Y = np.zeros(k, 2)

        for i in 1..k:
            source_pt = self.S[i][0, :]
            dest_pt = self.S[i][-1, :]
            source_ni = self.map_pts_to_ni(source_pt)
            dest_ni = self.map_pts_to_ni(dest_pt)
            Y[i, 0] = source_ni
            Y[i, 1] = dest_ni


