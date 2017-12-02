
import sys

import torch

class MotorProgram:

    def __init__(self, ns):
        self.I = torch.ByteTensor([]) # binary image (true means 'ink')
        self.S = [] # list of stroke objects
        self.parameters = [] # fixed params (not random variables)
        #self.lh # listener handles (does this make sense in Python?)
        self.epsilon = 0 # noise on pixels
        self.blur_sigma = 0 # image blur
        A = torch.FloatTensor([]) # affine transofrmation
        self.ns = ns # no. of strokes
        self.pimg = torch.FloatTensor([]) # prob of inking each pixel
        self.ink_off_page = 0 # is any ink drawn off page?
        self.motor = [] # nested cell array of trajectories
        self.motor_warped = [] # same as motor, except affine warp
