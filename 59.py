class Solution:
    # @return a list of lists of integers
    def fill(self, x, y, d, cnt, n):
        if cnt == n * n:
            return 
        self.res[x][y] = cnt + 1
        if d == (0, 1):     # right
            if y == n - 1 or self.res[x][y+1] != 0:
                self.fill(x + 1, y, (1, 0), cnt + 1, n)
            else:
                self.fill(x, y + 1, (0, 1), cnt + 1, n)
        elif d == (1, 0):   # down
            if x == n - 1 or self.res[x+1][y] != 0:
                self.fill(x, y - 1, (0, -1), cnt + 1, n)
            else:
                self.fill(x + 1, y, (1, 0), cnt + 1, n)
        elif d == (0, -1):  # left
            if y == 0 or self.res[x][y-1] != 0:
                self.fill(x - 1, y, (-1, 0), cnt + 1, n)
            else:
                self.fill(x, y - 1, (0, -1), cnt + 1, n)
        else:   #up
            if x == 0 or self.res[x-1][y] != 0:
                self.fill(x, y + 1, (0, 1), cnt + 1, n)
            else:
                self.fill(x - 1, y, (-1, 0), cnt + 1, n)
                
    def generateMatrix(self, n):
        self.res = [ [ 0 for i in range(n) ] for j in range(n) ]
        self.fill(0, 0, (0, 1), 0, n)
        return self.res