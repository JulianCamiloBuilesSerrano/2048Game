## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import numpy, sys

## -------------------------------------------------------------------------
'''
'''
class MSE:

  '''
  '''
  def __init__( self, in_X, in_y ):
    assert isinstance( in_X, ( list, numpy.matrix ) ), "Invalid X type."
    assert isinstance( in_y, ( list, numpy.matrix ) ), "Invalid y type."
    
    if type( in_X ) is list:
      X = numpy.matrix( in_X )
    else:
      X = in_X
    # end if
    if type( in_y ) is list:
      y = numpy.matrix( in_y ).T
    else:
      y = in_y
    # end if
    assert X.shape[ 0 ] == y.shape[ 0 ], "Invalid X,y sizes."
    assert y.shape[ 1 ] == 1, "Invalid y size."

    self.m_M = X.shape[ 0 ]
    self.m_N = X.shape[ 1 ]

    self.m_XtX = ( X.T / float( self.m_M ) ) @ X
    self.m_Xby = ( numpy.array( X ) * numpy.array( y ) ).mean( axis = 0 )
    self.m_uX = X.mean( axis = 0 )
    self.m_uy = y.mean( )
    self.m_yty = ( y.T / float( self.m_M ) ) @ y
  # end def

  def NumberOfExamples( self ):
    return self.m_M
  # end def

  def VectorSize( self ):
    return self.m_N
  # end def

  '''
  '''
  def AnalyticSolve( self ):
      x = numpy.append( self.m_Xby, numpy.array( [ self.m_uy ] ), axis = 0 )
      B = numpy.append( self.m_uX, numpy.matrix( [ 1 ] ), axis = 1 )
      A = numpy.append( self.m_XtX, self.m_uX.T, axis = 1 )
      A = numpy.append( A, B, axis = 0 )
      Wb = x @ numpy.linalg.inv( A )
      return [ Wb[ :, 0 : Wb.shape[ 1 ] - 1 ], Wb[ : , -1 ] ]
  # end def

  '''
  '''
  def CostAndDerivatives( self, W, b ):
    J = \
      ( W @ self.m_XtX @ W.T ) + \
      ( 2.0 * b * ( W @ self.m_uX.T ) ) + \
      ( b * b ) - \
      ( 2.0 * ( W @ self.m_Xby.T ) ) - \
      ( 2.0 * b * self.m_uy ) + \
      self.m_yty
    dW = 2.0 * ( ( W @ self.m_XtX ) + ( b * self.m_uX ) - self.m_Xby )
    db = 2.0 * ( ( W @ self.m_uX.T ) + b - self.m_uy )
    return [ J, dW, db ]
      
  # end def
# end class

## -------------------------------------------------------------------------
'''
'''
class MaximumLikelihood:

  '''
  '''
  def __init__( self, in_X, in_y ):
    assert isinstance( in_X, ( list, numpy.matrix ) ), "Invalid X type."
    assert isinstance( in_y, ( list, numpy.matrix ) ), "Invalid y type."
    
    if type( in_X ) is list:
      self.m_X = numpy.matrix( in_X )
    else:
      self.m_X = in_X
    # end if
    if type( in_y ) is list:
      self.m_y = numpy.matrix( in_y ).T
    else:
      self.m_y = in_y
    # end if
    assert self.m_X.shape[ 0 ] == self.m_y.shape[ 0 ], "Invalid X,y sizes."
    assert self.m_y.shape[ 1 ] == 1, "Invalid y size."

    self.m_M = self.m_X.shape[ 0 ]
    self.m_N = self.m_X.shape[ 1 ]

    self.m_Xby = \
      ( numpy.array( self.m_X ) * numpy.array( self.m_y ) ).mean( axis = 0 )
    self.m_uy = self.m_y.mean( )
  # end def

  def NumberOfExamples( self ):
    return self.m_M
  # end def

  def VectorSize( self ):
    return self.m_N
  # end def

  '''
  '''
  def CostAndDerivatives( self, W, b ):
    Z = ( self.m_X @ W.T ) + b
    H = 1.0 / ( 1.0 + numpy.exp( -Z ) )
    m = float( self.m_M )

    e = sys.float_info.epsilon
    J = 0.0
    J  = numpy.log( 1.0 - H[ self.m_y[ :, 0 ] == 0 ] + e ).sum( ) / m
    J += numpy.log( H[ self.m_y[ :, 0 ] == 1 ] + e ).sum( ) / m

    dW = \
      ( numpy.array( self.m_X ) * numpy.array( H ) ).mean( axis = 0 ) - \
      self.m_Xby

    db = H.mean( axis = 0 ) - self.m_uy

    return [ -J, dW, db ]
      
  # end def
# end class

## eof - $RCSfile$
