
import sys

import torch

import CPD

def scoreMP(M, libclass):
    # Score a MotorProgram
    # log-probability score as in Equation 1 in the main text
    # Input
    #   M: motor program
    #   libclass: object of type LibraryClass

    # By default, it includes all components of the log-score.
    # To choose only specific components, you can use this syntax:
    #   'token',true,'type',true,'image',true,'stat',true
    # For the token, type, and image model respectively set to true or
    # false. 'stat' is only needed for alphabet model, which is not
    # included here and should not be used.
    # Output
    #   score : score
    #   out : struct that breaks down the score by component

    # list of stroke ids
    list_sid = range(0,M.ns)

    #PM = M.parameters;

    out = []

    # score for number of strokes
    out.append(CPD.score_number(libclass,M.ns))

    for i in list_sid:
        MS = M.S[i]

        # score for number of sub-strokes given no. of strokes
        out.append( CPD.score_sequence(libclass,M.ns,MS.ids) )

        # score for
        out.append( CPD.score_invscale_type(libclass,MS.invscales_type,MS.ids) );
        #out.S{i}.relation = CPD.score_relation_type(libclass,MS.R);
            #if ~isempty(MS.shapes_type)
               #out.S{i}.shape_type = CPD.score_shape_type(libclass,MS.shapes_type,MS.ids);

       #token-level scores

    # #token-level image variables


    # # score the image
    # if inc_image
    #     out.image = CPD.score_image(M.I,M.pimg);
    # end

    # sum all scores
    return sum(out)

    # if isnan(score)
    #    assert(false);
    # end



