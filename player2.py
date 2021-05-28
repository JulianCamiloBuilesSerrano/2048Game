def ecuation( W, b, X ):
  return ( 1.0 / ( 1.0 + numpy.exp( -( ( W @ X ) + b ) ) ) )[ 0 ]
#end def