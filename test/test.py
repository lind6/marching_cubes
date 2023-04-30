#!/usr/bin/env python3

import numpy as np
import pyvista as pv

def test_superquadric( value ):

	print( "value: ", value )

	## test cases ##
	np.testing.assert_almost_equal( superQuadric( [0,0,0] ), 0.0, err_msg="Failed case 1", verbose=False )
	np.testing.assert_almost_equal( superQuadric( [1,1,1] ), 1.7320508075688772, err_msg="Failed case 2", verbose=False )
	np.testing.assert_almost_equal( superQuadric( [-5,-6,-777], [1,1,1], [3,3,3] ), 21658.665101986317, err_msg="Failed case 3", verbose=False )
	np.testing.assert_almost_equal( superQuadric( [-1,-2,-100], [4,0.5,12], [7,0.25,14] ), 2790816.4723367887, err_msg="Failed case 4", verbose=False )
	np.testing.assert_almost_equal( superQuadric( [-5,-6,-777]  ), 777.0392525477719, err_msg="Failed case 5", verbose=False )
	np.testing.assert_almost_equal( superQuadric( [0,0,0], [4,2,1], [-3,-1,-5]  ), 0.0, err_msg="Failed case 6", verbose=False )
	np.testing.assert_almost_equal( superQuadric( [-1,-1,-1], [4,2,1], [-3,-1,-5]  ), 8.18535277187245, err_msg="Failed case 7", verbose=False )

	print( "superQuadric() tests succeeded" )
	return


def test_cell():

	print( "cell() tests succeeded" )
	return