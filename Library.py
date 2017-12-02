
import sys

import torch
class Library:

    def __init__(self):
        self.shape = [] # .mu,Sigma,mixprob
        self.scale = [] # .theta,minfreq
        self.rel = [] # .sigma_x,sigma_y,mixprob
#        self.Spatial # ref to class
        self.tokenvar = [] # .sigma_shape,sigma_invscale
        self.affine = [] # .mu_scale,mu_xtranslate,mu_ytranslate, Sigma_scale,sigma_xtranslate,sigma_ytranslate
        self.stat = [] # .q_ink_emp,.q_ink_prior,.q_canvas_emp,.q_canvas_prior

        # misc. items
        self.logT = torch.DoubleTensor([])
        self.logStart = torch.DoubleTensor([])
        self.pkappa = torch.DoubleTensor([])
        self.pmat_nsub = torch.DoubleTensor([])
        self.newscale = 0
        self.smooth_bigrams = 0
        self.diagSigma = 1

        self.ncpt = 0 # number of control points
        self.N = 0 # number of primitives
        self.endstate = 0 # the special endstate in the Markov process
