class Solution:
	# @param board, a 2D array
	# Capture all regions by modifying the input board in-place.
	# Do not return any value.
	def bfs(self, x, y):
		queue = [ (x, y) ]
		self.vis[x][y] = True
		ok = True
		while len(queue) > 0:
			xx = queue[-1][0]
			yy = queue[-1][1]
			queue.pop()
			for dx, dy in self.d:
				tx = xx + dx
				ty = yy + dy
				if tx < 0 or ty < 0 or tx >= self.m or ty >= self.n:
					ok = False
					continue
				if self.board[tx][ty] == 'O' and not self.vis[tx][ty]:
					self.vis[tx][ty] = True
					queue.append( (tx, ty) )
		return ok

	def fill(self, x, y):
		queue = [ (x, y) ]
		self.vis2[x][y] = True
		while len(queue) > 0:
			xx = queue[-1][0]
			yy = queue[-1][1]
			self.cng[xx][yy] = 1
			queue.pop()
			for dx, dy in self.d:
				tx = xx + dx
				ty = yy + dy
				if tx < 0 or ty < 0 or tx >= self.m or ty >= self.n:
					continue
				if self.board[tx][ty] == 'O' and not self.vis2[tx][ty]:
					self.vis2[tx][ty] = True
					queue.append( (tx, ty) )

	def solve(self, board):
		m = len(board)
		if m == 0:
			return board
		n = len(board[0])
		self.d = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
		self.m = m
		self.n = n
		self.board = board
		self.vis = [ [ 0 for i in xrange(n) ]  for j in xrange(m) ]
		self.cng = [ [ 0 for i in xrange(n) ]  for j in xrange(m) ]
		for i in xrange(m):
			for j in xrange(n):
				if self.vis[i][j] or self.board[i][j] == 'X':
					continue
				if self.bfs(i, j):
					self.vis2 = [ [ 0 for p in xrange(n) ]  for q in xrange(m) ]
					self.fill(i, j)
		res = []
		for i in xrange(m):
			tmp = ''
			for j in xrange(n):
				if self.board[i][j] == 'X' or self.cng[i][j] == 1:
					tmp += 'X'
				else:
					tmp += 'O'
			res.append(tmp)
		for i in range(m):
			board[i] = res[i]
		#print board