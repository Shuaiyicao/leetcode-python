class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def dfs(self, x, y, st):
        if st + 1 == self.len:
            return True
        tar = self.word[st+1]
        for dx, dy in self.dirs:
            tx = x + dx
            ty = y + dy
            if tx < 0 or ty < 0 or tx >= self.m or ty >= self.n or self.vis.get((tx,ty)):
                continue
            if self.board[tx][ty] != tar:
                continue
            self.vis[(tx,ty)] = True
            if self.dfs(tx, ty, st + 1):
                return True
            self.vis[(tx,ty)] = False
        return False
            
            
    def exist(self, board, word):
        m = len(board)
        if m == 0:
            return False
        if word == '':
            return True
        n = len(board[0])
        
        self.dirs = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]
        self.m = m
        self.n = n
        self.len = len(word)
        self.word = word
        self.board = board
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue
                self.vis = { (i,j):True }
                if self.dfs(i, j, 0):
                    return True
        return False