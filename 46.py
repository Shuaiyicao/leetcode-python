class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.ve = []
        self.res = []
    def dfs(self, cnt):
        if cnt == self.n:
            self.res.append(list(self.ve))
            return
        
        for i in range(self.n):
            if self.vis[i] == 1:
                continue
            self.vis[i] = 1
            self.ve.append(self.num[i])
            self.dfs(cnt + 1)
            self.ve.pop()
            self.vis[i] = 0
        
    def permute(self, num):
        n = len(num)
        if n == 0:
            return []
        self.num = num
        self.n = n
        self.vis = [ 0 for i in range(n) ]
        self.dfs(0)
        return self.res