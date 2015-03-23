class Solution:
    # @return an integer
    def dfs(self, choose, l, r):
        if choose == self.mx:
            self.ret += 1
            return
        can = self.mx & (~(choose | l | r))
        while can > 0:
            c = can & -can
            can -= c
            self.dfs(choose + c, (l | c) >> 1, (r | c) << 1)
        
        
    def totalNQueens(self, n):
        self.mx = (1<<n) - 1
        self.ret = 0
        self.dfs(0, 0, 0)
        return self.ret