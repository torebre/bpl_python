import numpy as np

from bpl.classes import MotorProgram



class MotorProgramFit(MotorProgram):

    def __init__(self, TypeSamples):
        nsamp = len(TypeSamples)

        anchor = TypeSamples[0].deepcopy()
        super(self, anchor.ns)

        self.A = anchor.A
        self.epsilon = anchor.epsilon
        self.blur_sigma = anchor.blur_sigma
        self.parameters = anchor.parameters

        for sid in 0..self.ns:
            stk = anchor.S[sid]
            self.S[sid].pos_token = stk.pos_token
            self.S[sid].shapes_token = stk.shapes_token
            self.S[sid].invscales_token = stk.invscales_token

            if(stk.R.type == 'mid'):
                self.S[sid].R = stk.R


        self.TypeS = np.array((nsamp, self.ns))

        for i in 0..nsamp:
            for sid in 0..self.ns:
                self.TypeS[i, sid] = TypeSamples[i].S[sid].myType.copy()


        # TODO assert (checkSampleSameRelations(this));

        for sid in 0..self.ns:
            self.list_typeR[sid] = self.TypeS[0, sid].R.type


        clearSampleType(self)