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

rotations = [
[
	[[1, 1.5, 1],
	[0, 1, 0]],

	[[0, 1],
	[1, 1.5],
	[0, 1]],

	[[0, 1, 0],
	[1, 1.5, 1]],

	[[1, 0],
	[1.5, 1],
	[1, 0]],
],
[
	[[0.5, 2, 2],
	[2, 2, 0]],

	[[2, 0],
	[2, 2],
	[0, 2]],

	[[0, 2, 2],
	[2, 2, 0]],

	[[2, 0],
	[2, 2],
	[0, 2]]
],
[
	[[3, 3, 0],
	[0.5, 3, 3]],

	[[0, 3],
	[3, 3],
	[3, 0]],

	[[3, 3, 0],
	[0, 3, 3]],
	[[0, 3],

	[3, 3],
	[3, 0]]
],
[
	[[4, 0.5, 0],
	[4, 4, 4]],

	[[4, 4],
	[4, 0],
	[4, 0]],

	[[4, 4, 4],
	[0, 0, 4]],

	[[0, 4],
	[0, 4],
	[4, 4]]
],
[
	[[0, 0.5, 5],
	[5, 5, 5]],

	[[5, 0],
	[5, 0],
	[5, 5]],

	[[5, 5, 5],
	[5, 0, 0]],

	[[5, 5],
	[0, 5],
	[0, 5]]
],
[
	[[6, 6, 6, 6.5]],

	[[6],
	[6],
	[6],
	[6.5]],

	[[6.5, 6, 6, 6]],

	[[6.5],
	[6],
	[6],
	[6]]
],
[
	[[7.5, 7],
	[7, 7]],

	[[7, 7.5],
	[7, 7]],

	[[7, 7],
	[7, 7.5]],

	[[7, 7],
	[7.5, 7]]
]
]

def rotate_clockwise(shape):
	for row in shape:
		for cell in row:
			if int(cell) != 0:
				block_type = int(cell)
				break
	ind = 0
	for i, ro in enumerate(rotations[block_type-1]):
		if ro == shape:
			ind = i
			break
	return rotations[block_type-1][(ind+1)%4]

def rotate_counterclockwise(shape):
	for row in shape:
		for cell in row:
			if int(cell) != 0:
				block_type = int(cell)
				break
	ind = 0
	for i, ro in enumerate(rotations[block_type-1]):
		if ro == shape:
			ind = i
			break
	if ind-1 < 0:
		ind += 4
	return rotations[block_type-1][(ind-1)%4]

if __name__ == '__main__':
	print("Prettyprint new rotate function: ")
	display_rotations = [[] for i in range(len(tetris_shapes))]
	for s_i, s in enumerate(tetris_shapes):
		for x in range(4):
			display_rotations[s_i].append(s)
			s = rotate_clockwise(s)

	print("-------------------------------")
	pprint(display_rotations, width=18)
