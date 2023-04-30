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

def test_opposite_map( aItems ):

	nbItems = len( aItems )
	for i in range ( 0, nbItems ):
		a = aItems[i]
		b = aItems[(nbItems-i)-1]

		if ( a + b != 7 or a < 0 or b < 0 or a == b ):
			print( "Opposite map test failed" )
			return(1)

	print( "Opposite map test succeeded" )


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