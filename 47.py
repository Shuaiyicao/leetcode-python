class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers 
    def __init__(self):
        self.res = set()
        self.ve = []
    
    def dfs(self, cnt):
        n = len(self.num)
        if cnt == n:
            self.res.add(tuple(self.ve))
            return
        choose = {}
        for i in range(n):
            if self.vis[i]:
                continue
            if self.num[i] in choose:
                continue
            self.ve.append(self.num[i])
            choose[self.num[i]] = True
            self.vis[i] = True
            self.dfs(cnt + 1)
            self.vis[i] = False
            self.ve = self.ve[:-1]
            
    def permuteUnique(self, num):
        n = len(num)
        if n == 0:
            return [ [] ]
        num.sort()
        self.num = num
        self.vis = [ 0 for i in range(n) ]
        self.dfs(0)
        res = []
        for perm in self.res:
            res.append(list(perm))
        return res