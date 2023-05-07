#!/usr/bin/env python3

import numpy as np
import pyvista as pv

#=======================================================================================
# test superQuadric function
#=======================================================================================
def test_superquadric( f ):

    ## test cases ##
    try:
        np.testing.assert_almost_equal( f( [0,0,0] ), 0.0, decimal=6, err_msg="Failed case 1: superQuadric( [0,0,0] ):", verbose=True )
        np.testing.assert_almost_equal( f( [1,1,1] ), 1.7320508075688772, decimal=6, err_msg="Failed case 2: superQuadric( [1,1,1] ):", verbose=True )
        np.testing.assert_almost_equal( f( [-5,-6,-777], [1,1,1], [3,3,3] ), 21658.665101986317, decimal=6, err_msg="Failed case 3: superQuadric( [-5,-6,-777], [1,1,1], [3,3,3] ):", verbose=True )
        np.testing.assert_almost_equal( f( [-1,-2,-100], [4,0.5,12], [7,0.25,14] ), 2790816.4723367887, decimal=6, err_msg="Failed case 4: superQuadric( [-1,-2,-100], [4,0.5,12], [7,0.25,14] )", verbose=True )
        np.testing.assert_almost_equal( f( [-5,-6,-777]  ), 777.0392525477719, decimal=6, err_msg="Failed case 5: superQuadric( [-5,-6,-777]  ):", verbose=True )
        np.testing.assert_almost_equal( f( [0,0,0], [4,2,1], [-3,-1,-5]  ), 0.0, decimal=6, err_msg="Failed case 6: superQuadric( [0,0,0], [4,2,1], [-3,-1,-5]  ):", verbose=True )
        np.testing.assert_almost_equal( f( [-1,-1,-1], [4,2,1], [-3,-1,-5]  ), 8.18535277187245, decimal=6, err_msg="Failed case 7: superQuadric( [-1,-1,-1], [4,2,1], [-3,-1,-5]  ):", verbose=True )
        
    except Exception as e:
        print( e )
        return

    print( "superQuadric() tests succeeded" )
    return
    
#=======================================================================================
# test scalarField class
#=======================================================================================
def test_scalarfield( sf, p ):

    ### test cases: Pole() ###
    try:
        pole = p( 1, 2, 3, 4 )
        np.testing.assert_almost_equal( pole.getValue(), 4, err_msg="Failed case 1: p = Pole( 1, 2, 3, 4 ), p.getValue()", verbose=True )
        np.testing.assert_almost_equal( pole.getVector(), [1,2,3], err_msg="Failed case 2: p = Pole( 1, 2, 3, 4 ), p.getVector()", verbose=True )
        pole.setValue( -3.1415928 )
        np.testing.assert_almost_equal( pole.getValue(), -3.1415928, err_msg="Failed case 3: p = Pole.setValue( -PI ), p.getValue()", verbose=True )
    except Exception as e:
        print( e )
        return

    print( "Pole() tests succeeded")

    ### test cases: ScalarField() ###
    try:
        field = sf(4,4,4)
        np.testing.assert_almost_equal( field.dimension, [5,5,5], err_msg="Failed case 4: sf = ScalarField( [4,4,4] ), sf.dimension", verbose=True )

        field = sf(-4,4,4)
        np.testing.assert_almost_equal( field.dimension, [1,5,5], err_msg="Failed case 5: sf = ScalarField( [-4,4,4] ), sf.dimension", verbose=True )

        field = sf( 4,4,4 )
        pole = p( 1,2,3,4)
        field.setVertex( 1,1,1, pole )
        poleOut = field.getVertex(1,1,1)
        np.testing.assert_almost_equal( poleOut.getValue(),  4,       err_msg="Failed case 6: sf = ScalarField( [4,4,4] ), p = Pole( 1,2,3,4 ), p2 = sf.setVertex( 1,1,1, p ), p2.getValue()", verbose=True )
        np.testing.assert_almost_equal( poleOut.getVector(), [1,2,3], err_msg="Failed case 7: sf = ScalarField( [4,4,4] ), p = Pole( 1,2,3,4 ), p2 = sf.setVertex( 1,1,1, p ), p2.getVector()", verbose=True )
    except Exception as e:
        print( e )
        return

    print( "ScalarField() tests succeeded" )
    return


#===============================================================================================
# test createScalarField()
#===============================================================================================
def test_createScalarField( csf, test_mode ):


    if test_mode == 0:
        field = csf()

        try:
            ### low resolution field ###
            pole = field.getVertex( 20, 20, 20 )
            # print( "v: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [0.0,0.0,0.0], decimal=6, err_msg="Failed case 1: sf = createScalarField(), p = f.getVertex( 20, 20, 20 ), p.getVector()", verbose=True )
            np.testing.assert_almost_equal( pole.getValue(), 0.0, decimal=6, err_msg="Failed case 2: sf = createScalarField(), p = f.getVertex( 20, 20, 20 ), p.getValue()", verbose=True )
            print( "test center point succeeded" )

            pole = field.getVertex( 40, 40, 40 )
            # print( "v: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [5,5,5], decimal=6, err_msg="Failed case 3: sf = createScalarField(), p = f.getVertex( 40, 40, 40 ), p.getVector()", verbose=True )
            np.testing.assert_almost_equal( pole.getValue(), 8.660254037844387, decimal=6, err_msg="Failed case 4: sf = createScalarField(), p = f.getVertex( 40, 40, 40 ), p.getValue()", verbose=True )
            print( "test corner grid point succeeded" )

            field = csf( 0.667, [-5,-5,-5], [5,5,5], [4,2,1], [0.1, 8, 4] )
            pole = field.getVertex( 3, 2, 2 )
            # print( "v: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [-2.857142857142857, -3.5714285714285716, -3.5714285714285716], decimal=6, 
            err_msg="Failed case 5: sf = createScalarField( 0.667, [-5,-5,-5], [5,5,5], [4,2,1], [0.1, 8, 4] ), p = f.getVertex( 3,2,2 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(), 16.34177612693006, decimal=6, 
            err_msg="Failed case 6: sf = createScalarField( 0.667, [-5,-5,-5], [5,5,5], [4,2,1], [0.1, 8, 4] ), p = f.getVertex( 3,2,2 ), p.getValue()", verbose=True )
            
            print( "test random position 1 succeeded" )

            pole = field.getVertex( 13, 9, 4 )
            # print( "v: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [4.2857142857142865, 1.4285714285714288, -2.1428571428571432], decimal=6, 
            err_msg="Failed case 7: sf = createScalarField( 0.667, [-5,-5,-5], [5,5,5], [4,2,1], [0.1, 8, 4] ), p = f.getVertex( 13,9,4 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(), 4.7074035414110575, decimal=6, 
            err_msg="Failed case 8: sf = createScalarField( 0.667, [-5,-5,-5], [5,5,5], [4,2,1], [0.1, 8, 4] ), p = f.getVertex( 13,9,4 ), p.getValue()", verbose=True )
            print( "test random position 2 succeeded" )
        except Exception as e:
            print( e )
            return
            
            
    elif test_mode == 1:
    
        # [101, 51, 82]
        ### medium resolution field ### 
        field = csf( 0.15, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] )
        try:
            pole = field.getVertex( 50, 25, 41 )
            # print( "v0: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [2.5, 1.75, 6.200617283950617], decimal=6, 
            err_msg="Failed case 9: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 50, 25, 41 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(), 1.1761760359000197, decimal=6, 
            err_msg="Failed case 10: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 50, 25, 41 ), p.getValue()", verbose=True )
            print( "test center point succeeded" )

            pole = field.getVertex( 0, 0, 0 )
            # print( "v1: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [-5.0, -2.0, 0.0], decimal=6, 
            err_msg="Failed case 11: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 0,0,0 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(),  1.4078114378573263, decimal=6, 
            err_msg="Failed case 12: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 0,0,0 ), p.getValue()", verbose=True )
            print( "test lower corner succeeded" )

            pole = field.getVertex( 100, 50, 81 )
            # print( "v2: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [10.0, 5.5, 12.25], decimal=6, 
            err_msg="Failed case 13: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 100, 50, 81 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(), 3.743757874457781e+17, decimal=2, 
            err_msg="Failed case 14: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 100, 50, 81 ), p.getValue()", verbose=True )
            print( "test upper corner succeeded" )

            pole = field.getVertex( 37, 48, 13 )
            # print( "v3: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [0.5499999999999998, 5.199999999999999, 1.9660493827160495], decimal=6, 
            err_msg="Failed case 15: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 37, 48, 13 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(), 3.9713111838963384e+16, decimal=6, 
            err_msg="Failed case 16: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 37, 48, 13 ), p.getValue()", verbose=True )
            print( "test random position succeeded" )
            
        except Exception as e:
            print( e )
            return
            
    elif test_mode == 2:
        
        # [300,150,245]
        ### high resolution field ### 
        field = csf( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] )
        try:
            pole = field.getVertex( 150, 75, 123 )
            # print( "v0: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [2.5, 1.75, 6.15], decimal=6, 
            err_msg="Failed case 9: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 150,75,123 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(), 1.1697523792416138, decimal=6, 
            err_msg="Failed case 10: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 150,75,123 ), p.getValue()", verbose=True )
            print( "test center point succeeded" )

            pole = field.getVertex( 0, 0, 0 )
            # print( "v1: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [-5.0, -2.0, 0.0], decimal=6, 
            err_msg="Failed case 11: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 0,0,0 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(),  1.4078114378573263, decimal=6, 
            err_msg="Failed case 12: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 0,0,0 ), p.getValue()", verbose=True )
            print( "test lower corner succeeded" )

            pole = field.getVertex( 300, 150, 245 )
            # print( "v2: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [10.0, 5.5, 12.25], decimal=6, 
            err_msg="Failed case 13: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 300, 150, 245 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(), 374375787445778100, decimal=2, 
            err_msg="Failed case 14: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 300, 150, 245 ), p.getValue()", verbose=True )
            print( "test upper corner succeeded" )

            pole = field.getVertex( 137, 21, 85 )
            # print( "v3: ", pole.getVector(), pole.getValue() )
            np.testing.assert_array_almost_equal( pole.getVector(), [1.8500000000000005, -0.95, 4.25], decimal=6, 
            err_msg="Failed case 15: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 137, 21, 85 ), p.getVector()", verbose=True )
            
            np.testing.assert_almost_equal( pole.getValue(), 0.9960486598671837, decimal=6, 
            err_msg="Failed case 16: f = createScalarField( 0.05, [-5, -2, 0], [10, 5.5, 12.25], [6,2,7.5], [0.1, 80, 4] ), p = f.getVertex( 137, 21, 85 ), p.getValue()", verbose=True )
            print( "test random position succeeded" )
            
        except Exception as e:
            print( e )
            return


    print( "createScalarField() tests succeeded" )

#===============================================================================================
# test Cell()
#===============================================================================================
def test_cell( cell, pole ):

    try:
        # pole test
        c = cell()
        n = 10
        values    = []
        positions = []
        for i in range( 0, n ):
            v = np.random.rand()
            p = pole( i+1, i+2, i+3, v )
            values.insert( i, v )
            positions.insert( i, [i+1,i+2,i+3] )
            c.addPole( p )
        np.testing.assert_almost_equal( c.Count, n, err_msg="Failed case 1: Cell.Count", verbose=True )
        np.testing.assert_almost_equal( c.values, values, err_msg="Failed case 2: Cell.values", verbose=True )
        np.testing.assert_array_almost_equal( c.positions, positions, err_msg="Failed case 3: Cell.positions", verbose=True )
            
        # edgemap test
        cellA = cell()
        cellB = cell()
        cellC = cell()

        for i in range( 0, 19 ):
            cellA.edgeMap[i] = i
            cellB.edgeMap[i] = i
            cellC.edgeMap[i] = i

        c = cell()
        c.edgeMap = [-1,-2,-3,-4, -5,-6,-7,-8, -9,-10,-11,-12, -13,-14,-15, -16,-17,-18, -19]
        c.copyEdgeMap( cellA, cellB, cellC )
        np.testing.assert_almost_equal( c.edgeMap, [4, 5, 6, 7, 6, -6, -7, 5, 11, 10, -11, 10, 15, 17, 16, -16, -17, -18, -19], err_msg="Failed case 4: Cell.edgeMap", verbose=True )
    except Exception as e:
        print( e )
        return
    
    print( "cell tests succeeded" )



	
def test_evalTetra_range( f, tetraIndex, bitCode, failMessage ):

    try:
        aPolygons = f( tetraIndex, bitCode )
    except Exception as e:
        print( "  Error: evalTetra( " + str(tetraIndex) + ", " + str(bitCode) + " ) " + failMessage )
        return True
        
    if aPolygons != []:
        print( "  Error: evalTetra( " + str(tetraIndex) + ", " + str(bitCode) + " ) returns non-empty polygon list" )
        return True
        
    return False
	
def test_evalTetra( f ):
    # bitcodes to test: -10, 3, 13, 72, 192, 236, 255, 1000
    
    a = [-99999,-10,-1,6,7,10,99999]
    b = [10]*len(a)
    
    # tetrahedron index validation
    message = "- invalid tetrahedron index"   
    for i in range(0,len(a),1):
        if test_evalTetra_range( f, a[i], b[i], message ):
            return

    b = [-99999,-255,-1,256,999999] 
        
    # bitcode validation
    message = "- invalid bitcode"
    for i in range(0,len(b),1):
        if test_evalTetra_range( f, i, b[i], message ):
            return
        
    print( "test bounds succeeded" )
            
    # polygon connectivity validation
    c = [1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,2,2,1,0,0,1,1,0,0,1,1,2,2,1,1,0,0,1,2,1,0,1,1,2,1,2,1,0,1,1,0,0,0,1,2,2,1,1,1,0,1,1,1,1,0,1,2,2,2,2,1,0,1,2,1,0,0,1,2,1,2,1,1,0,1,2,2,1,0,1,2,1,1,2,1,1,0,0,0,0,1,2,1,1,1,1,2,1,0,0,1,1,1,2,1,1,2,2,2,1,0,1,1,0,1,2,1,2,2,1,2,1,0,1,2,1,1,2,1,2,1,2,2,1,1,1,0,0,1,2,2,2,1,1,2,1,1,1,1,1,1,2,2,2,2,2,2,1,1,2,1,0,1,2,2,1,2,1,2,1,1,2,2,1,1,2,2,1,1,2,2,0,0,0,0,1,1,1,1,1,1,2,2,0,0,0,1,2,1,1,1,1,2,1,2,0,0,1,1,1,1,1,1,2,2,2,2,0,0,1,2,2,1,1,1,2,1,1,2,0,1,1,0,1,1,1,2,2,1,2,2,0,1,1,1,2,1,1,2,2,2,1,2,0,1,2,1,1,1,1,2,1,2,2,2,0,1,2,2,2,1,1,2,1,1,1,2,1,0,0,0,1,2,2,1,1,1,2,1,1,0,0,1,2,2,2,1,1,2,1,1,1,0,1,1,1,2,2,1,2,2,2,1,1,0,1,2,2,2,2,1,2,1,1,1,1,1,1,0,1,2,2,2,2,1,2,1,1,1,1,1,2,2,2,2,2,2,1,1,1,1,2,1,1,2,2,2,1,2,2,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,1,1,1,2,2,1,2,2,2,1,1,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,1,2,1,2,2,1,0,1,2,1,2,2,1,1,1,2,1,1,2,2,2,1,2,2,2,2,1,2,1,1,1,1,2,1,2,1,2,1,1,2,1,0,1,2,2,1,2,1,1,2,1,2,1,0,0,1,2,2,1,1,1,1,2,1,2,2,2,2,1,2,1,1,2,2,2,1,2,2,1,1,1,2,1,2,2,1,2,1,2,1,1,2,1,2,1,2,1,2,2,1,2,1,0,1,1,2,2,2,1,1,2,1,1,1,2,2,1,2,2,2,2,2,2,1,1,1,1,1,1,2,2,1,2,1,2,1,1,0,1,2,1,2,2,1,1,2,2,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,2,1,2,2,2,2,1,0,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,2,1,1,2,2,2,1,0,0,1,1,2,2,1,2,2,2,1,1,2,1,1,1,2,2,2,1,2,2,1,1,1,0,1,1,2,1,2,2,2,2,1,0,1,1,1,1,2,1,1,1,2,2,1,0,0,0,1,2,1,1,1,2,1,1,2,2,2,1,0,2,1,1,2,1,1,1,2,2,1,0,0,2,1,2,2,2,1,1,2,1,1,1,0,2,1,2,1,1,1,1,2,1,0,0,0,2,2,2,1,2,1,1,1,1,2,1,0,2,2,2,2,1,1,1,1,1,1,0,0,2,2,1,2,2,1,1,1,0,1,1,0,2,2,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,2,2,1,1,1,1,1,1,0,1,1,0,2,2,1,2,2,1,1,1,1,1,0,0,2,2,2,2,1,1,1,1,1,2,1,0,2,2,2,1,2,1,1,2,1,0,0,0,2,1,2,1,1,1,1,2,1,1,1,0,2,1,2,2,2,1,1,2,2,1,0,0,2,1,1,2,1,1,1,2,2,2,1,0,2,1,1,1,2,1,2,1,0,0,0,1,1,2,1,1,1,2,2,1,0,1,1,1,1,2,1,2,2,2,2,1,1,1,0,1,1,2,2,2,1,2,2,1,1,2,1,1,1,2,2,1,2,2,2,2,1,0,0,1,1,1,2,1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,1,0,1,1,1,1,2,1,2,2,2,2,2,1,1,1,1,1,1,2,2,1,1,0,0,1,1,2,2,1,1,2,2,1,1,0,1,2,1,2,2,1,2,1,2,1,1,1,1,1,1,2,2,2,2,2,2,1,1,1,2,2,1,2,2,2,1,1,2,1,2,1,0,1,1,2,1,2,1,2,2,1,2,1,1,2,1,2,1,2,2,1,2,1,2,2,1,1,1,2,1,1,2,2,2,1,2,2,2,2,1,2,1,1,1,1,2,2,1,0,0,1,2,1,2,1,1,2,1,2,1,0,1,2,2,1,2,1,2,1,1,2,1,1,1,1,2,1,2,2,2,2,1,2,1,1,2,2,2,1,2,2,1,1,1,2,2,1,0,1,2,1,1,2,1,2,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,2,1,1,2,1,1,1,2,2,1,2,2,2,2,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2,2,2,2,2,2,1,2,2,1,1,1,2,1,1,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,1,2,1,1,1,1,0,1,2,2,1,2,1,1,1,1,0,1,2,2,2,2,1,2,2,2,1,1,0,1,1,1,2,2,1,1,2,1,1,1,0,0,1,2,2,2,1,1,1,2,1,1,0,0,0,1,2,1,2,1,1,1,2,0,1,2,2,2,1,1,2,1,2,2,2,0,1,2,1,1,1,1,2,2,2,1,2,0,1,1,1,2,1,1,2,2,1,2,2,0,1,1,0,1,1,1,1,2,1,1,2,0,0,1,2,2,1,1,1,2,2,2,2,0,0,1,1,1,1,1,1,1,2,1,2,0,0,0,1,2,1,1,1,1,1,2,2,0,0,0,0,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,2,1,2,1,1,2,1,0,1,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,1,1,2,1,1,1,0,0,1,2,1,2,1,2,2,1,0,1,2,1,1,2,1,2,2,1,2,1,0,1,1,0,1,2,1,1,2,2,2,1,0,0,1,1,1,2,1,1,1,1,2,1,0,0,0,0,1,1,2,1,1,2,1,0,1,2,2,1,0,1,2,1,2,1,1,0,1,2,1,0,0,1,2,2,2,2,1,0,1,1,1,1,0,1,2,2,1,1,1,0,1,1,0,0,0,1,1,2,1,2,1,0,0,1,2,1,0,1,1,2,2,1,1,0,0,1,1,0,0,1,1,1,2,2,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0]
    n = 0
    for i in range(1,256,1):
        for j in range(0,6,1):
            r = f( j, i )
            if len(r) != c[n]:
                print( "  Error: evalTetra( " + str(j) + ", " + str(i) + " ) returns " + str(len(r)) + " polygons (expected: " + str(c[n]) + ")" )
                return
            n += 1
    print( "test polygon count succeeded" )
                
    # randomly chosen cases
    a = [0,1,2,3,4,5, 0,1,2,3,4,5, 0,1,2,3,4,5, 0,1,2,3,4,5, 0,1,2,3,4,5, 0,1,2,3,4,5, 0,1,2,3,4,5]
    b = [3,3,3,3,3,3, 51,51,51,51,51,51, 72,72,72,72,72,72, 135,135,135,135,135,135, 179,179,179,179,179,179, 211,211,211,211,211,211, 251,251,251,251,251,251 ]
    r = [
        # 3
        [[3, 14, 18, 8]],
        [[3, 3, 18, 14]],
        [[3, 18, 3, 12]],
        [[3, 18, 12, 1], [3, 1, 16, 18]],
        [[3, 18, 16, 9], [3, 9, 13, 18]],
        [[3, 18, 13, 8]],
        
        # 51
        [[3, 18, 15, 7], [3, 7, 14, 18]],
        [[3, 3, 18, 14]],
        [[3, 18, 3, 12]],
        [[3, 18, 12, 1], [3, 1, 16, 18]],
        [[3, 18, 16, 5]],
        [[3, 5, 15, 18]],
        
        #72
        [[3, 6, 15, 18]],
        [[3, 11, 6, 18], [3, 18, 3, 11]],
        [[3, 3, 18, 10], [3, 10, 2, 3]],
        [[3, 18, 16, 10]],
        [[3, 5, 16, 18]],
        [[3, 18, 15, 5]],

        # 135
        [[3, 18, 8, 7], [3, 7, 6, 18]],
        [[3, 11, 3, 18], [3, 18, 6, 11]],
        [[3, 3, 2, 10], [3, 10, 18, 3]],
        [[3, 10, 16, 18]],
        [[3, 18, 16, 9], [3, 9, 13, 18]],
        [[3, 18, 13, 8]],
        
        # 179
        [[3, 18, 15, 6]],
        [[3, 11, 3, 18], [3, 18, 6, 11]],
        [[3, 18, 3, 12]],
        [[3, 18, 12, 1], [3, 1, 16, 18]],
        [[3, 18, 16, 5]],
        [[3, 5, 15, 18]],
        
        # 211
        [],
        [[3, 3, 17, 11]],
        [[3, 3, 12, 10], [3, 10, 17, 3]],
        [[3, 12, 1, 10]],
        [[3, 5, 9, 13]],
        [[3, 13, 4, 5]],
        
        # 251
        [],
        [],
        [[3, 10, 2, 12]],
        [[3, 12, 1, 10]],
        [],
        []
    ]
    
    for i in range(0,len(a),1):
        v = f( a[i], b[i] )
        if v != r[i]:
            print( "  Error: evalTetra( " + str(a[i]) + "," + str(b[i]) + " ) produced wrong output:", v )
            return
    print( "test randomly selected cases succeeded" )
    
    
    print( "evalTetra() tests succeeded" )
    
    
def test_isomesh( iso, csf ):

    try:
        field = csf( 1.0, [-5,-5,-5], [5,5,5], [1,1,1], [4,4,4] )
        isoMesh = iso()
        polygonMesh = isoMesh.createIsoSurface( field, 1.0 )

        np.testing.assert_equal( len(polygonMesh.points), 14, err_msg="Failed case 1: Incorrect vertex count",  verbose=True )
        np.testing.assert_equal( polygonMesh.n_faces,     24, err_msg="Failed case 2: Incorrect polygon count", verbose=True )

        ##
        field = csf( 0.25, [-5,-5,-5], [5,5,5], [4,4,4], [4,4,4] )
        isoMesh = iso()
        polygonMesh = isoMesh.createIsoSurface( field, 1.0 )

        np.testing.assert_equal( len(polygonMesh.points), 19022, err_msg="Failed case 3: Incorrect vertex count",  verbose=False )
        np.testing.assert_equal( polygonMesh.n_faces,     38040, err_msg="Failed case 4: Incorrect polygon count", verbose=False )
        
    except Exception as e:
        print(e)
        return
        
    print( "IsoMesh tests succeeded" )


def test_marchingTetra5( iso, csf ):

    try:
        field = csf( 0.25, [-5,-5,-5], [5,5,5], [1,1,1], [2,2,2] )
        isoMesh = iso()
        polygonMesh = isoMesh.createIsoSurface( field, 1.0 )

        #
        np.testing.assert_almost_equal( len( polygonMesh.points ), 1800, err_msg="Incorrect vertex count",  verbose=True )
        np.testing.assert_almost_equal( polygonMesh.n_faces,       1256, err_msg="Incorrect polygon count", verbose=True )
        
    except Exception as e:
        print(e)
        return
        
        
    print( "tests succeeded" )
