
import sys

class Stroke:

    def __init__(self):
        self.myType = 0 # should be StokeType() object
        # self.lh = 0 # listener handle

        # type-level params
        self.R = torch.DoubleTensor([])
        self.ids = [] #
        self.invscales_type = torch.DoubleTensor([])
        self.shapes_type = torch.DoubleTensor([])

        # token-level params
        self.pos_token = 0  #
        self.invscales_token = 0  #
        self.shapes_token = 0  #

        # fully determined variables given the others
        self.nsub = 0
        self.motor = 0
        self.motor_spline = 0
