class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def walk(self, x, y, d, cnt, m, n):
        if cnt == m * n:
            return 
        self.res.append(self.matrix[x][y])
        self.matrix[x][y] = -12358123
        if d == (0, 1):     # right
            if y == n - 1 or self.matrix[x][y+1] == -12358123:
                self.walk(x + 1, y, (1, 0), cnt + 1, m, n)
            else:
                self.walk(x, y + 1, (0, 1), cnt + 1, m, n)
        elif d == (1, 0):   # down
            if x == m - 1 or self.matrix[x+1][y] == -12358123:
                self.walk(x, y - 1, (0, -1), cnt + 1, m, n)
            else:
                self.walk(x + 1, y, (1, 0), cnt + 1, m, n)
        elif d == (0, -1):  # left
            if y == 0 or self.matrix[x][y-1] == -12358123:
                self.walk(x - 1, y, (-1, 0), cnt + 1, m, n)
            else:
                self.walk(x, y - 1, (0, -1), cnt + 1, m, n)
        else:   #up
            if x == 0 or self.matrix[x-1][y] == -12358123:
                self.walk(x, y + 1, (0, 1), cnt + 1, m, n)
            else:
                self.walk(x - 1, y, (-1, 0), cnt + 1, m, n)
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
            
        self.res = []
        self.matrix = matrix
        self.walk(0, 0, (0, 1), 0, m, n)
        return self.res