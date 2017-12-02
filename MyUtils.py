import numpy as np

import torch

import matlab.engine

# Take a matlab Double matrix and convert to DoubleTensor
# Helps conversion of data returned from matlab engine

def mat2tensor(mat):

    if isinstance(mat, matlab.double):
        return torch.DoubleTensor(mat)

    # if wrapped in list, return list of DoubleTensors
    elif isinstance(mat, list):
        tlist = []
        for m in mat:
            tlist.append(torch.DoubleTensor(m))

        return tlist

    # if scalar, wrap in tensor
    else:
        return torch.DoubleTensor([mat])


