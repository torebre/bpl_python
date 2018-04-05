import numbers
import numpy as np

from bpl.classes import Stroke


class MotorProgram:

    def __init__(self, arg):
        self.refresh_listener()

        if isinstance(arg, numbers.Number):
            self.ns = arg  # number of strokes
            self.S = np.zeros([self.ns, 1])
            for i in 1..self.ns:
                self.S[i] = Stroke()
        elif isinstance(arg, MotorProgram):
            Template = arg
            self.S = np.array([Template.ns, 1])

            for i in 1..Template.ns:
                self.S[i] = Stroke(Template.S[i])

            self.parameters = Template.parameters
        else:
            # TODO Is this the correct exception to use?
            raise NameError("Unexpected input to constructor")

    def has_relations(self, list_sid):

        if list_sid is None:
            list_sid = 1..self.ns

        present = np.zeros(len(list_sid))
        count = 1

        for sid in list_sid:
            present[count] = self.S[sid].R is None
            count = count + 1

        present_sum = sum(present)

        if present_sum == 0:
            return False
        elif present_sum == len(present):
            return True
        else:
            raise NameError("All relations should be present or not")


    def lightweight(self):
        self.cache_pimg = []
        self.I = []
        self.cache_noise_current = False


    def clear_shapes_type(self):
        for sid in 1..self.ns:
            self.S[sid].shapes_type = []


    # TODO onListener



    def apply_warp(self):
        motor_unwarped = self.motor
        if self.A is None:
            motor_warped = motor_unwarped
            return

        cell_traj = UtilMP.flatten_substrokes(motor_unwarped)
        com = com_char(cell_traj)
        B = np.zeros([4, 1])
        B[0:1] = self.A[0:1]
        # TODO Probably need to transpose com
        B[2:3] = self.A[2:3].flatten() - (self.A[0:1] - 1).flatten() * com
        motor_warped= UtilMP.apply_each_substroke(motor_unwarped, lambda stk : affine_warp(stk, B))







