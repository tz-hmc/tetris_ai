"""
EDIT: April 2018
It was discovered that rotating clockwise code (from original Pygame implementation)
was incorrect and did not always rotate clockwise.
Direction that rotated would vary.

A solution was found, but speed may be an issue.

Instead, easier to compute rotations once and save to memory.
It was done here, and "prettyprinted." If you have a need to rotate
shapes about a point in a 2D matrix, in 90deg rotations, you can use this script.

I copied it into rotations.py to test the new rotation function there.
"""
import sys
from pprint import pprint
tetris_shapes = [
	[[1, 1.5, 1],
	 [0, 1, 0]],

	[[0.5, 2, 2],
	[2, 2, 0]],

	[[3, 3, 0],
	 [0.5, 3, 3]],

	[[4, 0.5, 0],
	 [4, 4, 4]],

	[[0, 0.5, 5],
	 [5, 5, 5]],

	[[6, 6, 6, 6.5]],

	[[7.5, 7],
	 [7, 7]]
]

def rotate_clockwise_orig(shape):
	"""
	Original from borrowed code
	Tested this, does not seem to actually rotate clockwise
	L and T pieces are rotated counterclockwise
	This is more of like a... matrix transpose? that sometimes gets it right
	1  1  1               1         1
	   1    should be   1 1  not    1  1
	                      1         1
	"""
	return [ [ shape[y][x]
			for y in xrange(len(shape)) ]
			for x in xrange( len(shape[0])-1, -1, -1 ) ]

def rotate_clockwise(shape):
	"""
	New version
	"""
	dic = {}
	shape_type = 0
	origin = (0,0)
	for y in range(len(shape[0])):
		for x in range(len(shape)):
			if shape[x][y] + 0.5 == int(shape[x][y])+1:
				origin = (x,y)
			elif shape[x][y] != 0:
				shape_type = shape[x][y]
	for y in range(len(shape[0])):
		for x in range(len(shape)):
			if int(shape[x][y]) != 0:
				dic[(x,y)] = (x-origin[0], y-origin[1])
	min_x = sys.maxsize
	min_y = sys.maxsize
	max_x = -sys.maxsize
	max_y = -sys.maxsize
	for k,v in dic.iteritems():
			x, y = v
			# For counterclockwise:
			# newx = -y+origin[0]
			# newy = x+origin[1]
			newx = y+origin[0] # x' = y
			newy = -x+origin[1] # y' = -x
			if min_x > newx:
				min_x = newx
			if max_x < newx:
				max_x = newx
			if min_y > newy:
				min_y = newy
			if max_y < newy:
				max_y = newy
			dic[k] = (newx, newy)
	new_shape = [[0 for y in range(min_y, max_y+1)] for x in range(min_x, max_x+1)]
	for k,v in dic.iteritems():
		x, y = v
		oldx, oldy = k
		new_shape[x-min_x][y-min_y] = shape[oldx][oldy]
	return new_shape

"""
Some automated testing to ensure correctness
Note: Doing the "sort of" rotation matrix is still a little wasteful
	for our needs. Would probably be much faster to save all the possible
	rotations and pull them out when necessary.
"""

print("Testing old rotate function: ")
for s in tetris_shapes:
	print("Original shape:")
	pprint(s, width=20)
	for x in range(4):
		print("Rotation"+str(x))
		s = rotate_clockwise_orig(s)
		pprint(s, width=18)
	print("-------------------------------")

print("===============================")

print("Testing new rotate function: ")
for s in tetris_shapes:
	print("Original shape:")
	pprint(s, width=20)
	for x in range(4):
		print("Rotation"+str(x))
		s = rotate_clockwise(s)
		pprint(s, width=18)
	print("-------------------------------")

print("Prettyprint new rotate function: ")
display_rotations = [[] for i in range(len(tetris_shapes))]
for s_i, s in enumerate(tetris_shapes):
	for x in range(4):
		display_rotations[s_i].append(s)
		s = rotate_clockwise(s)

print("-------------------------------")
pprint(display_rotations, width=18)
