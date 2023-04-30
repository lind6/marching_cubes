#!/usr/bin/env python3

import numpy as np
import pyvista as pv

def test_cell():

	print( "cell() tests succeeded" )
	return

def test_adjacent_map( aItems ):

	nbItems = len( aItems )

	for i in range( 0, nbItems ):

		indices = aItems[i]

		if ( len( indices ) != 3 ):
			print( "Adjacent Map test failed: vertex " + str(i) )

		for j in range( 0, len(indices) ):
			# range test
			if indices[j] < 0 or indices[j] > 7:
				print( "Adjacent Map test failed: vertex " + str(i) )

		# similarity test
		if ( indices[0] == indices[1] or indices[0] == indices[2] or indices[1] == indices[2] ):
			print( "Adjacent Map test failed: vertex " + str(i) )

		if i & 1:
			# odd
			if i + 6 != sum( indices ):
				print( "Adjacent Map test failed: vertex " + str(i) )
		else:
			# even
			if i + 8 != sum( indices ):
				print( "Adjacent Map test failed: vertex " + str(i) )

	print( "Adjacent map test succeeded" )
	
def test_adjacent_func( f ):

    # check all success cases
    v1 = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
    v2 = [1,3,4,0,2,5,1,3,6,0,2,7,0,5,7,1,4,6,2,5,7,3,4,6]
    
    for i in range(0, len(v1),1 ):
        if f( v1[i], v2[i] ) == False:
            print( "failed: isAdjacent( " + str(v1[i]) + ", " + str(v2[i]) + " )" )
            return
    
    # check all fail cases
    v1 = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,0,1,2,3,4,5,6,7]
    v2 = [2,5,6,7,3,4,6,7,0,4,5,7,1,4,5,6,1,2,3,6,0,2,3,7,0,1,3,4,0,1,2,5,0,1,2,3,4,5,6,7]
    
    for i in range(0, len(v1),1 ):
        if f( v1[i], v2[i] ) == True:
            print( "failed: isAdjacent( " + str(v1[i]) + ", " + str(v2[i]) + " )" )
            return
            
    print( "isAdjacent() test succeeded" )


def test_diagonal_map( aItems ):

	nbItems = len( aItems )

	for i in range( 0, nbItems ):
		indices = aItems[i]
		if len(indices) != 3:
			print( "Diagonal map test failed: vertex " + str(i) )

		v = sum( indices )
		v += i
		if v != 14:
			print( "Diagonal map test failed: vertex " + str(i) )
			return(1)

	print( "Diagonal map test succeeded" )
	
def test_diagonal_func( f ):

    # check all success cases
    
    v1 = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
    v2 = [2,5,7,3,6,4,0,5,7,1,4,6,6,3,1,7,0,2,4,1,3,5,2,0]
    
    for i in range(0, len(v1),1 ):
        if f( v1[i], v2[i] ) == False:
            print( "  Failed: isDiagonal( " + str(v1[i]) + ", " + str(v2[i]) + " )" )
            return
    
    # check all fail cases
    v1 = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,0,1,2,3,4,5,6,7]
    v2 = [1,3,4,6,0,2,5,7,1,3,4,6,0,2,5,7,0,2,5,7,1,3,4,6,0,2,5,7,1,3,4,6,0,1,2,3,4,5,6,7]
    
    for i in range(0, len(v1),1 ):
        if f( v1[i], v2[i] ) == True:
            print( "  Failed: isDiagonal( " + str(v1[i]) + ", " + str(v2[i]) + " )" )
            return
            
    print( "isDiagonal() test succeeded" )

def test_opposite_map( aItems ):

	nbItems = len( aItems )
	for i in range ( 0, nbItems ):
		a = aItems[i]
		b = aItems[(nbItems-i)-1]

		if ( a + b != 7 or a < 0 or b < 0 or a == b ):
			print( "Opposite map test failed" )
			return(1)

	print( "Opposite map test succeeded" )


def test_opposite_func( f ):

    v1 = [0,1,2,3,4,5,6,7]
    v2 = [6,7,4,5,2,3,0,1]
    
    for i in range(0, len(v1),1 ):
        for j in range( 0, len(v1), 1):
            r = f( v1[i], j )
            if ( r == True and j != v2[i] ) or (r == False and j == v2[i]):
                print( "  Failed: isOpposite( " + str(v1[i]) + ", " + str(j) + " )" )
                return
            
    print( "isOpposite() test succeeded" )
    
def test_sameface_func( f ):

    v = [ [0,1,2,3], [0,1,4,5], [0,3,4,7], [1,2,5,6], [2,3,6,7], [4,5,6,7] ]
    
    for i in range(0,5):
        for j in range(i+1,8):
            for k in range(j+1,8):
                for m in range(k+1,8):
                    
                    expected = False
                    items = [i,j,k,m]
                    if items == v[0] or items == v[1] or items == v[2] or items == v[3] or items == v[4] or items == v[5]:
                        expected = True

                    r = f( items )
                    
                    if r != expected:
                        print( "  Failed: isPolesOnSameFace( " + str( items ) + " )" )
                        return       
            
    print( "isPolesOnSameFace() test succeeded" )
    
def test_polesdiagonal_func( f ):

    v = [ 
        [0,1,6,7],
        [0,2,4,6], 
        [0,3,5,6],
        [1,2,4,7],
        [1,3,5,7],
        [2,3,4,5]
    ]
    
    for i in range(0,5):
        for j in range(i+1,8):
            for k in range(j+1,8):
                for m in range(k+1,8):
                    
                    expected = False
                    items = [i,j,k,m]
                    if items == v[0] or items == v[1] or items == v[2] or items == v[3] or items == v[4] or items == v[5]:
                        expected = True

                    r = f( items )
                    
                    if r != expected:
                        print( "  Failed: isPolesOnDiagonal( " + str( items ) + " )" )
                        return       
            
    print( "isPolesOnDiagonal() test succeeded" )
    

def test_poletriad_map( aItems ):

	nbItems = len( aItems )

	for i in range( 0, nbItems ):
		indices = aItems[i]

		if len( indices ) != 4 or indices[0] != i:
			print( "Pole Triad Map test failed: vertex " + str(i) )
			return(1)

		aVisited = [False] * 8

		for j in range( 0, len(indices) ):
			# range test
			if indices[j] < 0 or indices[j] > 7:
				print( "Pole Triad Map test failed: vertex " + str(i) )
				return(1)

			if aVisited[ indices[j] ]:
				print( "Pole Triad Map test failed: vertex " + str(i) )
				return(1)

			aVisited[ indices[j] ] = True

		if i & 1:
			# odd
			if i + 6 != ( sum( indices ) - i ):
				print( "Pole Triad Map test failed: vertex " + str(i) )
				return(1)
		else:
			# even
			if i + 8 != sum( indices ) - i:
				print( "Pole Triad Map test failed: vertex " + str(i) )
				return(1)

	print( "Pole Triad map test succeeded" )
	
def test_poletriad_func( f ):

    v = [
        [0,1,2,5],     
        [0,1,3,4],
        [0,2,3,7], 
        [0,4,5,7],        
        [1,2,3,6], 
        [1,4,5,6],
        [2,5,6,7], 
        [3,4,6,7] 
    ]
    
    for i in range(0,5):
        for j in range(i+1,8):
            for k in range(j+1,8):
                for m in range(k+1,8):
                    
                    expected = False
                    items = [i,j,k,m]
                    if items == v[0] or items == v[1] or items == v[2] or items == v[3] or items == v[4] or items == v[5] or items == v[6] or items == v[7]:
                        expected = True

                    r = f( items )
                    
                    if r != expected:
                        print( "  Failed: isPoleTriad( " + str( items ) + " )" )
                        return       
            
    print( "isPoleTriad() test succeeded" )
    


def test_adjacent_edges_map( aItems ):

	nbItems = len( aItems )

	for i in range( 0, nbItems ):
		indices = aItems[i]
		if len(indices) != 3:
			print( "Adjacent Edges map test failed: vertex " + str(i) )
			return(1)

	print( "Adjacent Edges map test succeeded" )

def test_face_indices_map( aItems ):

	nbItems = len( aItems )

	for i in range( 0, nbItems ):
		indices = aItems[i]
		if len(indices) != 4:
			print( "Face Indices map test failed: vertex " + str(i) )
			return(1)
	print( "Face Indices map test succeeded" )


def test_one_pole( func ):

	for i in range(0,8):
    		bitcode = 1 << i
    		indices = func( bitcode, [i] )
#     		print( "indices: ", indices )
    		if len( indices ) != 4:
        		print( "invalid indices: ", i, indices )

	print( "1-pole tests succeeded" )

def test_seven_pole( func ):
	vertexIndices = []
	for i in range(0,8):
		v       = 255
		mask    = 1 << i
		bitcode = v ^ mask
		for j in range(0,8):
			if j != i:
				vertexIndices.append(j)
		indices = func( bitcode, vertexIndices )
		#print( "indices: ", indices )
		if len( indices ) != 4:
			print( "invalid indices: ", i, indices )

	print( "7-pole tests succeeded" )
	
	
def test_two_pole( func ):
    print( "I have no idea if it succeeded" )
    
