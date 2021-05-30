## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import numpy, sys
import Cost, GradientDescent,training

def logisticUpDown():
    # Read the the csv whith the training information
    X,Y = training.readArribaAbajo()

    cost = Cost.MaximumLikelihood( X, Y )
    
    [ W, b, nIter ] = GradientDescent.Solve(
        cost,
        learning_rate = 1e-6,
        max_iterations = 500,
        debug_step = 10
        )
    return [W,b]
def logisticRightLetf():
    # Read the the csv whith the training information
    X,Y = training.readDerecchaIzquierda()

    cost = Cost.MaximumLikelihood( X, Y )
    
    [ W, b, nIter ] = GradientDescent.Solve(
        cost,
        learning_rate = 1e-6,
        max_iterations = 500,
        debug_step = 10
        )
    return [W,b]
    
def logisticOption():
    # Read the the csv whith the training information
    X,Y = training.readOption()

    cost = Cost.MaximumLikelihood( X, Y )
    
    [ W, b, nIter ] = GradientDescent.Solve(
        cost,
        learning_rate = 1e-6,
        max_iterations = 500,
        debug_step = 10
        )
    return [W,b]

## eof - $RCSfile$
