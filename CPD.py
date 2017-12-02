
import sys
import numpy as np
import torch

def score_number(libclass, data):
    # data: vector [n x 1] of number of strokes
    # returns: vector [n x 1] of log-likelihood scores

    # if any(data>length(libclass.pkappa))

    #     ll = -inf;
    #     return
    # end

    # pkappa: [n x 1] probability of each number of strokes (starts at 1)
    return np.log(libclass.pkappa[data-1,0]) # pkappa: probability of each number of strokes (starts at 1)

def score_sequence(libclass, ns, ids):
    #  ids: [k x 1] data sequence
    #  ns: [scalar] how many strokes are in the character. If ns<0, this means to leave out scoring the number of sub-strokes
    #  output is a scalar log-likelihood value

    nsub = ids.size()[0]
    nstate = libclass.N
    return np.log(libclass.pmat_nsub[ns-1,nsub-1]) #[ns x nsub] each row is probability of each number of sub-strokes, for a charater with a certain number of strokes

def score_shape_type(libclass,bspline_stack,subid):
    # Input
        #  subid [k x 1]: the id (index) of the sub-stroke
        #  bspline_stack: (ncpt x 2 x k) shapes of bsplines
        #
    # Output
        #  ll : [k x 1]: vector of scores

    #mu = Variable(mymu) # wrap mean in pyro Variable
    #sigma = Variable(mysd) # wrap variance in pyro Variable
    #vbspline = Variable(vbspline) # wrap substroke spline in pyro Variable
    #log_p_vbspline = dist.normal.batch_log_pdf(vbspline, mu, sigma)

    print('TODO: implement the score_shape_type function from BPL MATLAB code (Lake et al.)')

def score_shape_marginalize(libclass,bspline_stack_token,subid):
    # Input
        #  subid [k x 1]: the id (index) of the sub-stroke
        #  bspline_stack: (ncpt x 2 x k) shapes of bsplines
        #
    # Output
        #  ll : [k x 1]: vector of scores

    # Score a parsed substroke spline for each of the primitives i.e. to compute its log probability according to the distribution N(mu,sigma)

    log_p_vbspline = dist.normal.batch_log_pdf(vbspline, mu, sigma)

    print('TODO: implement the score_shape_marginalize function from BPL MATLAB code (Lake et al.)')


def score_invscale_type(libclass,invscales_type,subid):
    # Input
        #  subid: [k x 1] vector of sub-stroke ids

    #assert(isvector(invscales_type));
    #assert(isvector(subid));
    # k = subid.size()[0];
    #assert(numel(invscales_type)==k);

    #if isunif(libclass)
    #    lprob = CPDUnif.score_invscale_type(libclass,invscales_type,subid);
    #    return

    theta = libclass.scale.theta[subid]

    return dist.batch.batch_log_pdf(invscales_type,theta[1],theta[2])

def score_invscale_token(libclass,invscales_token,invscales_type):
    # Score the token-level inverse scales.
    # Computes the right normalization constant, since negative values are not allowed.
    # Input
        # invscales_token: [n x 1] vector
        # invscales_type: [n x 1] vector
    # Output
        # ll: [n x 1] vector of log-likelihood

    print('TODO: implement the score_invscale_token function from BPL MATLAB code (Lake et al.)')

def score_image(I, pimg):
    # Score the image model

    print('TODO: implement the score_image function from BPL MATLAB code (Lake et al.)')
