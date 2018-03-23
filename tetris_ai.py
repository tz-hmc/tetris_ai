# @Author: T. Zhu <tinazhu>
# @Date:   2018-03-11T17:23:31-07:00
# @Email:  tzhu@g.hmc.edu
# @Last modified by:   tinazhu
# @Last modified time: 2018-03-17T18:46:47-07:00

from copy import deepcopy
from pprint import pprint

cols =		10
rows =		22

def check_collision(board, shape, offset):
	#pprint(board)
	#print shape
	#print offset
	off_x, off_y = offset
	for cy, row in enumerate(shape):
		for cx, cell in enumerate(row):
			try:
				if cell and board[ cy + off_y ][ cx + off_x ]:
					return True
			except IndexError:
				return True
	return False

def remove_row(board, row):
	del board[row]
	return [[0 for i in xrange(cols)]] + board

def join_matrixes(mat1, mat2, mat2_off):
	#print mat1, mat2, mat2_off
	off_x, off_y = mat2_off
	for cy, row in enumerate(mat2):
		for cx, val in enumerate(row):
			mat1[cy+off_y-1][cx+off_x] += val
	return mat1

def rotate_clockwise(shape):
	return [ [ shape[y][x]
			for y in xrange(len(shape)) ]
		for x in xrange(len(shape[0]) - 1, -1, -1) ]

class state(object):
	def __init__(self, board, stone, next_stone, stone_x, stone_y, lines=0):
		self.board = board
		self.stone = stone
		self.next_stone = next_stone
		self.stone_x = stone_x
		self.stone_y = stone_y
		self.lines = 0
		self.score = 0
		self.gameover = False

	def __str__(self):
		return "board: "+str(self.board)#+"stone: "+str(self.stone)+str(self.stone_x)+","+str(self.stone_y)
		#return "stone: "+str(self.stone)+str(self.stone_x)+","+str(self.stone_y)

	def new_stone(self):
		try:
			self.stone = self.next_stone.pop(0)
		except:
			pass
		# chance node here?

	def add_cl_lines(self, n):
		linescores = [0, 40, 100, 300, 1200]
		self.lines += n
		self.score += linescores[n] #* self.level
		#if self.lines >= self.level*6:
		#	self.level += 1
		#	newdelay = 1000-50*(self.level-1)
		#	newdelay = 100 if newdelay < 100 else newdelay
		#	pygame.time.set_timer(pygame.USEREVENT+1, newdelay)

	def rotate_stone(self):
		if not self.gameover:
			new_stone = rotate_clockwise(self.stone)
			if not check_collision(self.board,
			                       new_stone,
			                       (self.stone_x, self.stone_y)):
				self.stone = new_stone

	def drop(self, manual):
		if not self.gameover:
			self.score += 1 if manual else 0
			self.stone_y += 1
			if check_collision(self.board,
			                   self.stone,
			                   (self.stone_x, self.stone_y)):
				self.board = join_matrixes(
				  self.board,
				  self.stone,
				  (self.stone_x, self.stone_y))
				self.new_stone()
				cleared_rows = 0
				while True:
					for i, row in enumerate(self.board[:-1]):
						if 0 not in row:
							self.board = remove_row(
							  self.board, i)
							cleared_rows += 1
							break
					else:
						break
				self.add_cl_lines(cleared_rows)
				return True
		return False

	def insta_drop(self):
		if not self.gameover:
			while(not self.drop(True)):
				#print "d"
				pass

class TetrisAI(object):
	def __init__(self, board, stone, next_stone, stone_x, stone_y):
		self.initState = state(board, stone, next_stone, stone_x, stone_y)

	# return the optimal move
	def ai_move(self):
		#self.test()
		#return None
		q = []
		q.append(self.initState)
		best_s = self.initState
		while(q):
			s = q.pop(0)
			#pprint(s.board)
			if s.score > best_s.score:
				best_s = s
			for x in self.successors(s):
				q.append(x)
		return best_s

	# print successor boards to the current game state
	def test(self):
		for x in self.successors(self.initState):
			pprint(x.board)
			pprint(x.stone)

	# returns possible boards
	def successors(self, init_state):
		# not just hard drop, softdrop, also need softdrop and push in under overhang
		gameStates = []
		s = init_state

		# No more next_stones left, no more successors
		if not s.next_stone:
			print "lol"
			return []

		# Otherwise, generate successors for
		# 10 unique columns, 4 unique rotations
		oldshapes = []
		for i in range(4):
			if s.stone not in oldshapes:
				oldshapes.append(s.stone)
				for c in range(10):
					b = deepcopy(s)
					b.stone_x = c
					if not check_collision(b.board,
					                   b.stone,
					                   (b.stone_x, b.stone_y)):
						b.insta_drop()
						gameStates.append(b)
			s.rotate_stone()
		return gameStates

	def score_board(state):
		"""
		for cy, row in enumerate(state.board):
			for cx, cell in enumerate(row):
				 w_1 = min(0, cx-1)
				 w_2 = min(len(state.board), cx+1)
				 h_1 = min(0, cy-1)
				 h_2 = min(len(state.board[0]), cy+1)
		"""
		return state.score + state.lines
