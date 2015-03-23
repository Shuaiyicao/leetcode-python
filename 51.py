class Solution:
    # @return a list of lists of string
    def trans(self, num):
        n = len(num)
        res = []
        for i in range(n):
            res.append(''.join([ 'Q' if num[i] & (1<<j) else '.' for j in range(n) ]))
        return res
        
    def dfs(self, choose, l, r):
        if choose == self.mx:
            self.res.append(list(self.ve))
            return True
        can = self.mx & (~(choose | l | r))
        ok = False
        while can > 0:
            c = can & -can
            can -= c
            self.ve.append(c)
            if self.dfs(choose + c, (l | c) >> 1, (r | c) << 1):
                ok = True
            self.ve.pop()
        return ok
        
    def solveNQueens(self, n):
        self.mx = (1<<n) - 1
        self.ve = []
        self.res = []
        self.dfs(0, 0, 0)
        ret = []
        for solution in self.res:
            ret.append(self.trans(solution))
        return ret